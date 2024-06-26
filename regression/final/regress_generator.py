import JSONSettingsInvoker 
from target_builder import Target_builder
from variable_setter import VariableSetter
import json, sys, subprocess
from datetime import datetime

class RegressGenerator:
    def __init__(self, target_json):
        #get the valid settings file for included simulator
        self.json_file = JSONSettingsInvoker.get_file(sys.argv[1])

        #Build the correct targets by invoking each one from the given testdata file
        self.TB = Target_builder(self.json_file)
        self.targets_built = self.TB.build
        print(f"*****Targets successfully built are: {self.targets_built}*****")
        self.output_file = 'regress.scr'

        #set the varaibles of makefile by reading and extracting with key-value_pair
        self.setter = VariableSetter(self.json_file)
        self.test_opts = self.setter.test_opts
        self.log_opts = self.setter.log_opts
        self.trace_opts = self.setter.trace_opts

        #Generates the regress file with commands to run each testcases
        self.regress_file = self.generate_regress(self.targets_built, self.test_opts, self.log_opts, self.trace_opts)

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
        return 'regress.scr'
    


                
#class usage
#RG = RegressRunner(sys.argv[2])

