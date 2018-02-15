# This program formats the typed modules.txt file
# run in iPython with
# %cd /Users/chengnie/Dropbox/Schools/UTD/Teach/sp18Teach/knowledge_management/
# %run module_format.py

for line in open('modules.txt'):
    if '+++' in line:
        print('{:<60}{:<}'.format(*line.strip().split('+++')))
        # print(repr('{:<60}{:<}'.format(*line.strip().split('+++'))))
    else:
        print(line, end="")
        # print(repr(line), end="")
