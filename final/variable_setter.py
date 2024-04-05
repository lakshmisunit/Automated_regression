import json
import sys, os
from datetime import datetime
from variable_extracter import extract_variables
from tool_checker import simulator_setter

class variable_setter:
    def __init__(self):
        self.variable_list = extract_variables(sys.argv[2])
        self.set_simulator = simulator_setter('settings.json')
        self.Tool_name = self.set_simulator.result
        self.json_file = self.select_file(self.Tool_name)
        self.Simulator_CMD = self.set_variable(self.json_file, 'Simulator_CMD')
        self.compile_opts = self.set_variable(self.json_file, 'compile_opts')
        
    def select_file(self, Tool_name):
        if(Tool_name == 'Synopsys VCS'):
            file = 'synopsys_vcs.json'
        elif(Tool_name == 'Mentor Questa'):
            file = 'mentor_questa.json'
        elif(Tool_name == 'Icarus Verilog'):
            file = 'Iverilog.json'
        return file

    def set_variable(self, json_file, variable):
        with open(json_file, 'r') as f:
            settings = json.load(f)
        output = settings[variable]
        return output
        
