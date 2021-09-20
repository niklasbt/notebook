#!/usr/bin/env python
import os
import importlib

### Exceptions #################################################################
class negativeList(Exception):
    pass

class exceedsList(Exception):
    pass
### Code here ##################################################################

while True:
    try:
        os.system('clear')
        print('OPTIONS '+'#'*(os.get_terminal_size()[0]-8)+'\n')
        print('0: New entry')
        print('1: New project')
        print('2: New template\n')
        selection = int(input(' Selection: '))
        if selection < 0:
            raise negativeList
        elif selection > 2:
            raise exceedsList
        break
    except ValueError:
        input('\nInvalid selection...')
    except negativeList:
        input('\nInvalid selection...')
    except exceedsList:
        input('\nInvalid selection...')

if selection == 0:
    exec(open('lib/entry.py').read())
elif selection == 1:
    exec(open('lib/project.py').read())
else:
    exec(open('lib/template.py').read())
