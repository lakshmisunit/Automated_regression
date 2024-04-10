import json
import subprocess
with open('sample.json', 'r') as f:
    data = json.load(f)
Simulator_CMD = data['Simulator_CMD']
compile_opts = data['compile_opts']

subprocess.run(['make', 'build', f'Simulator_CMD={Simulator_CMD}', f'compile_opts={compile_opts}'])

