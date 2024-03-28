import subprocess
import json
'''
tool_name_cmd = 'jq -r .selected_tool config.json'
sim_cmd_cmd = 'jq -r \'.tools[] | select(.name == "$(TOOL_NAME)") | .Simulator_CMD\' config.json'
tool_name_proc = subprocess.Popen(tool_name_cmd, shell=True, stdout=subprocess.PIPE)
tool_name = tool_name_proc.stdout.read().decode().strip()

sim_cmd_cmd = sim_cmd_cmd.replace("S(TOOL_NAME)", tool_name)
sim_cmd_proc = subprocess.Popen(sim_cmd_cmd, shell=True, stdout=subprocess.PIPE)
sim_cmd = sim_cmd_proc.stdout.read().decode().strip()

print(tool_name_cmd, sim_cmd_cmd)
if not (sim_cmd):
    print("does not exist")
else:
    print("exists")'''

TOOL_NAME = subprocess.run(['jq',  '-r', '.selected_tool', 'config.json'])
print(TOOL_NAME)
subprocess.run(['jq', '-r', '.tools[]', '|', f'select(.name == {TOOL_NAME})', '|', '.Simulator_CMD', 'config.json'])
