LAST_TIMESTAMP = '2019/08/16 11:19:20 PM MDT'
import csv
import json
import requests
import time
from itertools import count
from pprint import pformat

with open('utilscripts/secret-config.json') as f:
    secret_config = json.load(f)


class RenameCity(dict): pass


class Already:
    def __init__(self, name):
        self.name = name


def pprint(*args, **kwargs):
    print(*map(pformat, args), **kwargs)


def get(name, *, url='https://maps.googleapis.com/maps/api/geocode', format='json', api_key=secret_config['GMAPS_API_KEY']):
    while True:
        r = requests.get(f'{url}/{format}', {'address': name, 'key': api_key})
        if r.ok:
            break
        elif 'y'.casefold() != input(f'retry? Y/* ({r.status_code}, {r.reason}) ').casefold():
            return None

        time.sleep(1)
    return r.json()


def find_lb(given, d=None, transformations=None):
    name = given
    if name.casefold() in transformations:
        name = transformations[name.casefold()]
    if name in d:
        return Already(name)
    if '(' in name:
        idx = name.index('(')
        name, parenthetical = name[:idx], name[idx + 1 : name.find(')', idx)]
        if name.casefold() in transformations:
            name = transformations[name.casefold()]
        if name in d:
            return Already(name)
        proper_names = ', '.join([word.strip(',.') for word in parenthetical.split() if word[0].isupper()])
        if proper_names:
            name += ', ' + proper_names
    if name.casefold() in transformations:
        name = transformations[name.casefold()]
    if name in d:
        return Already(name)
    print(given, name, sep='\n')
    if input('name ok? /* '):
        name = input('new name (blank to skip): ')
        if not name:
            return None
    if name.casefold() in transformations:
        name = transformations[name.casefold()]
    if name in d:
        return Already(name)
    name += ' Lebanon'
    i = 0
    while True:
        r = get(name)
        pprint(*r['results'], sep='\n', end='\n\n')
        i = input('ok? N/(result index): ')
        if r['results'] and not i.casefold().startswith('n'.casefold()):
            return r['results'][int(i or 0)]
        print('Old name:', name)
        name = input('new name (blank to skip, "city" to rename city): ')
        if not name:
            return None
        if name == 'city':
            return RenameCity(r['results'][int(i[1:] or 0)])


def populate(d, responses, out):
    unknown_counter = count()
    transformations = {}
    found_timestamp = False
    last_timestamp = None
    for response in responses:
        if response[0] == 'Timestamp':
            continue
        if response[0] == LAST_TIMESTAMP:
            found_timestamp = True
            continue
        if not found_timestamp:
            continue
        last_timestamp = response[0]
        name = city = response[1]
        info = find_lb(name, d, transformations)
        if isinstance(info, Already):
            city = info.name
        elif info is not None:
            _, governorate, district, city, *_ = *(i['long_name'] for i in info['address_components'][::-1]), *[None]*4
            if city is None or isinstance(info, RenameCity):
                city = input(f'Renaming city. Enter nothing to use {name}, . to use"unknown", else enter new name: ')
                if not city:
                    city = name
                elif city == '.':
                    city = f'unknown_{next(unknown_counter)}'
            if name.casefold() != city:
                transformations[name.casefold()] = city
            d[city] = {
                'district': district,
                'governorate': governorate,
                'location': info['geometry'].get('location', None),
                'bounds': info['geometry'].get('bounds', None)
            }
        response[1] = city
        out.append(response)
    if last_timestamp is not None:
        with open('utilscripts/populate_locations.py') as this:
            this_file = this.readlines()
        this_file[0] = f'LAST_TIMESTAMP = {last_timestamp!r}\n'
        with open('utilscripts/populate_locations.py', 'w') as this:
            this.writelines(this_file)


def update_locations(
    new_csv_path='Lebanon_ Dialect Survey.csv',
    old_csv_path='results-normalized.csv',
    json_path='data/locations.json'
  ):
    with open(new_csv_path, 'r', encoding='utf-8') as new_csv_f, \
     open(json_path, 'r', encoding='utf-8') as json_f:
        json_d, out = json.load(json_f), []
        populate(json_d, csv.reader(new_csv_f), out)
    with open(old_csv_path, 'a', encoding='utf-8', newline='') as csv_f, \
     open(json_path, 'w', encoding='utf-8') as json_f:
        csv.writer(csv_f).writerows(out)
        json.dump(json_d, json_f, indent=4)
