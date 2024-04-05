import os
import subprocess
import re
import datetime

class MakefileChecker:
    def __init__(self, makefile_path, log_file):
        self.makefile_path = makefile_path
        self.log_file = log_file

    def append_to_log(self, message):
        with open(self.log_file, 'a+') as f:
            error_id = sum(1 for line in f) + 1
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - ID: {error_id} - {message}\n")

    def check_makefile_errors(self):
        if not os.path.exists(self.makefile_path):
            self.append_to_log("Makefile not found")
            return "Makefile not found"

        try:
            output = subprocess.check_output(['make', '-n', '-f', self.makefile_path], stderr=subprocess.STDOUT).decode()
        except subprocess.CalledProcessError as e:
            output = e.output.decode()
            error_message = self.parse_makefile_errors(output)
            self.append_to_log(error_message)
            return error_message

        return "No errors found in Makefile"

    def parse_makefile_errors(self, output):
        if "missing separator" in output:
            return self.handle_missing_separator_error(output)
        if "No rule to make target" in output:
            return self.handle_no_rule_error(output)
        if "Circular dependency dropped" in output:
            return self.handle_circular_dependency_error(output)
        if "multiple target patterns" in output:
            return self.handle_multiple_target_patterns_error(output)
        return f"Syntax error in Makefile:\n{output}"

    def handle_missing_separator_error(self, output):
        line_number = re.search(r"Makefile:(\d+):", output).group(1)
        return f"Missing separator on line {line_number}"

    def handle_no_rule_error(self, output):
        target = re.search(r"make: \*\*\* No rule to make target '(.+)', needed by", output).group(1)
        return f"No target specified for '{target}'"

    def handle_circular_dependency_error(self, output):
        circular_dependencies = re.findall(r"Circular dependency dropped: (.+)", output)
        for dep in circular_dependencies:
            self.append_to_log(f"Circular dependency dropped: {dep}")
        return "Circular dependencies dropped"

    def handle_multiple_target_patterns_error(self, output):
        target = re.search(r"make: \*\*\* \[.+\] Error .+: (.+)", output).group(1)
        return f"Multiple target patterns for '{target}'"

if __name__ == "__main__":
    checker = MakefileChecker('Makefile', 'error.log')
    error_message = checker.check_makefile_errors()
    print(error_message)

