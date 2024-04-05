
import subprocess

subprocess.run(['jq', '-r', '.tools[] | select(.name == env.TARGET_TOOL) | .Simulator_CMD', 'config.json'], env={'TARGET_TOOL': 'Synopsys VCS'})
