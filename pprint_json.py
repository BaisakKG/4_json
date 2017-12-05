import json
import sys

def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def pretty_print_json(json_content):
    print(json.dumps(json_content, sort_keys=True, indent=4, ensure_ascii=False))


if __name__ == '__main__':
    file_json = sys.argv[1]
    load_json = load_data(file_json)
    pretty_print_json(load_json)
    
