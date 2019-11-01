import csv
import json
import regex
from contextlib import suppress

regex.DEFAULT_VERSION = regex.VERSION1

from utilscripts import badjson


def parse(title, current_question):
    print(title)
    lbrack = title.rfind('[')
    if lbrack == -1:
        return title.strip(), title.strip(), None, None, None
    rbrack = title.rfind(']')
    question = title[:lbrack].strip()
    answer = title[lbrack:-1]
    arabic = regex.search(r'[\p{Block=Arabic}[\p{Punctuation}--[\[\]]]()\s\+.]*[\p{Block=Arabic}.]', answer)
    if arabic is not None:
        answer = answer[:arabic.start()] + answer[arabic.end():]
    else:
        arabic = [None]
    english_1 = regex.search(r'\((.+?)\)', answer)
    if english_1 is not None:
        answer = answer[:english_1.start()] + answer[english_1.end():]
        english_1 = [english_1[1]]
    else:
        english_1 = [None]
    english_2 = regex.search(r'[\dA-Za-zāēīōū]?[\dA-Za-z[\p{Punctuation}--[()\[\]]]\sāēīōū]*[\d[\p{Punctuation}--[()\[\]]]A-Za-zāēīōū]', answer) or [None]
    #print(arabic, english_1, english_2)
    return None if current_question == question else question, question, arabic[0], english_1[0], english_2[0]


def normalize_questions(csv_header, json_li):
    json_it = iter(json_li)
    question = current_question = examples = None
    q_idx = -1
    example_idx = 0
    for idx, title in enumerate(csv_header[3:], 3):
        question, current_question, arabic, english_1, english_2 = parse(title, current_question)
        has_examples = any(map(None.__ne__, (arabic, english_1, english_2)))
        if not has_examples:
            q_idx += 1
            csv_header[idx] = f'{q_idx}'
            print(q_idx)
            next(json_it)
            continue
        if question is None:
            example_idx += has_examples
        else:
            example_idx = 0
            q_idx += 1
            _fug = next(json_it)
            assert question == _fug['question'], [question, _fug['question']]
            examples = _fug['examples']
            examples = iter(examples)
        print(q_idx, example_idx, sep='.')
        try:
            example = next(examples)
        except StopIteration:
            print(_fug)
            print(question, current_question, sep='\n')
            raise
        if arabic is not None:
            example['arabic'] = arabic
        if english_1 is not None:
            print(english_1)
            english_1_type = input('[e]nglish or [t]ransliteration? (blank to skip) ')
            if english_1_type:
                english_1_type = ['english', 'transliteration'][english_1_type == 't']
                example[english_1_type] = english_1
        if english_2 is not None:
            print(english_2)
            types = ['english', 'transliteration']
            if english_1_type:
                types.remove(english_1_type)
            types = ' or '.join([f'[{head}]{"".join(tail)}' for head, *tail in types])
            english_2_type = input(f'{types}? (blank to skip) ')
            if english_2_type and not english_1_type.startswith(english_2_type):
                english_1_type = ['english', 'transliteration'][english_1_type == 't']
                example[english_2_type] = english_2
        csv_header[idx] = f'{q_idx}.{example_idx}'
    return csv_header, json_li


def do_questions(csv_path='results-normalized.csv', json_path='src/data/questions.json'):
    with open(csv_path, encoding='utf-8', newline='') as csv_f, open(json_path, encoding='utf-8') as json_f:
        csv_header, json_li = normalize_questions(next(iter(csv.reader(csv_f))), json.load(json_f))
        csv_f.seek(0)
        next(csv_f)
        csv_out = [csv_header, *csv.reader(csv_f)]
    badjson.write(json_li, 'src/data/questions.json')
    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_f:
        csv.writer(csv_f).writerows(csv_out)


def compile_answers(csv_f, json_f, cross_file_answer_map=None):
    '''assumed to be run after do_questions'''
    answer_map_given = True
    if cross_file_answer_map is None:
        answer_map_given = False
        cross_file_answer_map = {}  # {question number: {csv answer: json option}}
    respondents = []
    answers = {}
    json_it = iter(json_f)
    j_question = None
    csv_questions = next(csv_f)[3:]
    for user_id, (timestamp, location, extra_location, *line) in enumerate(csv_f):
        respondents.append({
          'timeCompleted': timestamp,
          'number': user_id,
          'location': location,
          'ala': extra_location,
          'answers': {},
          'otherAnswers': {}
        })
        for question_no, answer in zip(csv_questions, line):
            if '.' not in question_no or question_no.split('.', 1)[1] == '0':
                j_question = None
            if j_question is None:
                try:
                    j_question = next(json_it)
                except StopIteration:
                    json_it = iter(json_f)
                    j_question = next(json_it)
            if question_no not in answers:
                answers[question_no] = {'number': question_no, 'environment': '', 'options': {}, 'otherOptions': {}}
            if '.' in question_no and not answers[question_no]['environment']:
                example_no = int(question_no.split('.')[1])
                answers[question_no]['environment'] = j_question['environmentTemplate'].format(
                  *j_question['examples'][example_no]['environmentArgs']
                )
            option_map = dict(zip(range(1, 1 + len(j_question['optionsList'])), j_question['optionsList']))
            newline_printed = False
            for option in answer.split(';'):
                options = []
                if option and option not in cross_file_answer_map:
                    if not newline_printed:
                        print()
                        newline_printed = True
                    if answer_map_given:
                        which = ''
                    else:
                        print(*(f'{k}: {v}' for k, v in option_map.items()), sep='\n', end='\n\n')
                        which = input(f'{option}: which numbers? (blank for other) ')
                    if which:
                        for i in map(int, which):
                            cross_file_answer_map.setdefault(option, []).append(option_map[i])
                            options.append(option_map[i])
                    else:
                        options = [f'Other: {option}']
                elif option in cross_file_answer_map:
                    options = cross_file_answer_map[option]
                else:
                    options = [None]
                for option in options:
                    if option is None or option.startswith('Other'):
                        answers[question_no]['otherOptions'].setdefault(option, {}).setdefault('answeredBy', []).append(user_id)
                        respondents[-1]['answers'].setdefault(question_no, []).append(-1)
                        respondents[-1]['otherAnswers'].setdefault(question_no, []).append(option)
                    else:
                        number = j_question['options'][option]
                        answers[question_no]['options'].setdefault(number, {}).setdefault('answeredBy', []).append(user_id)
                        if 'indicates' not in answers[question_no]['options'][number]:
                            answers[question_no]['options'][number]['indicates'] = [
                            j_question['insights'][primary][secondary]
                            for primary, primary_li in enumerate(j_question['optionsIndicate'][number])
                            for secondary in primary_li
                            ]
                        respondents[-1]['answers'].setdefault(question_no, []).append(number)
    return cross_file_answer_map, respondents, answers


def do_compilation(csv_path='results-normalized.csv', json_path='src/data/questions.json', answer_map_path='src/data/cross_file_answer_map.json'):
    with open(csv_path, encoding='utf-8', newline='') as csv_f, \
     open(json_path, encoding='utf-8') as json_f, \
     open(answer_map_path, encoding='utf-8') as answer_map:
        cross_file_answer_map, respondents, question_answered_by_map = compile_answers(
          csv.reader(csv_f),
          json.load(json_f),
          cross_file_answer_map=json.load(answer_map)
        )
    with open('src/data/cross_file_answer_map.json', 'w', encoding='utf-8') as f:
        json.dump(cross_file_answer_map, f, indent=4)
    with open('src/data/respondents.json', 'w', encoding='utf-8') as f:
        f.write(regex.sub(r'\[\n\s+(.+?)\n\s*]', r'[\1]', json.dumps(respondents, indent=4)))
    with open('src/data/question_answerers.json', 'w', encoding='utf-8') as f:
        f.write(regex.sub(r'(\d),\n\s*', r'\1, ', json.dumps(question_answered_by_map, indent=4)))
    print('\n:)')


def do_special_cases(json_questions_path='src/data/question_answerers.json', json_users_path='src/data/respondents.json'):
    '''assumed to be run after do_compilation()'''
    with open(json_users_path, encoding='utf-8') as user_f, \
     open(json_questions_path, encoding='utf-8') as q_f:
        userj = json.load(user_f)
        qj = json.load(q_f)
        for user in userj:
            user_answers = user['answers']
            user_id = user['number']
            '''
            take care of ka-ta-b?t: -bat was not included in the survey,
            with question 19 saying "if you say -bat, just pick one of
            the options that has the correct syllable count, and your answer
            to how you pronounce 'ktbt' in isolation (#20) will clarify"
            '''
            if 0 in user_answers['19.0']:
                # surprisingly, nobody answered more than one thing for 20
                # but that could still change ofc
                original_20 = user_answers['20']
                adjusted_20 = [0 if i < 3 else 3 for i in original_20]
                # if, for 19.0, they answered both "bat" and "bet", then combine the answers for 20
                # in order to get both e.g. "kat-bat" and "kat-bet". Otherwise if they only answered
                # "bat" for 19.0 then use only the adjusted answers for 20 so only use "kat-bat"
                if len(user_answers['19.0']) == 1:
                    user_answers['20'] = adjusted_20
                    for option in original_20:
                        if option in qj['19.0']['options'] and user_id in qj['19.0']['options'][option]['answeredBy']:
                            qj['19.0']['options'][option]['answeredBy'].remove(user_id)
                else:
                    user_answers['20'] = list(dict.fromkeys(original_20 + adjusted_20))
                for option in adjusted_20:
                    if option in qj['20']['options'] and user_id not in qj['20']['options'][option]['answeredBy']:
                        qj['20']['options'][option]['answeredBy'].append(user_id)
            '''
            take care of the fact that "N/A, I'd never say 3am here" should XOR with the other '3amma'
            options in question 16
            '''
            for qno in (f'16.{minor}' for minor in range(8)):
                if 0 in user_answers[qno]:
                    user_answers[qno] = [0]
                    for i in range(1, 4):
                        if i in qj[qno]['options'] and user_id in qj[qno]['options'][i]['answeredBy']:
                            qj[qno]['options'][i]['answeredBy'].remove(user_id)
            '''
            take care of the fact that "N/A, I don't say this" should XOR with the other 'taba3' options
            in question 32
            '''
            for qno in (f'32.{minor}' for minor in range(8)):
                if 0 in user_answers[qno]:
                    user_answers[qno] = [0]
                    for i in range(1, 5):
                        if i in qj[qno]['options'] and user_id in qj[qno]['options'][i]['answeredBy']:
                            qj[qno]['options'][i]['answeredBy'].remove(user_id)
    
    with open(json_users_path, 'w', encoding='utf-8') as user_f, \
     open(json_questions_path, 'w', encoding='utf-8') as q_f:
        user_f.write(regex.sub(r'\[\n\s+(.+?)\n\s*]', r'[\1]', json.dumps(userj, indent=4)))
        q_f.write(regex.sub(r'(\d),\n\s*', r'\1, ', json.dumps(qj, indent=4)))


def normalize_map_names(map_path='src/data/map/lb_2009_administrative_districts.geojson', locations_path='src/data/map/locations.json'):
    with open(map_path) as map_f, open(locations_path) as locations_f:
        lb_map, locations = json.load(map_f), json.load(locations_f)
    cross_file_name_map = {'districts': {}, 'governorates': {}}
    districts = cross_file_name_map['districts']
    governorates = cross_file_name_map['governorates']
    # prompt for entry of locations.json names
    for feature in lb_map['features']:
        props = feature['properties']
        if props['GOVERNORATE'] not in governorates:
            governorates[props['GOVERNORATE']] = input(f"'{props['GOVERNORATE']}' (governorate): ") or props['GOVERNORATE']
        props['GOVERNORATE'] = governorates[props['GOVERNORATE']]
        if props['DISTRICT'] not in districts:
            districts[props['DISTRICT']] = input(f"'{props['DISTRICT']}' (district): ") or props['DISTRICT']
        props['DISTRICT'] = districts[props['DISTRICT']]
    with open(map_path, 'w') as f:
        json.dump(lb_map, f)
    with open('src/data/map/cross_file_name_map.json', 'w') as f:
        json.dump(cross_file_name_map, f, indent=4)
