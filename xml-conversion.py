import os
from xml.dom.minidom import parse

path = ''
logfile = os.path.join(os.getcwd(), 'output.txt')
with open('paths.txt', 'r') as file:
    path = file.read().replace('\n', '').strip()

filepaths = []
for dirpath, dirnames, filenames in os.walk(path):
    for f in filenames:
        filepaths.append(os.path.join(dirpath, f))

for filepath in filepaths:
    if 'log.txt' not in filepath:
        fxml = open(filepath)
        dom = parse(fxml)
        locs = dom.getElementsByTagName('loc')
        for loc in locs:
            with open(logfile, 'a') as f:
                f.write(loc + '\n')