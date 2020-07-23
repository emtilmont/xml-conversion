import os

path = ''
with open('paths.txt', 'r') as file:
    path = file.read().replace('\n', '').strip()

filepaths = []
for dirpath, dirnames, filenames in os.walk(path):
    for f in filenames:
        filepaths.append(os.path.join(dirpath, f))

for filepath in filepaths:
    print(filepath)
    # parse xml