import datetime
import pprint
from pathlib import Path
from fillpdf import fillpdfs
from pypdf import PdfReader, PdfWriter
from pyaml_env import parse_config

data = {}

QUESTIONS = [
    "estate number",
    "executor id",
    "executor first name",
    "executor surname",
    "executor relationship to deceased",
    "executor residential address line 1",
    "executor residential address line 2",
    "executor residential address line 3",
    "executor postal address line 1",
    "executor postal address line 2",
    "executor postal address line 3",
    "executor business address line 1",
    "executor business address line 2",
    "executor business address line 3",
    "executor home telephone",
    "executor work telephone",
    "deceased id",
    "deceased first name",
    "deceased surname",
    "deceased date of death",
    "deceased place of death",
    "deceased date of birth",
    "deceased income tax ref. no",
    "deceased district",
    "deceased population group",
    "deceased nationality",
    "deceased occupation",
    "deceased oridinary residence",
    "deceased place of birth",
    "deceased will",
    "deceased marital status",
    "deceased place of marriage",
    "deceased number of wives",
    "surviving spouse id",
    "surviving spouse name",
    "surviving spouse address",
    "father of deceased",
    "mother of deceased",
    "deceased number of customary unions",
    "agent name",
    "agent postal address",
    "agent telephone",
    "bond of security",
    "commissioner of oaths",
    "appointed area",
    "state office held",
    "children info",
    "sibling info",
    "dead sibling info",
    "massed estate",
    "minors under tutorship",
    "minor address",
    "marriage info",
    "predeceased or divorced spouse names",
    "predeceased spouse date of death",
    "masters office and estate number of predeceased spouse",
    "names of children of deceased",
    "capacity",
    "signatory presence at death",
    "signatory identification of deceased",
    "known since",
]


def get_input():
    print("Input Anything To Continue:")

    answers = {}

    for question in QUESTIONS:
        answers[question] = input(f"Please insert {question}: ")

    answers[
        "executor full name"
    ] = f"{answers['executor first name']} {answers['executor surname']}"
    answers[
        "executor full name and id"
    ] = f"{answers['executor full name']}, {answers['executor id']}"
    answers[
        "deceased full name"
    ] = f"{answers['deceased first name']} {answers['deceased surname']}"
    answers[
        "executor residential address line 2 and 3"
    ] = f"{answers['executor residential address line 2']}, {answers['executor residential address line 3']}"
    answers[
        "executor residential address"
    ] = f"{answers['executor residential address line 1']}, {answers['executor residential address line 2']}, {answers['executor residential address line 3']}"
    answers[
        "executor postal address"
    ] = f"{answers['executor postal address line 1']}, {answers['executor postal address line 2']}, {answers['executor postal address line 3']}"
    answers[
        "executor full name and address"
    ] = f"{answers['executor full name']}, {answers['executor residential address']}"
    answers["answer1"] = "yes"
    answers["answer2"] = "yes"
    answers["answer3"] = "yes"
    answers["spouse relationship"] = "Spouse"
    answers["executor home telephone area"] = answers["executor home telephone"][:3]
    answers["executor home telephone remainder"] = answers["executor home telephone"][
        3:
    ]
    answers["executor work telephone area"] = answers["executor work telephone"][:3]
    answers["executor work telephone remainder"] = answers["executor work telephone"][
        3:
    ]
    answers["agent telephone area"] = answers["agent telephone"][:3]
    answers["agent telephone remainder"] = answers["agent telephone"][3:]
    answers["deceased date of birth compressed"] = answers[
        "deceased date of birth"
    ].replace("/", "")
    answers["deceased date of death compressed"] = answers[
        "deceased date of death"
    ].replace("/", "")
    return answers


def run():
    config = parse_config("config.yml")
    user_details = get_input()

    source = Path("forms")
    destination = Path("output")
    destination.mkdir(exist_ok=True)

    for pdf_file in config:
        output_fields = {}
        pdf_filename = pdf_file["filename"]
        for question_id, field in pdf_file["fields"].items():
            try:
                output_fields[field] = user_details[question_id]
            except KeyError:
                print(f"UNABLE TO FIND FIELD {question_id} in {pdf_filename}")
            except TypeError:
                for item in field:
                    try:
                        output_fields[item] = user_details[question_id]
                    except KeyError:
                        print(f"UNABLE TO FIND FIELD {question_id} in {pdf_filename}")

        reader = PdfReader(source / pdf_filename)
        writer = PdfWriter()
        writer.append(reader)
        for page in writer.pages:
            writer.update_page_form_field_values(page, output_fields)
        with open(destination / pdf_filename, "wb") as output_stream:
            writer.write(output_stream)


if __name__ == "__main__":
    run()
