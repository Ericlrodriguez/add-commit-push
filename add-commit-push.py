import os
import sys

commitCommand = '\ngit commit -m "Update."'
if len(sys.argv) == 3:
    print(sys.argv[1])
    if sys.argv[1] == '-m':
        commitCommand = '\ngit commit -m "' + sys.argv[2] + '"'

print(commitCommand)

print('add-commit-push')
print('\ngit status')
os.system('git status')

print('\ngit add -A')
os.system('git add -A')
print(commitCommand)
os.system(commitCommand)
print('\ngit push')
os.system('git push')