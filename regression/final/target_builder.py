import subprocess
import os 
from target_checker import target_checker
from datetime import datetime
from variable_setter import VariableSetter

class Target_builder:
    def __init__(self, json_file):
        self.json_file = json_file
        TC = target_checker()
        self.found_targets = TC.found_targets
        self.setter = VariableSetter(self.json_file)
        self.Simulator_CMD = self.setter.Simulator_CMD
        self.compile_opts = self.setter.compile_opts
        self.build = self.build_targets(self.found_targets, self.Simulator_CMD, self.compile_opts)

    def build_targets(self, found_targets, sim_cmd, comp_opts):
        targets = found_targets
        built_targets =[]
        for target in targets:
            subprocess.run(['make', target, f'Simulator_CMD={sim_cmd}', f'compile_opts={comp_opts}', f'output_file={target}'])
            if(os.path.exists(target)):
                message = f"{target} target is built successfully"
                built_targets.append(target) 
            else:
                message = "Build falied some compilation errors has occured"
            with open('build.log', 'a+') as f:
                time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{time_stamp} - {message}\n")
        return built_targets



#class usage
#TB = Target_builder()
#print(f"Targets which are successfully built: {TB.build}")


