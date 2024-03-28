import json

class JSONDataReader:
    def __init__(self,json_file_path):
        self.json_file_path = json_file_path;
        self.data_array = []

    def read_data(self, keyword):
        with open(self.json_file_path, 'r') as file:
            data = json.load(file)
            for item in data:
                if keyword in item:
                    self.data_array.append(item[keyword])
        return self.data_array
json_reader = JSONDataReader("config.json")
result = json_reader.read_data('name')
print(result)
