def find_path(d, target, path=None):
    if path is None:
        path = []

    if isinstance(d, dict):
        for k, v in d.items():
            new_path = path + [k]
            if v == target:
                return new_path
            elif isinstance(v, (dict, list)):
                result = find_path(v, target, new_path)
                if result:
                    return result
    elif isinstance(d, list):
        for i, v in enumerate(d):
            new_path = path + [i]
            if v == target:
                return new_path
            elif isinstance(v, (dict, list)):
                result = find_path(v, target, new_path)
                if result:
                    return result
    return None

import json
def read_json(file_name:str='db.json')->dict:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    data = {
        "key1": "value1",
        "key2": {
            "key3": "value3",
            "key4": "value4"
        },
        "key5": [
            "value5",
            "value6",
            {"key6": "value7"}
        ]
    }

    result_path = find_path(data, "value7")
    print(result_path)  # Output: ['key5', 2, 'key6']
