from makefile import Makefile
from variable_extracter import extract_variables
import sys

class MakefileHandler:
    def __init__(self, makefile_path):
        #Initialise Makefile Reader
        self.make_reader = Makefile()
        #Set the path to the Makefile
        self.makefile_path = makefile_path

    def read_makefile(self):
        #Read the Makefile and retun the Makefile tree
        return self.make_reader.read(self.makefile_path)

    def extract_variables(self, variables_file):
        #Extract variables from the specified file and return them
        return extract_variables(variables_file)

    def get_remaining_targets(self, variables_file):
        #Read the Makefile
        result = self.read_makefile()
        #Extract variables from the Specified file
        variables_list = self.extract_variables(variables_file)
        #Find the remaining targetsby comparing with the variables-list
        target_list = [x for x in result if x not in variables_list]
        return target_list

if __name__ == "__main__":
    #Initialise the Makefile Handler with the makefile path
    handler = MakefileHandler(sys.argv[1])
    #Get the remaining targets based on the variables list passed as argument
    remaining_targets = handler.get_remaining_targets(sys.argv[1])
    #print the result
    print(remaining_targets)
