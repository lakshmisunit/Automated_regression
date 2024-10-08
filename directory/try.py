'''from JSONReader import JSONDataReader
import subprocess

print("Provide the path for Test_Data JSON file and Makefile")
json_reader = JSONDataReader("settings.json")
available_simulators = json_reader.read_data('Simulator')
print("The list of available simulators are:")
for index, simulator in enumerate(available_simulators, start=1):
    print(f"{index}. {simulator}")

simulator_choice = int(input("Select simulator by entering the serial number: "))
selected_simulator = available_simulators[simulator_choice - 1]
print(f"Selected simulator: {selected_simulator}")

simulator_cmd = None
for item in json_reader.read_data('Simulator_CMD'):
    if item['Simulator'] == selected_tool:
        simulator_cmd =item['Simulator_CMD']
        break
if simulator_cmd:
    print(f"The command for selected tool is: {simulator_cmd}")
else:
    print(f"Selected simulator not found in the json data")
#simulator_cmd_data = json_reader.read_data('Simulator_CMD')
#print(type(simulator_cmd_data))
#print(simulator_cmd_data)
#simulator_cmd = json_reader.read_data('Simulator_CMD')[selected_simulator]

#print(f"Selected simulator: {selected_simulator}")
#print(f"Simulator command: {simulator_cmd}")'''



import subprocess
import json
with open('settings.json', 'r') as f:
    settings = json.load(f)

Tool_name = "Synopsys VCS"

command = f'jq -r \'.tools[] | select(.Simulator == "{Tool_name}") | .Simulator_CMD\' settings.json'
compile_cmd = f'jq -r \'.tools[] | select(.Simulator == "{Tool_name}") | .compile_opts\' settings.json'

compile_output = subprocess.check_output(compile_cmd, shell=True)
compile_opt = compile_output.decode('utf-8')
print(compile_opt)
output_bytes = subprocess.check_output(command, shell=True)
output = output_bytes.decode('utf-8')
print(output)
