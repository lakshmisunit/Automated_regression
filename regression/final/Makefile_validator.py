import os
import subprocess
import re
import datetime
import sys

class MakefileSanityChecker:
    def __init__(self, makefile_path):
        self.makefile_path = makefile_path
        #self.check_existence(self.makefile_path)        
        self.dependencies, self.line_numbers = self.parse_makefile()
        self.message = self.check_makefile_errors()

    def check_existence(self, makefile_path):
        if not os.path.exists(makefile_path):
            self.append_to_log(f"{makefile_path} not found")
            print(f"{makefile_path} not found")
            sys.exit(1)

    def append_to_log(self, message):
        with open('checkers.log', 'a+') as f:
            error_id = sum(1 for line in f) + 1
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{timestamp} - {message}\n")

    def check_makefile_errors(self):

        try:
            output = subprocess.check_output(['make', '-n', '-f', self.makefile_path], stderr=subprocess.STDOUT).decode()
        except subprocess.CalledProcessError as e:
            output = e.output.decode()
            error_message = self.parse_makefile_errors(output)
            self.append_to_log(error_message)
            return error_message

        if not self.check_for_circular_dependencies():
            message = f"{self.makefile_path} is successfully checked"
            self.append_to_log(message)
            print(message)
            return f"{message}"

    def parse_makefile_errors(self, output):
        if "missing separator" in output:
            return self.handle_missing_separator_error(output)
        if "No rule to make target" in output:
            return self.handle_no_rule_error(output)
        if "multiple target patterns" in output:
            return self.handle_multiple_target_patterns_error(output)
        return f"Syntax error in Makefile:\n{output}"

    def handle_missing_separator_error(self, output):
        line_number = re.search(r"Makefile:(\d+):", output).group(1)
        return f"Missing separator on line {line_number}"

    def handle_no_rule_error(self, output):
        target = re.search(r"make: \*\*\* No rule to make target '(.+)', needed by", output).group(1)
        return f"No target specified for '{target}'"

    def handle_multiple_target_patterns_error(self, output):
        target = re.search(r"make: \*\*\* \[.+\] Error .+: (.+)", output).group(1)
        return f"Multiple target patterns for '{target}'"

    def find_circular_dependencies(self, target, visited=None, path=None):
        if visited is None:
            visited = set()
        if path is None:
            path = []
       
        visited.add(target)
        path.append(target)

        for dep in self.dependencies.get(target, []):
            if dep in path:
                error_message = f"Circular dependency found: {' -> '.join(path+[dep])}, at line {self.line_numbers[target]}"
                self.append_to_log(error_message)
                print(error_message)
                return True
            if dep not in visited:
                if self.find_circular_dependencies(dep, visited, path):
                    return True

        path.pop()
        return False

    def check_for_circular_dependencies(self):
        for target in self.dependencies:
            if self.find_circular_dependencies(target):
                return True
        return False

    def parse_makefile(self):
        dependencies = {}
        line_numbers = {}
        with open(self.makefile_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if line.startswith('\t'):
                    continue
                parts = line.strip().split(':')
                if(len(parts) >= 2):
                    target = parts[0].strip()
                    deps = [dep.strip() for dep in parts[1].split()]
                    dependencies[target] = deps
                    line_numbers[target] = line_number
        return dependencies, line_numbers

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py path_to_makefile")
        sys.exit(1)
   
    makefile_path = sys.argv[2]
   
    #checker = MakefileSanityChecker(makefile_path)
    #error_message = checker.message
    #print(error_message)
