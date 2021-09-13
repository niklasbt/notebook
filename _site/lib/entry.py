#!/usr/bin/env python
import os
import importlib
from datetime import datetime

### Functions ##################################################################

def getFiles(path,type):
    if type == 'project':
        files = [f for f in os.listdir(path) if f.endswith('.md')]
        files = [os.path.splitext(f)[0] for f in files]
        files.sort()
        files.insert(0,'New project')
        print(files)
    elif type == 'template':
        files = [f for f in os.listdir(path) if f.endswith('.py')]
        for f in files:
            if '__' in f:
                files.remove(f)
        files = [os.path.splitext(f)[0] for f in files]
        files.sort()
        files.insert(0,'Blank template')
    return(files)

def listFiles(list,type):
    os.system('clear')
    if type == 'project':
        print('CHOOSE A PROJECT '+'#'*(os.get_terminal_size()[0]-17))
        print('\nAvailable projects:')
        for k in range(len(list)):
            print('  '+str(k)+': '+list[k])
    if type == 'template':
        print('CHOOSE A TEMPLATE '+'#'*(os.get_terminal_size()[0]-18))
        print('\nAvailable templates:')
        for k in range(len(list)):
            print('  '+str(k)+': '+list[k])

def save_entry(title,short_title,project,body):
    save_path = '../_posts/'
    header = ([
        '---\n',
        'title: '+title+'\n',
        'project: '+project+'\n',
        '---\n',
        ])
    lines = header + body
    for k in range(len(lines)):
        if not lines[k].endswith('\n'):
            lines[k] = "".join((lines[k],'\n'))
    filename = datetime.today().strftime('%Y-%m-%d')+'-'+short_title+'.md'
    fullpath = os.path.join(save_path,filename)
    if os.path.isfile(fullpath):
        print('\n This entry exists! \n')
        exit()
    with open(fullpath,'w') as file:
        file.writelines(lines)

### Exceptions #################################################################
class negativeList(Exception):
    pass

class exceedsList(Exception):
    pass

class badTemplate(Exception):
    pass

### Code here ##################################################################

projects = getFiles('../_projects','project') # Get list of projects
templates = getFiles('templates','template') # Get list of templates
body = []

# Print projects and query user
listFiles(projects,'project')
while True:
    try:
        projectNo = int(input('\nEntry project #: '))
        if projectNo > len(projects)-1:
            raise exceedsList
        elif projectNo < 0:
            raise negativeList
        break
    except ValueError:
        input('\nInvalid project #...')
        listFiles(projects,'project')
    except exceedsList:
        input('\nInvalid project #...')
        listFiles(projects,'project')
    except negativeList:
        input('\nInvalid project #...')
        listFiles(projects,'project')

# If a new project is to be created
if projectNo == 0:
    print('New project!')
    exec(open('project.py').read())
    projName = short_name
else:
    projName = projects[projectNo]

# Query entry info
title = input(" Entry title: ")
short_title = input(" Short title: ")

# List templates and query user
listFiles(templates,'template')
while True:
    try:
        templateNo = int(input('\nTemplate #: '))
        if templateNo > len(templates)-1:
            raise exceedsList
        elif templateNo < 0:
            raise negativeList
        break
    except ValueError:
        input('\nInvalid template #...')
        listFiles(templates,'template')
    except exceedsList:
        input('\nInvalid template #...')
        listFiles(templates,'template')
    except negativeList:
        input('\nInvalid template #...')
        listFiles(templates,'template')

# If a blank template is to be used
if templateNo == 0:
    save_entry(title,short_title,projName,body)
    exit()

# Otherwise, use the chosen template
while True:
    try:
        importedTemplate = importlib.import_module('templates.'+templates[templateNo])
        body = importedTemplate.get_body()
        if not all(type(l) is str for l in body):
            body = []
            raise badTemplate
        save_entry(title,short_title,projName,body)
        exit()
    except AttributeError:
        input('\nBad template!')
        listFiles(templates,'template')
        templateNo = int(input('\nTemplate #: '))
        if templateNo == 0:
            save_entry(title,short_title,projName,body)
            exit()
    except badTemplate:
        input('\nBad template!')
        listFiles(templates,'template')
        templateNo = int(input('\nTemplate #: '))
        if templateNo == 0:
            save_entry(title,short_title,projName,body)
            exit()
