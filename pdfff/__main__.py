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
