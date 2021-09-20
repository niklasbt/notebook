#!/usr/bin/env python
import os
save_path = '_projects/'

name = input("\n Project name: ")
short_name = input(" Project nickname: ")
excerpt = input(" Short description: ")

lines = ([
    '---',
    'name: '+name,
    'short_name: '+short_name,
    'excerpt_separator: <!--more-->',
    '---\n',
    excerpt,
    '<!--more-->\n'
    ])

filename = os.path.join(save_path,short_name+'.md')
if os.path.isfile(filename):
    print('\n This project exists! \n')
    exit()
with open(filename,'w') as file:
    file.writelines('%s\n' % l for l in lines)
