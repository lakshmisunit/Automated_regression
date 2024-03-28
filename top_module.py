from JSONReader import JSONDataReader

print("provide the path for Test_Data json file and Makefile")
json_reader = JSONDataReader("settings.json")
available_simulators = json_reader.read_data('Simulator')
print("The list of available simulators are:")
count = 0
for each in available_simulators:
    count = count+1
    print(f"{count}. {each}")
simulator_choice = 0
slected_tool = ''
simulator_choice = int(input("select simulator by entering the serial no:"))
print(simulator_choice)
selected_tool = available_simulators[simulator_choice]
print(f" the selected simulator is:{selected_tool}")


    
