import json
import sys
from datetime import datetime

class JSONValidator:
    def __init__(self, file_path):
        self.file_path = file_path

    def validate(self):
        try:
            with open(self.file_path, 'r') as file, open('checker.log', 'a') as log_file:
                try:
                    json.load(file)
                    timestamp= datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log_message = f"{timestamp} - {file_path} is successfully checked\n"
                    log_file.write(log_message)
                    print(log_message.strip())
                except json.JSONDecodeError as e:
                    self.log_error(e)
        except FileNotFoundError as e:
            self.log_error(e)

    def log_error(self, error):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp} - Error: {error}\n"
        print(error_message.strip())
        with open('checkers.log', 'a') as log_file:
            log_file.write(error_message)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_json.py <json_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    validator = JSONValidator(file_path)
    validator.validate()
