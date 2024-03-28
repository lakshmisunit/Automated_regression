import json
class JSONDataReader:
    def __init__(self, json_file_path):
        self.json_file_path = json_file_path;
        self.data_array = []
        with open(self.json_file_path, 'r') as file:
            self.data = json.load(file)

    def extract_values(self, key):
            arr = []
            obj = self.data
            
            def extract(obj, arr, key):
                if isinstance(obj, dict):
                    for k, v in obj.items():
                        if isinstance(v, (dict, list)):
                            extract(v, arr, key)
                        elif k == key:
                            arr.append(v)
                elif isinstance(obj, list):
                    for item in obj:
                        extract(item, arr, key)
                return arr

            results = extract(obj, arr, key)
            return results

'''with open('settings.json') as f:
    json_object = json.load(f)
def extract_values(obj, key):
    arr = []

    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results
json_reader = JSONDataReader("settings.json")
values = json_reader.extract_values('Simulator')
print(values)'''
