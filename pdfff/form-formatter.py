import random
import argparse
import pathlib
from pypdf import PdfReader, PdfWriter
from pypdf.generic import create_string_object, NameObject


class Suffix:
    options = [
        "11",
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
        "25",
        "26",
        "27",
        "28",
        "29",
        "30",
        "31",
        "32",
        "33",
        "34",
        "35",
        "36",
        "37",
        "38",
        "39",
    ]

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.i == len(self.options):
            self.i = 0
        self.i += 1
        return self.options[self.i]


SUFFIX = iter(Suffix())


def randomHex():
    return next(SUFFIX)


FIELD_NAMES = {
    "1-1-12": "deceased surname",
    "2-1-13": "deceased first name",
    "0-1-14": "deceased id",
    "1-1-15": "date of birth",
    "2-1-16": "date of death",
    "1-1-17": "dated at",
    "2-1-18": "the day",
    "0-1-19": "day of",
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("form", type=pathlib.Path)
    parser.add_argument("--initial", "-i", action="store_true")
    args = parser.parse_args()

    reader = PdfReader(args.form, strict=False)
    i = 0
    for page in reader.pages:
        i += 1
        for annot in page["/Annots"]:
            obj = annot.get_object()
            annotation = {"subtype": obj["/Subtype"], "location": obj["/Rect"]}
            if obj["/Subtype"] == "/Widget" and "/T" in obj:
                if args.initial:
                    if not obj["/T"].isdigit():
                        continue
                    new_field_name = f"{obj['/T']}-{i}-{randomHex()}"
                else:
                    if obj["/T"] not in FIELD_NAMES:
                        continue
                    new_field_name = FIELD_NAMES[obj["/T"]]

                obj.update(
                    {
                        NameObject("/T"): create_string_object(new_field_name),
                    }
                )
                if args.initial:
                    print(obj["/T"])
    fields = reader.get_form_text_fields()
    data_dict = {a: a for a in fields.keys()}
    writer = PdfWriter()
    writer.append(reader)
    for page in writer.pages:
        writer.update_page_form_field_values(page, data_dict)
    with open(f"form-labels/{args.form.name}", "wb") as output_stream:
        writer.write(output_stream)

    data_dict = {a: "" for a in fields.keys()}
    for page in writer.pages:
        writer.update_page_form_field_values(page, data_dict)
    with open(f"forms/{args.form.name}", "wb") as output_stream:
        writer.write(output_stream)
