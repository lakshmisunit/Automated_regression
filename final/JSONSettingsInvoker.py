def get_file(selected_tool):
    file = ""
    if(selected_tool == "VCS_Include"):
        file = "synopsys_vcs.json"
    elif(selected_tool == "Questa_Include"):
        file = "questa.json"
    elif(selected_tool == "Iverilog_Include"):
        file = "iverilog.json"
    else:
        message = f"check if the simulator is misspelled"
    if (file != None):
        return file
    else:
        return message
