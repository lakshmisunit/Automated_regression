import sys
import subprocess
import datetime
import json


class SimulatorChecker:
    def __init__(self, json_file):
        self.json_file = json_file
        # Get the simulator name from command-line arguments
        self.simulator = sys.argv[1] if len(sys.argv) > 1 else None
        if not self.simulator:
            # Exit if simulator name is not provided
            self.log_message("Please provide the simulator name as a command-line argument in the following format <Simulator_Include>")
            sys.exit(1)
        # Check the path for the specified simulator
        self.result = self.check_path(self.simulator, self.json_file)

    def log_message(self, message):
        """Log messages with timestamp to a file."""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{timestamp}: {message}"
        # Print message to console
        print(message)
        # Append message to log file
        with open('checkers.log', 'a') as log_file:
            log_file.write(formatted_message + '\n')

    def check_output(self, cmd):
        """Run shell command and return output."""
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        return stdout.decode('utf-8') if stdout else stderr.decode('utf-8')

    def check_path(self, included_tool, json_file):
        """Check if the specified simulator path exists."""
        if not json_file:
            # Exit if settings file is not found
            self.log_message(f"Settings file not found for {included_tool}.")
            sys.exit(1)
        with open(json_file, 'r') as f:
            settings = json.load(f)
            key = 'Simulator_CMD'
        sim_cmd = settings[key]
        cmd = f'which {sim_cmd}'
        # Check the path for the simulator command
        sim_path = self.check_output(cmd)
        if f"/{sim_cmd}" in sim_path:
            # Log message if path is found
            self.log_message(f'Path for {sim_cmd} is found.')
            return included_tool
        else:
            # Log message if path is not found
            self.log_message(f"Path for {sim_cmd} is not found. Please include the correct path or available simulator")
            sys.exit(1)

# Usage
#if __name__ == "__main__":
    #sim = SimulatorChecker()


