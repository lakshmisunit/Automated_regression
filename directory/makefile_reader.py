from makefile import Makefile
from variable_extracter import extract_variables
import sys
make_reader = Makefile()
result = make_reader.read('Makefile')
#print(f"result=${result}")

variables_list = extract_variables(sys.argv[1])
#print(f"variables_list = ${variables_list}")
target_list = [x for x in result if x not in variables_list]

#print(target_list)
