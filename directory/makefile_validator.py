import subprocess
import re, sys
import datetime
from makefile_handler import MakefileHandler

MH = MakefileHandler(sys.argv[1])
targets = MH.get_remaining_targets(sys.argv[1])

def log_error(error_msg):
    with open('checkers.log', 'a') as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}] {error_msg}\n")
    print(error_msg)

def check_makefile_errors(target):
    try:
        result = subprocess.run(['make', '-n' , f'{target}'], check=True, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error running 'make -n {target}':{e}")
        return
    error_output = result.stderr.decode('utf-8')
    if(error_output):
        print(f"-------------ERROR_OUTPUT---------------: {error_output}")
        if 'No makefile found' in error_output:
            log_error('Error: No makefile found.')
        if 'Nothing to be done for' in error_output:
            log_error('Error: No targets specified.')
        if 'missing separator' in error_output:
            log_error('Error: Missing separator.')
        if 'circular dependency dropped' in error_output:
            log_error('Error: Circular dependency dropped.')
        if 'recipe comsmences before first target' in error_output:
            log_error('Error: Recipe commences before first target.')
        if 'is up to date' in error_output:
            log_error('Error: Target is up to date.')
        if 'missing rule before recipe' in error_output:
            log_error('Error: Missing rule before recipe.')
        if 'commands commence before first target' in error_output:
            log_error('Error: Commands commence before first target.')
        if 'multiple target patterns' in error_output:
            log_error('Error: Multiple target patterns.')
        if 'stop.' in error_output:
            log_error('Error: Makefile execution stopped.')
        if 'Error' in error_output:
            log_error('Error: Unknown error in Makefile.')

if __name__ == "__main__":
    for each in targets:
        check_makefile_errors(each)
