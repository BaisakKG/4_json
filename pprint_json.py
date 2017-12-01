import json
import sys

def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(data):
    print(json.dumps(data, sort_keys=True, indent=4))


if __name__ == '__main__':
    #f_json = r'd:\PythonScript\Devman\4_json\data-6784-2017-11-21.json'
    f_json = sys.argv[1]
    p_json = load_data(f_json)
    pretty_print_json(p_json)
    
