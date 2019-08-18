import csv
import json
import regex

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
            '''
            example['arabic'] = arabic
            '''
        if english_1 is not None:
            '''
            print(english_1)
            english_1_type = input('[e]nglish or [t]ransliteration? (blank to skip) ')
            if english_1_type:
                english_1_type = ['english', 'transliteration'][english_1_type == 't']
                example[english_1_type] = english_1
            '''
        if english_2 is not None:
            '''
            print(english_2)
            types = ['english', 'transliteration']
            if english_1_type:
                types.remove(english_1_type)
            types = ' or '.join([f'[{head}]{"".join(tail)}' for head, *tail in types])
            english_2_type = input(f'{types}? (blank to skip) ')
            if english_2_type and not english_1_type.startswith(english_2_type):
                english_1_type = ['english', 'transliteration'][english_1_type == 't']
                example[english_2_type] = english_2
            '''
        csv_header[idx] = f'{q_idx}.{example_idx}'
    return csv_header, json_li


def do_questions(csv_path='results-normalized.csv', json_path='data/questions.json'):
    with open(csv_path, encoding='utf-8', newline='') as csv_f, open(json_path, encoding='utf-8') as json_f:
        csv_header, json_li = normalize_questions(next(iter(csv.reader(csv_f))), json.load(json_f))
        csv_f.seek(0)
        next(csv_f)
        csv_out = [csv_header, *csv.reader(csv_f)]
    #badjson.write(json_li, 'data/questions.json')
    with open(csv_path, 'w', encoding='utf-8', newline='') as csv_f:
        csv.writer(csv_f).writerows(csv_out)


def compile_answers(csv_f, json_f):
    '''assumed to be run after do_questions'''
    cross_file_answer_map = {}  # {question number: {csv answer: json option}}
    user_answered_map = {}
    answers = {}
    json_it = iter(json_f)
    j_question = None
    csv_questions = next(csv_f)[3:]
    for user_id, (timestamp, location, extra_location, *line) in enumerate(csv_f):
        user_answered_map[user_id] = {
          'timeCompleted': timestamp,
          'location': location,
          '3a': extra_location,
          'answers': {}
        }
        for question_no, answer in zip(csv_questions, line):
            if '.' not in question_no or question_no.split('.', 1)[1] == '0':
                j_question = None
            if j_question is None:
                try:
                    j_question = next(json_it)
                except StopIteration:
                    json_it = iter(json_f)
                    j_question = next(json_it)
            answers[question_no] = {'indicates': ''}
            if '.' in question_no:
                example_no = int(question_no.split('.')[1])
                answers[question_no]['indicates'] = j_question['exampleTemplate'].format(
                  *j_question['examples'][example_no]['templateArgs']
                )
            j_options = j_question['options']
            option_map = dict(zip(range(1, 1 + len(j_options)), j_options))
            newline_printed = False
            for option in answer.split(';'):
                options = []
                if option and option not in cross_file_answer_map:
                    if not newline_printed:
                        print()
                        newline_printed = True
                    print(*(f'{k}: {v}' for k, v in option_map.items()), sep='\n', end='\n\n')
                    which = input(f'{option}: which #? (blank for other) ')
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
                    answers[question_no].setdefault(option, {}).setdefault('answered_by', []).append(user_id)
                    if option is not None and not option.startswith('Other') and 'indicates' not in answers[question_no][option]:
                        answers[question_no][option]['indicates'] = [
                          j_question['answersIndicate'][int(k)][i] for k, v in j_options[option].items() for i in v
                        ]
                    user_answered_map[user_id]['answers'].setdefault(question_no, []).append(option)
                    
    return cross_file_answer_map, user_answered_map, answers


def do_compilation(csv_path='results-normalized.csv', json_path='data/questions.json'):
    with open(csv_path, encoding='utf-8', newline='') as csv_f, open(json_path, encoding='utf-8') as json_f:
        cross_file_answer_map, user_answered_map, question_answered_by_map = compile_answers(
          csv.reader(csv_f),
          json.load(json_f)
        )
    with open('data/cross_file_answer_map.json', 'w', encoding='utf-8') as f:
        json.dump(cross_file_answer_map, f, indent=4)
    with open('data/respondents.json', 'w', encoding='utf-8') as f:
        json.dump(user_answered_map, f, indent=4)
    with open('data/question_answerers.json', 'w', encoding='utf-8') as f:
        json.dump(question_answered_by_map, f, indent=4)
    print(':)')