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

    questions = [
        "Please insert your surname: ",
        "Please insert your first names: ",
        "Please insert your ID: ",
        "Please insert your birth date (DD/MM/YYYY): ",
        "Please insert your telephone number: ",
        "Please insert the current date (DD/MM/YYYY): ",
        "Please insert your birth place: ",
        "Please insert deceased date of birth (DD/MM/YYYY): ",
        "Please insert deceased ID: ",
        "Please insert your nationality: ",
        "Please insert your occupation: ",
        "Please insert your address: ",
        "Please insert the name of the deceased: ",
    ]


    answers = [
        "", "", "", "", "", "", "", "", "", "",
        "", "", "", "", "", "", "", "", "", ""
        ]

    qIndex = 0
    for i in range(len(questions)):
        print(answers)
        print("\n\n")
        answers[i] = input(questions[i])
        print("\n\n")
        qIndex += 1

    print(answers)
    print("\n\n\n\n")
    return answers

    


def run():

    config = parse_config('pdfff/config.yml')  
    UserDetails = getInput()
  
  
    source = Path('forms')
    fields = []
    for f in source.glob('*.pdf'):
        print(f'Handling file: {f}')
        fillpdfs.print_form_fields(f)
        fields += fillpdfs.get_form_fields(f).keys()
    print('List of fields')
    print(set(fields))

    print('List of fields \n\n\n')

    file = "file"
    for i in range(7):
        fileCounter = i+1
        fileName = file + str(fileCounter)

        config[fileName]['fullname']  = f"{UserDetails[1]} {UserDetails[0]}"
        config[fileName]['id'] = UserDetails[2]
        config[fileName]['Date'] = UserDetails[5]
        config[fileName]['Surname'] = UserDetails[0]
        config[fileName]['First Names'] = UserDetails[1]
        config[fileName]['Nationality'] = UserDetails[9]
        config[fileName]['Occupation'] = UserDetails[10]
        config[fileName]['Place of birth'] = UserDetails[6]
        config[fileName]['Address'] = UserDetails[11]
        config[fileName]['DeceasedName'] = UserDetails[12]


        # ---Additional fields that could be added---
            # config[fileName]['Estate late'] = ""
            # config[fileName]['nominates'] = ""
            # config[fileName]['Relationship  CapacityRow1'] = ""
            # config[fileName]['DateRow1'] = ""
            # config[fileName]['estate'] = ""
            # config[fileName]['Answer1'] = ""
        
    print("\n\n Config File: \n\n")
    print(config)
    

if __name__ == "__main__":
    run()