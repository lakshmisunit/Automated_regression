from target_builder import Target_builder
from variable_setter import VariableSetter
import json, sys, subprocess
from datetime import datetime
class RegressRunner:
    def __init__(self, target_json):
        self.TB = Target_builder()
        self.targets_built = self.TB.build
        print(f"*****Targets successfully built are: {self.targets_built}*****")
        self.output_file = 'regress.scr'
        self.setter = VariableSetter()
        self.test_opts = self.setter.test_opts
        self.log_opts = self.setter.log_opts
        self.trace_opts = self.setter.trace_opts
        self.generate_regress(self.targets_built, self.test_opts, self.log_opts, self.trace_opts)
        self.run_regress(self.output_file)

    def generate_regress(self, built_targets, test_opts, log_opts, trace_opts):
        with open('regress.scr', 'w') as regress_file:
            with open(sys.argv[2], 'r') as test_file:
                data = json.load(test_file)
            extracted_targets = []
            for item in data:
                target_name = item.get('target')
                if target_name in built_targets:
                    test_id = item.get('test_ID','')
                    timestamp = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
                    log_file = f'log/{timestamp}_{test_id}.log'
                    run_cmd = f"./{target_name} {test_opts}={test_id} {log_opts} {log_file} \n"
                    regress_file.write(run_cmd)
    
    def run_regress(self, file):
        with open(file, 'r') as f:
            for line in f:
                subprocess.run(line, shell=True)


                
#class usage
RG = RegressRunner(sys.argv[2])

