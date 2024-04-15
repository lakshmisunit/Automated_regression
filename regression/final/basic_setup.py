from path_checker import path_checker
from json_validator import JSONValidator
from Makefile_validator import MakefileSanityChecker
import sys
from log_reader import read_latest_log
 
class StatusValidator():
    def __init__(self):
        self.Json_valid_status = self.json_status_validation()
        self.Makefile_valid_status = self.makefile_status_validation()
 
        
    def json_status_validation(self):
        Json_path_exists = path_checker(sys.argv[2])
        if(Json_path_exists.status == 0):
            valid_json = JSONValidator(sys.argv[2])
            log_information = read_latest_log('checkers.log')
            if"successfully checked" in (log_information):
                return 0
            else:
                print(f"Fix the errors in {sys.argv[2]} to continue")
                return 1
        else:
            sys.exit(1)
 
    def makefile_status_validation(self):
        makefile_path_exists = path_checker(sys.argv[3])
        if(makefile_path_exists.status == 0):
            valid_makefile = MakefileSanityChecker(sys.argv[3])
            log_information = read_latest_log('checkers.log')
            if"successfully checked" in (log_information):
                return 0
            else:
                print(f"Fix the errors in {sys.argv[3]} to continue")
                return 1
        else:
            sys.exit(1)
 
#status = StatusValidator()
#print(status.Json_valid_status)
#print(status.Makefile_valid_status)
