import makefile_reader
import variable_extracter
import sys

total = []
variables_list = []

total = makefile_reader.result(sys.argv[1])
variables_list = variable_extracter.variables(sys.argv[1])

for item in total:
    if (item != variable_list):
        print(item)

