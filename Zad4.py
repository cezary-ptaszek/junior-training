import re

pattern = r'^RUN\s\d{6}\sCOMPLETED\.\sOUTPUT\sIN\sFILE\s\w+\.dat\.$'

with open('atoms.txt') as atoms:
    for line in atoms:
        if re.match(pattern, line):
            print(line)
