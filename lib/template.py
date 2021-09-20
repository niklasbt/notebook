#!/usr/bin/env python
import os
import sys
import textwrap
import re

### Functions ##################################################################

def getTemplate(path):
    with open(path,'r') as file:
        template = file.readlines()
    return(template)

def saveTemplate(filename,template):
    with open('lib/templates/'+filename+'.py','w') as outfile:
        outfile.write(textwrap.dedent('''\
            def get_body():
                body = []
                ### Customization here #####################################################
                # body must be a list of strings, to be written to the output file
                body = {body_text}
                ### Customization end ######################################################
                return(body)
        '''.format(length='multi-line', body_text=template)))
    exit()

### Code here ##################################################################

if len(sys.argv) < 2:
    while True:
        try:
            path = input(' Template file: ')
            template = getTemplate(path)
            break
        except FileNotFoundError:
            print('\nFile not found!\n')
else:
    path = sys.argv[1]
    template = getTemplate(path)

#filename = path.split('.')[0]
filename = re.split('\.|/',path)[-2]

saveTemplate(filename,template)
