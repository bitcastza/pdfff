from pathlib import Path
from fillpdf import fillpdfs
from pyaml_env import parse_config, BaseConfig
import logging
import sys
import yaml

data = {}


def getInput():        
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

        elif (index == 2) :
            data[2]= line.strip('\n')
            print(data)
            print("Please insert your birth date (DD/MM/YYYY):")
            index = 3
            
        elif (index == 3) :
            data[3]= line.strip('\n')
            print(data)
            print("Please insert your telephone number:")
            index = 4
            
        elif (index == 4) :
            data[4]= line.strip('\n')
            print(data)
            print("Please insert the current date (DD/MM/YYYY):")
            index = 5
            
        elif (index == 5) :
            data[5]= line.strip('\n')
            print(data)
            print("Please insert your birth place:")
            index = 6
            

        else :
            break
    data[index]= line.strip('\n')
    print(data)
    print("\n\n\n\n DONE \n\n\n\n")


def run():

    config = parse_config('pdfff/config.yml')
    
    
    getInput()

    source = Path('forms')
    fields = []
    for f in source.glob('*.pdf'):
        print(f'Handling file: {f}')
        fillpdfs.print_form_fields(f)
        fields += fillpdfs.get_form_fields(f).keys()
    print('List of fields')
    print(set(fields))

    uTelNum = data[4]


    FIRSTNAME = data[1]
    SURNAME = data[0]
    IDNUM = data[2]
    SURVIVING_SPOUSE_NAME = "null"
    SURVIVING_SPOUSE_ADDRESS = "null"
    CURRENT_DATE = data[5]
    NATIONALITY = "null"
    OCCUPATION = "null"
    BIRTH_DATE = data[3]
    BIRTH_PLACE = data[6]
    ADDRESS = "null"
    DECEASED_NAME = "null"
    KNOWN_SINCE = "null"
    SIGNED_AND_SWORN = "null"
    ESTATE_LATE = "null"
    NOMINATES = "null"
    NAME_ROW_1 = "null"
    RELATIONSHIP = "null"
    CAPACITY_ROW_1 = "null"
    DATE_ROW_1 = "null"
    ESTATE = "null"
    ANSWER_1 = "null"
    ANSWER_2 = "null"
    ANSWER_3 = "null"

    print(config)



if __name__ == "__main__":
    run()