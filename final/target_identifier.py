from target_invoker import JSON_target_invoker
from makefile import Makefile
from variable_extracter import extract_variables
import sys

class Target_identifier:
    def __init__(self):
        self.target_invoke = JSON_target_invoker()
        self.JSON_targets = self.target_invoke.targets
        self.check = 0;
        if(self.JSON_targets == None):
            print(f"No targets are invoked from {sys.argv[2]}")
            self.check = 1;
            sys.exit(1)
        else:
            self.targets = self.extract_targets()

    def extract_targets(self):
        make = Makefile()
        read_make = make.read(sys.argv[3])
        variables_list = extract_variables(sys.argv[3])
        target_list = [x for x in read_make if x not in variables_list]
        return target_list
        
            
#T_identifier = Target_identifier()
#identified_targets = T_identifier.targets
#if identified_targets != None:
#    print(identified_targets)
#else:
#    print(identified_targets)

