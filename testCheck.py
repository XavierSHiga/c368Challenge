import os
import subprocess
files = os.listdir()
for file in files:
    if file.endswith('.py'):
        print(subprocess.check_output(['black', '--check', file]))

