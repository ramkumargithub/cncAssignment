import gcode
import os

# Input gcode file with CNC instructions. 
file = input("Enter GCode File Name!")
if (file is None):
    file = 'rectangle.gcode'

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, file)
with open(filename, 'r') as f:
    for line in f:
        line = line.strip()
        # Ignore comments and start/end program and program name
        if not line.startswith('(') and not line.startswith('%') and not line.startswith('O') and len(line) > 0:
            print('> ' + line)
            # Ignore line number element from start of line if present
            if line.startswith('N'):
                line = line[3:]
                gcode.GCode.parse_line(line)
            else:
                gcode.GCode.parse_line(line)
                