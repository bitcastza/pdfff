from pathlib import Path
from fillpdf import fillpdfs
from pyaml_env import parse_config, BaseConfig
import logging
import sys
import yaml

data = {}

def getInput():        
    print("Input Anything To Continue:")

    questions = [
        "surname",
        "first name",        
        "id",
        "Deceased ID",
        "Deceased Full Name",
        "Estate No",
        "Deceased Date of Death",
        "Deceased District",
        "Relationship to deceased",
        "Residential Address",
        "Postal Address",
        "Home Tel",
        "Work Tel",
        "Agent Name and Postal Address",
        "Agent Tel",
        "Confirm",
        "Business Address",
        "Deceased date of birth",
        "Deceased Income Tax Ref. No",
        "Surviving Spouse Name",
        "Domicilium citandi et executandi",
        "Bond of Security",
        "Signed At",
        "Current Day and Month",
        "Current Year",
        "fullname and id",
        "Current Day",
        "Current Month",
        "Magistrate",
        "Appointed Area",
        "State Office Held",
        "Deceased Place of Death",
        "Children Info",
        "Father of Deceased",
        "Mother of Deceased",
        "Sibling Info",
        "Dead Sibling Info",
        "Surviving Spouse Address",
        "Massed Estate",
        "Minors Under Tutorship",
        "Address Granted",
        "Current Date",
        "Deceased Surname",
        "Deceased First Names",
        "Deceased Population Group",
        "Deceased Nationality",
        "Deceased Occupation",
        "Deceased Residence",
        "Deceased Place of Birth",
        "Deceased Will",
        "Deceased Marital Status",
        "Deceased Place of Marriage",
        "Surviving Spouse ID",
        "Marriage Info",
        "Predeceased or Divorced Spouse Names",
        "Predeceased Spouse Date of Death",
        "Names of Children of Deceased",
        "fullname and address",
        "Capacity",
        "Signatory Presence",
        "KnownSince",
        "Deceased Wives",
        "Deceased Customary Unions",
        "Person Nominated",
        "Answer1",
        "Answer2",
        "Answer3",
        "Estate Late",
    ]

    answers = {}

    for question in questions:
        answers[question] = input(f"Please insert {question}: ")
        
    answers["fullname"] = f"{answers['first name']} {answers['surname']}"
    answers["name and surname"] = f"{answers['first name']} {answers['surname']}"

    print(answers)
    print("\n\n")
    return answers


def run():
    config = parse_config('pdfff/config.yml')  
    user_details = getInput()
    
    source = Path('forms')
    fields = []
    for f in source.glob('*.pdf'):
        print(f'Handling file: {f}')
        fillpdfs.print_form_fields(f)
        fields += fillpdfs.get_form_fields(f).keys()
    print('List of fields')
    print(set(fields))

    print('List of fields \n\n\n')

    for config_file in config:
        output_fields = {}
        for question_id,field in config_file["fields"].items():
            try:
                output_fields[field] = user_details[question_id]
            except KeyError:
                continue
        fillpdfs.write_fillable_pdf(f"forms/{config_file['filename']}", f"test/{config_file['filename']}", output_fields, False)

    print("\n\n Config File: \n\n")
    print(config)
    

if __name__ == "__main__":
    run()