import csv
import json
import regex

regex.DEFAULT_VERSION = regex.VERSION1


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
            csv_header[idx] = f'{q_idx}'
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


def do(csv_path='results-normalized.csv', json_path='data/questions.json'):
    with open(csv_path, encoding='utf-8') as csv_f, open(json_path, encoding='utf-8') as json_f:
        csv_header, json_li = normalize_questions(next(iter(csv.reader(csv_f))), json.load(json_f))
        csv_f.seek(0)
        next(csv_f)
        csv_out = [csv_header, *csv.reader(csv_f)]
    input('done!')
    with open(csv_path, 'w', encoding='utf-8') as csv_f, open(json_path, 'w', encoding='utf-8') as json_f:
        json.dump(json_li, json_f)
        csv.writer(csv_f).writerows(csv_out)
