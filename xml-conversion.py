import os

path = ''
with open('paths.txt', 'r') as file:
    path = file.read().replace('\n', '').strip()

fname = []
for dirpath, dirnames, filenames in os.walk(path):
    for f in filenames:
        fname.append(os.path.join(dirpath, f))

print('fname = %s' %fname)