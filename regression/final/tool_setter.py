import subprocess
import sys
from JSONReader import JSONDataReader

class simulator_setter:
    def __init__(self, settings_file):
        self.file_path = settings_file
        self.result = self.select_tool(self.file_path)

    def select_tool(self, json_file):
        json_reader = JSONDataReader(json_file)
        available_simulators = json_reader.extract_values('Simulator')
        print('\nThe list of available simulators are:')
        count = 0
        for each in available_simulators:
            count += 1
            print(f"{count}.{each}")
        choice = 0
        selected_simulator = ''
        choice = int(input("\nSelect simulator by entering the number beside the simulator names: "))
        if(choice>count):
            print("Invalid choice. Please select correct option")
            self.select_tool('settings.json')
        selected_simulator = available_simulators[choice - 1]
        print(f"\nThe selected simulator is: {selected_simulator}")
        self.check_path(selected_simulator)
        return selected_simulator

    def check_output(self, cmd):
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        out = stdout.decode('utf-8')
        err = stderr.decode('utf-8')
        if out:
            return out
        elif err != None:
            self.log_message(err)
            return err

    def log_message(self, message):
        with open('checkers.log', 'a') as log_file:
            log_file.write(message)

    def check_path(self, selected_tool):
        cmd1 = f'jq -r \'.tools[] | select(.Simulator == "{selected_tool}") | .Simulator_CMD\' settings.json'
        simulator_cmd = self.check_output(cmd1)
        cmd2 = f'which {simulator_cmd}'
        simulator_path = self.check_output(cmd2)

        if f"/{simulator_cmd}" in simulator_path:
            print(f"The path for the {selected_tool} is found.\n")
            return 0
        else:
            print(f"The path for {selected_tool} is not present, Please select another tool\n")
            self.select_tool('settings.json')


# class usage
Sim_set = simulator_setter('settings.json')
