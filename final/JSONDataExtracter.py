'''import json, sys

class JSONDataExtracter:
    def __init__(self, target_json_file, options_json_file):
        self.target_json_file = target_json_file
        self.options_json_file = options_json_file

    def read_json(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def extract_data(self):
        target_data = self.read_json(self.target_json_file)
        options_data = self.read_json(self.options_json_file)
        extracted_data = []

        for target in target_data:
            target_name = target.get ('target')
            test_id = target.get('test_ID')
            log_file = target.get('log_file','')

            for options in options_data:
                test_opts = options.get('UVM', {}).get('test_opts', '')
                log_opts = options.get('UVM', {}).get('log_opts', '')
                trace_opts = options.get('UVM', {}).get('trace_opts', '')

                extracted_data.appen({
                    'target_name' : target_name,
                    'test_id' : test_id,
                    'test_opts' : test_opts,
                    'log_opts' : log_opts,
                    'trace_opts' : trace_opts,
                    'log_file' : log_file
                    })
        return extracted_data
#class usage 
target_json_file = sys.argv[1]
options_json_file = 'synopsys_vcs.json'

extractor = JSONDataExtracter(target_json_file, options_json_file)
extracted_data = extractor.extract_data()

for data in extracted_data :
    print(data)'''
import json, sys

class JSONDataExtracter:
    def __init__(self, json_file):
        self.json_file = json_file
        self.data = self.extract_data(self.json_file)

    def extract_data(self, json_file):
        with open (json_file, 'r') as f:
            options = json.load(f)
            Simulator_cmd = options.get('Simulator_CMD')
            compile_opts = options.get('compile_opts')
            test_opts = options.get("run_opts",{}).get("UVM", {}).get("test_opts")
            trace_opts = options.get("run_opts", {}).get("UVM", {}).get("trace_opts")
            log_opts = options.get("run_opts", {}).get("UVM", {}).get("log_opts")
            #print(test_opts)

#class usage
extractor = JSONDataExtracter
print(extractor.extract_data.test_opts)
#print(extracter.test_opts)
