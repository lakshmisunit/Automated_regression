from basic_setup import StatusValidator
from JSONReader import JSONDataReader
import sys
class JSON_target_invoker:
    def __init__(self):
        self.status = StatusValidator()
        self.targets = self.get_targets(self.status.Json_valid_status, self.status.Makefile_valid_status)

    def get_targets(self, json_status, makefile_status):
        if(json_status == 0) and (makefile_status == 0):
            jsonreader = JSONDataReader(sys.argv[1])
            target_list = jsonreader.extract_values('target')
            return target_list
        else:
            sys.exit(1)

TI = JSON_target_invoker()
target_list = TI.targets
if target_list != None:
    print(target_list)
else:
    print(f"No targets are invoked from the {sys.argv[1]} due to errors")
    
