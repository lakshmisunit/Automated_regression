from target_builder import Target_builder
from variable_setter import variable_setter
import json, sys, subprocess
class RegressGenerator:
    def __init__(self, target_json):
        self.TB = Target_builder()
        self.targets_built = self.TB.build
        print(f"*****Targets successfully built are: {self.targets_built}*****")
        self.output_file = 'regress.scr'
        self.setter = variable_setter()
        self.test_opts = self.setter.test_opts
        self.log_opts = self.setter.log_opts
        self.trace_opts = self.setter.trace_opts
        self.generate_regress(self.targets_built, self.test_opts, self.log_opts, self.trace_opts)

    def generate_regress(self, built_targets, test_opts, log_opts, trace_opts):
        with open('regress.scr', 'w') as regress_file:
            with open(sys.argv[1], 'r') as test_file:
                data = json.load(test_file)
            extracted_targets = []
            for item in data:
                target_name = item.get('target')
                if target_name in built_targets:
                    test_id = item.get('test_ID','')
                    log_file = item.get('log_file', '')
                    run_cmd = f"./{target_name} {test_opts}={test_id} {log_opts} {log_file} \n"
                    regress_file.write(run_cmd)
                    self.run_regress(run_cmd)
    
    def run_regress(self, run_cmd):
        subprocess.run(run_cmd, shell=True)

                
             #   if(target
        #with open('regress.scr', '+a') as regress_file:
            #for target in built_targets:
             #  run_statement = f"./target "
#class usage
RG = RegressGenerator(sys.argv[1])

