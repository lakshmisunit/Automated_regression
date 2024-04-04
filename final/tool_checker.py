import subprocess
import sys
import datetime
from JSONReader import JSONDataReader

class simulator_setter:
    def __init__(self, settings_file):
        # Initialize the class with the settings file
        self.file_path = settings_file
        self.result = self.select_tool(self.file_path)

    def select_tool(self, json_file):
        # Select a simulator tool from the JSON file
        json_reader = JSONDataReader(json_file)
        available_simulators = json_reader.extract_values('Simulator')
        print('The list of available simulators are:')
        count = 0
        for each in available_simulators:
            count += 1
            print(f"{count}.{each}")
        choice = 0
        selected_simulator = ''
        choice = int(input("\nSelect simulator by entering the number beside the simulator names: "))
        if choice > 3:
            self.log_message("Invalid choice. Please select a valid option")
            return self.select_tool('settings.json')
        selected_simulator = available_simulators[choice - 1]
        self.log_message(f"The selected simulator is: {selected_simulator}")
        self.check_path(selected_simulator)
        return selected_simulator

    def check_output(self, cmd):
        # Check the output of a command
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        out = stdout.decode('utf-8')
        err = stderr.decode('utf-8')
        if out:
            return out
        else:
            return err

    def log_message(self, message):
        # Log a message with a timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        formatted_message = f"{timestamp}: {message}"
        print(message)
        with open('checkers.log', 'a') as log_file:
            log_file.write(formatted_message + '\n')

    def check_path(self, selected_tool):
        # Check the path for a selected tool
        cmd1 = f'jq -r \'.tools[] | select(.Simulator == "{selected_tool}") | .Simulator_CMD\' settings.json'
        simulator_cmd = self.check_output(cmd1)
        cmd2 = f'which {simulator_cmd}'
        simulator_path = self.check_output(cmd2)

        if f"/{simulator_cmd}" in simulator_path:
            self.log_message(f"The path for the {selected_tool} is found.\n")
            return 0
        else:
            self.log_message(f"The path for {selected_tool} is not present. Please select another tool\n")
            return self.select_tool('settings.json')


# class usage
#Sim_set = simulator_setter('settings.json')
