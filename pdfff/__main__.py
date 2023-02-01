from pathlib import Path
from fillpdf import fillpdfs

def run():
    source = Path('forms')
    fields = []
    for f in source.glob('*.pdf'):
        print(f'Handling file: {f}')
        fillpdfs.print_form_fields(f)
        fields += fillpdfs.get_form_fields(f).keys()
    print('List of fields')
    print(set(fields))

    fillpdfs.write_fillable_pdf('forms/J294 - Death Notice.pdf', 'test/J294 - Death Notice_filled.pdf', {'0': '9602215094081'})


    form_data = {'0': '9602215094081', 'field2': 'value2', 'field3': 'value3'}
    #form_data[0]
    with open('forms/J294 - Death Notice.pdf','rb') as pdf_file:
        pdf_bytes = pdf_file.read()

    filled_pdf_bytes = fillpdfs.write_fillable_pdf(pdf_file, 'test/J294 - Death Notice_filled.pdf', form_data[0])

    with open('forms/J294 - Death Notice.pdf') as filled_pdf_file:
        filled_pdf_file.write(filled_pdf_bytes)