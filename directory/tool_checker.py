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
#subprocess.run(['make', 'check_simulator', f'TOOL_NAME={selected_tool}'])
CMD = f'jq -r \'.tools[] | select(.Simulator == "{selected_tool}") | .Simulator_CMD\' settings.json'
simulator_cmd = subprocess.check_output(CMD, shell=True)
sim = simulator_cmd.decode('utf-8')
print(f"sim={sim}")
cmd = f'which {sim}'
process = subprocess.Popen(cmd, shell = True ,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
print(f"output is {stdout}")
print(f"error is:{stderr}")
#print(f"res={res}")

