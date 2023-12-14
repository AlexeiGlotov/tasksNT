import sys
import json

file_path_tests = sys.argv[1]
file_path_values = sys.argv[2]

def get_values(id):
    with open(file_path_values, 'r', encoding='utf-8') as g: 
        val = json.load(g)['values']
        for _v in val:
            if _v['id'] == id:
                return _v['value'] 

def check_values(json):
    for _z in json: 
        _z['value'] = get_values(_z['id'])
        if 'values' in _z.keys():
            check_values(_z['values'])

with open(file_path_tests, 'r', encoding='utf-8') as f:
    tts = json.load(f)['tests']

    check_values(tts)

    with open('report.json', 'w') as file:
        json.dump(tts, file)
        