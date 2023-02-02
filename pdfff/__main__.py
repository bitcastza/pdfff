from pathlib import Path
from fillpdf import fillpdfs
import logging
import sys

def getInput():
    data = {}

    index = -1
    print("Input Anything To Continue:")
    for line in sys.stdin:
        if (index == -1) :
            print(data)
            print("Please insert your surname:")
            data[0]= line.strip('\n')
            del data[0]
            index = 0

        elif (index == 0) :
            data[0]= line.strip('\n')
            print(data)
            print("Please insert your first names:")
            index = 1

        elif (index == 1) :
            data[1]= line.strip('\n')
            print(data)
            print("Please insert your ID:")
            index = 2

        else :
            break
    data[2]= line.strip('\n')
    print(data)
    print("\n\n\n\n DONE \n\n\n\n")



def run():
    
    getInput()

    source = Path('forms')
    fields = []
    for f in source.glob('*.pdf'):
        print(f'Handling file: {f}')
        fillpdfs.print_form_fields(f)
        fields += fillpdfs.get_form_fields(f).keys()
    print('List of fields')
    print(set(fields))


    data_dic = {
    '1':'1', 
    '2':'2', 
    '0':'1234567890', 
    '1_2':'1_2', 
    '5 Nationality':'5 Nationality', 
    '2_2':'2_2', 
    '7 Ordinary places of residence during the 12 months prior to death and the Provinces':'7', 
    '9 Place of birth':'9 Place of birth', 
    '11Has the deceased left a will':
    '11Has the deceased left a will', 
    '12 Marital status at time of death':'12 Marital status at time of death', 
    '13 If married place where married':'13 If married place where married', 
    '14 Full names of surviving spouse':'14 Full names of surviving spouse', 
    'and hisher IDPassport number':'and hisher IDPassport number', 
    '15 State whether marriage was in or out of community of propertywhether accrual system is applicable':'15', 
    'a Names of predeceased spouses andor divorced spouses state opposite name of each whether predeceased or divorced':'a', 
    'b Date of death of predeceased spouses':'b', 
    '16 Masters offices where predeceaseds estates isare registered and numbers of estates if available':'16'}

    fillpdfs.write_fillable_pdf('forms/J294 - Death Notice.pdf', 'test/J294 - Death Notice_filled.pdf', data_dic, False)

if __name__ == "__main__":
    run()