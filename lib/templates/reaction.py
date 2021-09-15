import os

### Exceptions #################################################################
class nullReagent(Exception):
    pass
################################################################################

def get_body():
    body = []
    ### Customization here #####################################################
    # body must be a list of strings, to be written to the output file
    while True:
        try:
            os.system('clear')
            print('#'*(os.get_terminal_size()[0]))
            reagentNo = int(input(' # of reagents: '))
            if reagentNo < 1:
                raise nullReagent
            break
        except ValueError:
            input('\nInvalid number!\n')
        except nullReagent:
            input('\nInvalid number!\n')
    # List of reagent numbers as string
    reagentList = []
    for k in range(reagentNo):
        reagentList.append(str(k+1))

    # Define content for header string
    header_string = ''
    for k in range(reagentNo-1):
        header_string = header_string+' Reagent '+reagentList[k]+' |+|'
    header_string = header_string + ' Reagent '+reagentList[-1]+r' |$\rightarrow$|'

    # Define content for MW string
    MW_string = ''
    for k in range(reagentNo):
        MW_string = MW_string + ' MW'+reagentList[k]+' ||'
    MW_string = MW_string + ' MWProduct |'

    # Define content for Equiv string
    Equiv_string = ''
    for k in range(reagentNo):
        Equiv_string = Equiv_string + ' Equiv'+reagentList[k]+' ||'
    Equiv_string = Equiv_string + ' |'

    # Define content for mmol string
    mmol_string = ''
    for k in range(reagentNo):
        mmol_string = mmol_string + ' mmol'+reagentList[k]+' ||'
    mmol_string = mmol_string + ' |'

    # Define content for g string
    g_string = ''
    for k in range(reagentNo):
        g_string = g_string + ' g'+reagentList[k]+' ||'
    g_string = g_string + ' *Theory:* -- |'

    # Define content for mL string
    mL_string = ''
    for k in range(reagentNo):
        mL_string = mL_string + ' mL'+reagentList[k]+' ||'
    mL_string = mL_string + ' |'

    # Define content for rho string
    rho_string = ''
    for k in range(reagentNo):
        rho_string = rho_string + ' rho'+reagentList[k]+' ||'
    rho_string = rho_string + ' |'

    body_header = '||'+header_string+'Product|\n'
    body_table = '|'+':---:|'*(reagentNo*2+2)+'\n'
    body_MW = '|**MW**|'+MW_string+'\n'
    body_Equiv = '|**Equiv**|'+Equiv_string+'\n'
    body_mmol = '|**mmol**|'+mmol_string+'\n'
    body_g = '|**g**|'+g_string+'\n'
    body_mL = '|**mL**|'+mL_string+'\n'
    body_rho = r'|$\rho$|'+rho_string+'\n'

    body = (['### References\n',
             '### Reagents\n\n',
             body_header,
             body_table,
             body_MW,
             body_Equiv,
             body_mmol,
             body_g,
             body_mL,
             body_rho,
             '\n### Procedure\n',
             '---\n',
             '### Notes\n',
             '[^1]: This is a note.'
            ])
    ### Customization end ######################################################
    return(body)
