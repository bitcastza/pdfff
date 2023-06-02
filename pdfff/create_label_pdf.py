import argparse
import pathlib
from pypdf import PdfReader, PdfWriter

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("form", type=pathlib.Path)
    args = parser.parse_args()

    reader = PdfReader(args.form)
    fields = reader.get_form_text_fields()
    data_dict = {a: a for a in fields.keys()}
    writer = PdfWriter()
    writer.append(reader)
    for page in writer.pages:
        writer.update_page_form_field_values(page, data_dict)
    with open(f"form-labels/{args.form.name}", "wb") as output_stream:
        writer.write(output_stream)
