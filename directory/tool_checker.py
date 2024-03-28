from JSONReader import JSONDataReader
import subprocess

print("provide the path for Test_Data json file and Makefile")
json_reader = JSONDataReader("settings.json")
available_simulators = json_reader.extract_values('Simulator')
print("The list of available simulators are:")
count = 0
for each in available_simulators:
    count = count+1
    print(f"{count}. {each}")
simulator_choice = 0
slected_tool = ''
simulator_choice = int(input("select simulator by entering the serial no:"))
selected_tool = available_simulators[simulator_choice-1]
print(f"\nThe selected simulator is:{selected_tool}")
subprocess.run(['make', 'check_simulator', f'TOOL_NAME={selected_tool}'])
    
