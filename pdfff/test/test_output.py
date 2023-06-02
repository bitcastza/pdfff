import random
import string
from pathlib import Path
from pyaml_env import parse_config
import pdfff.__main__ as pdfff


def test_get_input(monkeypatch):
    def mockinput(prompt):
        letters = string.ascii_lowercase
        return "".join(random.choice(letters) for i in range(8))

    monkeypatch.setattr("builtins.input", mockinput)

    answers = pdfff.get_input()
    assert len(answers) != 0
    assert (
        answers["executor full name"]
        == f"{answers['executor first name']} {answers['executor surname']}"
    )


def test_full_run(monkeypatch):
    answers = [
        "1234",
        "098765432123",
        "John",
        "Smith",
        "Spouse",
        "1 Street Road",
        "Marina da Gama",
        "Cape Town",
        "2 Street Close",
        "Marina da Gama",
        "Cape Town 7945",
        "3 Street Way",
        "Marina da Gama",
        "Cape Town 7945",
        "0210000000",
        "0211111111",
        "123456789012",
        "Test",
        "Case",
        "2023/02/20",
        "Kaapstad",
        "2023/01/21",
        "123456",
        "Cape",
        "White",
        "South African",
        "Quality Assurance",
        "12 Kerk Road",
        "Welkom",
        "yes",
        "Married",
        "Gansbaai",
        "1",
        "123456",
        "Testus",
        "Casus",
        "Tasticle",
        "Taought",
        "1",
        "Richard",
        "3 Circle",
        "01231223",
        "5 000",
        "Jako",
        "Wynberg",
        "Judge",
        "1 Child",
        "1 sibling",
        "0 siblings",
        "12345",
        "0",
        "4 Kern Road",
        "A marriage occurred",
        "Hello kitty",
        "1995/01/31",
        "Johannesburg 1234",
        "Jake, Bob",
        "Executor",
        "No",
        "Yes",
        "Jan 2023",
    ]

    assert len(answers) == len(pdfff.QUESTIONS)
    answer_iter = iter(answers)

    def mockinput(prompt):
        return next(answer_iter)

    monkeypatch.setattr("builtins.input", mockinput)

    pdfff.run()

    output = Path("output")
    config = parse_config("config.yml")
    assert output.exists()
    for pdf_file in config:
        pdf = output / pdf_file["filename"]
        assert pdf.exists()
