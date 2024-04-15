import json
import sys, os
from datetime import datetime

class VariableSetter:
    def __init__(self, json_file):
        self.language = sys.argv[4]
        self.json_file = json_file
        self.Simulator_CMD = self.set_variable(self.json_file, 'Simulator_CMD')
        self.compile_opts = self.set_variable(self.json_file, 'compile_opts')
        self.test_opts = self.extract_run_opts(self.language, self.json_file, 'run_opts', 'test_opts')
        self.trace_opts = self.extract_run_opts(self.language, self.json_file, 'run_opts', 'trace_opts')
        self.log_opts = self.extract_run_opts(self.language, self.json_file, 'run_opts', 'log_opts')
        
    def extract_run_opts(self, language, json_file, run_opt, sub_opt):
        with open(json_file, 'r') as file:
            options = json.load(file)
            actual_language = options.get(run_opt, {})
            opt = options.get(run_opt, {}).get(language, {}).get(sub_opt)
            return opt

    def set_variable(self, json_file, variable):
        with open(json_file, 'r') as f:
            settings = json.load(f)
        output = settings[variable]
        return output

#class usage 
#extracter = VariableSetter()
#print(extracter.test_opts)
