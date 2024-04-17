import subprocess

class RegressRunner:
    def __init__(self, regress_file):
        self.file = regress_file
        self.execute_cmd(self.file)

    def execute_cmd(self, file):
        with open(file, 'r') as f:
            for line in f:
                subprocess.run(line, shell=True)

runner = RegressRunner('regress.scr')
