#!/usr/bin/env python
import os
from datetime import datetime

def listproj(list):
    print('\nAvailable projects:')
    for k in range(len(list)):
        print('  '+str(k)+': '+list[k])
    print('\n')

def save_entry(title,short_title,project):
    save_path = '_posts/'
    lines = ([
        '---\n',
        'title: '+title+'\n',
        'project: '+project+'\n',
        '---\n',
        ])
    filename = datetime.today().strftime('%Y-%m-%d')+'-'+short_title+'.md'
    fullpath = os.path.join(save_path,filename)
    if os.path.isfile(fullpath):
        print('\n This entry exists! \n')
        exit()
    with open(fullpath,'w') as file:
        file.writelines(lines)

files = [f for f in os.listdir('_projects')]
projects = [os.path.splitext(f)[0] for f in files]
projects.sort()
projects.insert(0,'New project')

listproj(projects)

newproj = int(input('Entry project #: '))

while newproj > len(projects)-1:
    print('\nInvalid project #!')
    listproj(projects)
    newproj = int(input('Entry project #: '))

if newproj == 0:
    print('New project!')
    exec(open('create-project.py').read())
    title = input("\n Entry title: ")
    short_title = input(" Short title: ")
    save_entry(title,short_title,short_name)
else:
    title = input(" Entry title: ")
    short_title = input(" Short title: ")
    save_entry(title,short_title,projects[newproj])
