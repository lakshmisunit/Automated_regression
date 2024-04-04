import subprocess
import json
import sys
from variable_extracter import extract_variables
from tool_checker import simulator_setter

class target_builder:
    def __init__(self):
        self.variable_list = extract_variables(sys.argv[2])

TB = target_builder()
print(TB.variable_list)
