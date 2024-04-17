import re
import sys

#reads the makefile and extracts only the variables and outputs the same in the list

def extract_variables(makefile_path):
    variables = []
    with open(makefile_path, 'r') as makefile:
        for line in makefile:
            match = re.match(r'^([A-Za-z_][A-Za-z0-9_]*)\s*([:+=])?=\s*(.*)$', line)
            if match:
                variable_name = match.group(1)
                variables.append(variable_name)
    return variables

variables = extract_variables(sys.argv[3])
#print(variables)
