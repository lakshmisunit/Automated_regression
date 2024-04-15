import sys
from difflib import get_close_matches
 
valid_options = ['VCS_Include', 'Questa_Include', 'Iverilog_Include']
 
def find_similar_option(option):
    closest_match = get_close_matches(option, valid_options, n=1)
    if closest_match:
        return closest_match    
    return None
 
def get_file(selected_tool):
    file = ""
    if(selected_tool == "VCS_Include"):
        file = "synopsys_vcs.json"
    elif(selected_tool == "Questa_Include"):
        file = "questa.json"
    elif(selected_tool == "Iverilog_Include"):
        file = "iverilog.json"
    else:
        option = sys.argv[1]
        similar_option = find_similar_option(option)
        if similar_option:
            print(f"'{option}' is not a valid option. Did you mean '{similar_option}'? (Y/N)")
            answer = input()
            if answer == 'Y':
                file = get_file(similar_option[0])
            else:
                sys.exit(1)
        else:
            print(f"'{option}' is not valid option. Test is failed due to invalid option included for simulator")
            sys.exit(1)
    if file != None:
        return file
    else:
        print(f"Settings file not found for {included_tool}.")


'''import sys
from difflib import get_close_matches

valid_options = ['VCS_Include', 'Questa_Include', 'Iverilog_Include']

def find_similar_option(option):
    closest_match = get_close_matches(option, valid_options, n=1)
    if closest_match:
        return closest_match    
    return None

def get_file(selected_tool):
    file = ""
    if(selected_tool == "VCS_Include"):
        file = "synopsys_vcs.json"
    elif(selected_tool == "Questa_Include"):
        file = "questa.json"
    elif(selected_tool == "Iverilog_Include"):
        file = "iverilog.json"
    else:
        option = sys.argv[1]
        similar_option = find_similar_option(option)
        if similar_option:
            print(f"'{option}' is not a valid option. Did you mean '{similar_option}'? (Y/N)")
            answer = input()
            if answer == 'Y':
                print(similar_option[0])
                file = get_file(similar_option[0])
        else:
            print(f"'{option}' is not valid option")
    if file != None:
        return file

print(get_file(sys.argv[1]))'''


