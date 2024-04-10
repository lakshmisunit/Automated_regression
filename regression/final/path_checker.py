import os
from datetime import datetime
import sys

class path_checker:
    def __init__(self, file_path):
        self.file = file_path
        self.log_file = 'checkers.log'
        self.status = self.check_existence(file_path)

    def append_to_log(self, message):
        with open(self.log_file, 'a+') as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - {message}\n")

    def check_existence(self, file):
        if not os.path.exists(file):
            message = f"{file} not found"
            self.append_to_log(message)
            print(message)
            return 1
            #sys.exit(1)
        else:
            message = f"{file} exists in the given path"
            self.append_to_log(message)
            print(message)
            return 0

#path_exists = path_checker(sys.argv[1])
#print(path_exists.status)
