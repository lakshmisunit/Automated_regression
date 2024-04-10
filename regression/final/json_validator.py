import json
import sys
from datetime import datetime

class JSONValidator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.valid = self.validate()

    def validate(self):
        """
        Validates the JSON file specified by file_path.
        Logs the validation result to checkers.log.
        """
        try:
            with open(self.file_path, 'r') as file:
                try:
                    json.load(file)
                    self.log_message(f"{self.file_path} is successfully checked")
                except json.JSONDecodeError as e:
                    self.log_error(e)
        except FileNotFoundError as e:
            self.log_error(e)

    def log_message(self, message):
        """
        Logs a message to checkers.log with a timestamp.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{timestamp} - {message}\n"
        print(message)
        with open('checkers.log', 'a') as log_file:
            log_file.write(log_message)

    def log_error(self, error):
        """
        Logs an error message to checkers.log with a timestamp.
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp} - Error: {error}\n"
        print(f"Error: {error}")
        with open('checkers.log', 'a') as log_file:
            log_file.write(error_message)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_json.py <json_file>")
        sys.exit(1)

    file_path = sys.argv[1]
    #validator = JSONValidator(file_path)
    #validator.validate()
