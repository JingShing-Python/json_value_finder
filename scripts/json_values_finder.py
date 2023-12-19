def find_paths(d, target, path=None, paths=None):
    if path is None:
        path = []
    if paths is None:
        paths = []

    if isinstance(d, dict):
        for k, v in d.items():
            new_path = path + [k]
            if v == target:
                paths.append(new_path)
            elif isinstance(v, (dict, list)):
                find_paths(v, target, new_path, paths)
    elif isinstance(d, list):
        for i, v in enumerate(d):
            new_path = path + [i]
            if v == target:
                paths.append(new_path)
            elif isinstance(v, (dict, list)):
                find_paths(v, target, new_path, paths)
    return paths

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
            {"key6": "value7"},
            {"key6": "value7"}
        ]
    }
    result_paths = find_paths(data, "value7")
    print(result_paths)  # Output: [['key5', 2, 'key6'], ['key5', 3, 'key6']]
