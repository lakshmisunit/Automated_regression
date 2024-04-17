import subprocess, sys
from regress_generator import RegressGenerator

class RegressRunner:
    def __init__(self, regress_file):
        self.generator = RegressGenerator(sys.argv[2])
        self.file = self.generator.regress_file
        self.run_regress(self.file)

    def run_regress(self, file):
        with open(file, 'r') as f:
            for line in f:
                subprocess.run(line, shell=True)
#class usage
if(len(sys.argv) < 5):
    print("Usage error: python3 [top_module_script] [Simulator_Include] [json_file] [makefile] [language]")
else:
    runner = RegressRunner('regress.scr')
