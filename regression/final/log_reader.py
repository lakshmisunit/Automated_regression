def read_latest_log(log_file_path):
    try:
        with open(log_file_path, 'r') as file:
            lines = file.readlines()
            if lines:
                latest_log = lines[-1].strip()
                #print("Latest log information:")
                #print(latest_log)
                return f"{latest_log}"

            else:
                print("log file is empty")
    except FileNOtFoundError:
        print("Log file not found")

#log_file_path = 'checkers.log'
#read_latest_log(log_file_path)
