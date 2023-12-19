# json_value_finder
a simple script help you find certain value in a json data structure. It will give you the path to the key.

## Example
```py
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
```
