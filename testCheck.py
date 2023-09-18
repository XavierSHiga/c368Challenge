import os
import subprocess
files = os.listdir()
testOutput = []
filesChecked = []
for file in files:
    if file.endswith('.py'):
        filesChecked.append(file)
        testOutput.append(subprocess.call(['black', '--check', file], stdout=subprocess.DEVNULL))
output = "Black formatting compatibility check:\n"
output += " File Name               Status\n"
output += "---------------------------------------------------------------------------\n"
for i in range(0, len(filesChecked)):
    output += filesChecked[i] + ":              "
    if testOutput[i] == 0:
        output += "Passed\n"
    else:
        output += "Failed\n"
f = open('blackFormatCheck.txt', 'w')
f.write(output)
f.close()
