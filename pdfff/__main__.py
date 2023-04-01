import datetime
from pathlib import Path
from fillpdf import fillpdfs
from pyaml_env import parse_config

data = {}


def getInput():
    print("Input Anything To Continue:")

    questions = [
        "estate number",
        "applicant id",
        "applicant first name",
        "applicant surname",
        "applicant relationship to deceased",
        "applicant residential address line 1",
        "applicant residential address line 2",
        "applicant residential address line 3",
        "applicant postal address line 1",
        "applicant postal address line 2",
        "applicant postal address line 3",
        "applicant business address line 1",
        "applicant business address line 2",
        "applicant business address line 3",
        "applicant home telephone",
        "applicant work telephone",
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
        "signed at",
        "magistrate",
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
        "names of children of deceased",
        "capacity",
        "signatory presence at death",
        "signatory identification of deceased",
        "known since",
        "person nominated",
    ]

    answers = {}

    for question in questions:
        answers[question] = input(f"Please insert {question}: ")

    answers[
        "applicant full name"
    ] = f"{answers['applicant first name']} {answers['applicant surname']}"
    answers[
        "applicant full name and id"
    ] = f"{answers['applicant full name']}, {answers['applicant id']}"
    answers[
        "deceased full name"
    ] = f"{answers['deceased first name']} {answers['deceased surname']}"
    answers[
        "applicant residential address line 2 and 3"
    ] = f"{answers['applicant residential address line 2']} {answers['applicant residential address line 3']}"
    answers[
        "applicant residential address"
    ] = f"{answers['applicant residential address line 1']} {answers['applicant residential address line 2']} {answers['applicant residential address line 3']}"
    answers[
        "applicant full name and address"
    ] = f"{answers['applicant full name']}, {answers['applicant residential address']}"
    today = datetime.date.today()
    answers["current day"] = f"{today.day}"
    answers["current month"] = f"{today.strftime('%B')}"
    answers["current year"] = f"{today.year}"
    answers["current date"] = f"{today.strftime('%d %B %Y')}"
    answers["current day and month"] = f"{today.strftime('%d %B')}"
    answers["answer1"] = "yes"
    answers["answer2"] = "yes"
    answers["answer3"] = "yes"
    answers["applicant home telephone area"] = answers["applicant home telephone"][:3]
    answers["applicant home telephone remainder"] = answers["applicant home telephone"][
        3:
    ]
    answers["applicant work telephone area"] = answers["applicant work telephone"][:3]
    answers["applicant work telephone remainder"] = answers["applicant work telephone"][
        3:
    ]
    answers["agent telephone area"] = answers["agent telephone"][:3]
    answers["agent telephone remainder"] = answers["agent telephone"][3:]
    return answers


def run():
    config = parse_config("config.yml")
    user_details = getInput()

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

        fillpdfs.write_fillable_pdf(
            source.joinpath(pdf_filename),
            destination.joinpath(pdf_filename),
            output_fields,
            False,
        )


if __name__ == "__main__":
    run()
