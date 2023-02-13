from pathlib import Path
from fillpdf import fillpdfs
import logging
import sys

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
    
    getInput()

    source = Path('forms')
    fields = []
    for f in source.glob('*.pdf'):
        print(f'Handling file: {f}')
        fillpdfs.print_form_fields(f)
        fields += fillpdfs.get_form_fields(f).keys()
    print('List of fields')
    print(set(fields))

    uSurname = data[0]
    uFirstNames = data[1]
    uID = data[2]
    uBirthDate = data[3]
    uTelNum = data[4]
    uCurDate = data[5]
    uBirthPlace = data[6]
    

    MasterDir_data_dic = {
        'Text1': 'Text1',
        'Text3': 'Text3',
        'Text4-1': 'Text4-1',
        'Text5': 'Text5',
        'Text6': 'Text6',
        'Text7-1': 'Text7-1',
        'Text8': 'Text8',
        'Text9-1': 'Text9-1',
        'Text10-1': 'Text10-1',
        'Text9-2': 'Text9-2',
        'Text10-2': 'Text10-2',
        'Text9-3': 'Text9-3',
        'Text10-3': 'Text10-3',
        'Text9-4': 'Text9-4',
        'Text9-5': 'Text9-5',
        'Text10-4': 'Text10-4',
        'Text10-5': 'Text10-5',
        'Text11-1': 'Text11-1',
        'Text11-2': 'Text11-1',
        'Text11-3': 'Text11-3',
        'Text11-4': 'Text11-4',
        '0': '0',
        '1': '1',
        '2': '2',
        'Text13': 'Text13'
    }
    
    Executor_data_dic = {
        'Estate No': 'Estate No',
        'lWe full names and surname': uFirstNames + ' ' + uSurname,
        '0': '0',
        'Residential address1': 'RESIDENTIAL address1',
        'Business address1': 'Business address1',
        '1': '1',
        'Business address2': 'Business address2',
        '2': '2',
        'Business address3': 'Business address3',
        'ID': uID,
        'Relationship to deceased': 'Relationship to deceased',
        'Full names and surname': 'Full names and surname',
        'Date of birth': 'Date of birth',
        'Date of death': 'Date of death',
        'Identity No': 'Identity No',
        'Income tax ref No': 'Income tax ref No',
        'District in which deceased normally resided': 'District in which deceased normally resided',
        'Name of surviving spouse in case of deceased having been a married woman': 'Name of surviving spouse in case of deceased having been a married woman',
        'contemplated in the Administration of Estates Act No 66 of 1965 as amended at not PO box number': 'contemplated in the Administration of Estates Act No 66 of 1965 as amended at not PO box number',        
        'rand': 'rand',
        'The name and address of myour agent is 1': 'VelileTintoCape Incorporated Attorneys',
        'The name and address of myour agent is 2': '29 Northumberland Road, Bellville',
        'signed at': 'signed at',
        'signed on': 'signed on',
        'year': 'year',
        'PRINT NAME AND SURNAME': 'PRINT NAME AND SURNAME'
    }

    NextOfKin_data_dic = {
        'I': uFirstNames + ' ' + uSurname,
        'of 1': 'of 1',
        'of 2': 'of 2',
        'Print Name and Surname': uFirstNames + ' ' + uSurname,
        'at': 'at',
        '0': '0',
        'day of': 'day of',
        'year': 'year',
        'MagistrateJustice of the PeaceCommissioner of Oaths': 'MagistrateJustice of the PeaceCommissioner of Oaths',
        'Area for which appointed': 'Area for which appointed',
        'If appointment is held ex officio state office held': 'If appointment is held ex officio state office held',
        'died at': 'died at',
        'date': 'date',
        'Names of relatives and degree of relationship1  Surviving spouse': 'Names of relatives and degree of relationship1  Surviving spouse',
        'Names of relatives and degree of relationship2 Children and date of their birth Also state names of predeceased children and their dates of death': 'Names of relatives and degree of relationship2 Children and date of their birth Also state names of predeceased children and their dates of death',
        'Names of relatives and degree of relationshipIgnore questions 3 4 and 5 if the deceased left children or descendants 3 Father of deceased Mother of deceased': 'Names of relatives and degree of relationshipIgnore questions 3 4 and 5 if the deceased left children or descendants 3 Father of deceased Mother of deceased',     
        'Names of relatives and degree of relationshipIgnore questions 4 and 5 if the parents are both alive 4  Brothers and sisters of the deceased  State whether full or half blood and their addresses and dates of birth State the name of the stepparent of half b\\\rrothers and half sisters': 'Names of relatives and degree of relationshipIgnore questions 4 and 5 if the parents are both alive 4  Brothers and sisters of the deceased  State whether full or half blood and their addresses and dates of birth State the name of the stepparent of half b\\\rrothers and half sisters',
        'Names of relatives and degree of relationship5 Names of brothers and sisters who are dead date of deaths and names addresses and dates of birth of their children if any': 'Names of relatives and degree of relationship5 Names of brothers and sisters who are dead date of deaths and names addresses and dates of birth of their children if any'
    }

    estate_inv_dic = {
        'name': 'name',
        'Full name of surviving spouse in a case where spouses were married in community of property': 'Full name of surviving spouse in a case where spouses were married in community of property',
        'Address of surviving spouse': 'Address of surviving spouse',
        'Massed estate of': 'Massed estate of',
        'Full names of minors under tutorship or person in respect of whose property letters of curatorship have been granted': 'Full names of minors under tutorship or person in respect of whose property letters of curatorship have been granted',
        'Full address': 'Full address',
        'lfull name': 'lfull name',
        'of full address': 'of full address',
        '0': '0',
        'premises at': 'premises at',
        'Place': 'Place',
        'Date': 'Date',
        'name and surname': 'name and surname',
        'furnished in the case of an inventory under section 9 of the Act 1': 'furnished in the case of an inventory under section 9 of the Act 1',
        'furnished in the case of an inventory under section 9 of the Act 2': 'furnished in the case of an inventory under section 9 of the Act 2',
        'furnished in the case of an inventory under section 9 of the Act 3': 'furnished in the case of an inventory under section 9 of the Act 3',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9',
        '10': '10',
        '11': '11',
        '12': '12',
        '13': '13',
        '14': '14',
        '15': '15',
        '16': '16',
        '17': '17',
        '18': '18',
        '19': '19',
        '20': '20',
        '21': '21',
        '22': '22',
        '23': '23',
        '24': '24',
        'ValueRTotal': 'ValueRTotal',
        'ValueRTotal2': 'ValueRTotal2',
        'ValueRTotal3': 'ValueRTotal3',
        'ValueRTotal4': 'ValueRTotal4'
    }

    death_data_dic = {
        '1':'1', 
        '2':'2', 
        '0': 123, 
        '1_2':'1_2', 
        '5 Nationality':'5 Nationality', 
        '2_2':'2_2', 
        '7 Ordinary places of residence during the 12 months prior to death and the Provinces':'7', 
        '9 Place of birth':'9 Place of birth', 
        '11Has the deceased left a will':
        '11Has the deceased left a will', 
        '12 Marital status at time of death':'12 Marital status at time of death', 
        '13 If married place where married':'13 If married place where married', 
        '14 Full names of surviving spouse':'14 Full names of surviving spouse', 
        'and hisher IDPassport number':'and hisher IDPassport number', 
        '15 State whether marriage was in or out of community of propertywhether accrual system is applicable':'15', 
        'a Names of predeceased spouses andor divorced spouses state opposite name of each whether predeceased or divorced':'a', 
        'b Date of death of predeceased spouses':'b', 
        '16 Masters offices where predeceaseds estates isare registered and numbers of estates if available':'16',
        'if that be the case the full names of such issue 1' : 'if that be the case the full names of such issue 1',
        'if that be the case the full names of such issue 2':'if that be the case the full names of such issue 2', 
        'a Father':'a Father', 
        'b Mother':'b Mother', 
        '19 Name and address of person signing the death notice':'19', 
        '20 Capacity':'20 Capacity', 
        '21 a Was the signatory present at the deceaseds death':'21 a Was the signatory present at the deceaseds death', 
        'b If the answer to the previous question is no did the signatory identify the deceased after his death':'b',   
        'in the year':'in the year', 
    }

    marital_stat__dic = {
        'I': 'I',
        'Of Address 1': 'Of Address 1',
        'Of Address 2': 'Of Address 2',
        'Deseaced': 'Deseaced',
        'Was well known to me since': 'Was well known to me since',
        '0': '0',
        '1': '1',
        '2': '2',
        'nr1': 'nr1',
        '3': '3',
        'nr2': 'nr2',
        '4': '4',
        'Signed and sworn toaffirmed before me at': 'Signed and sworn toaffirmed before me at',
        'This': 'This',
        'Day of': 'Day of',
        'in the year': 'in the year',
        'Area for which appointed': 'Area for which appointed'
    }

    NomRep_dic = {
        'Estate late': 'Estate late',
        'I  We the undersigned hereby nominates': 'I  We the undersigned hereby nominates',
        'NameRow1': 'NameRow1',
        'Relationship  CapacityRow1': 'Relationship  CapacityRow1',
        'DateRow1': 'DateRow1',
        'NameRow2': 'NameRow2',
        'Relationship  CapacityRow2': 'Relationship  CapacityRow2',
        'DateRow2': 'DateRow2',
        'NameRow3': 'NameRow3',
        'Relationship  CapacityRow3': 'Relationship  CapacityRow3',
        'DateRow3': 'DateRow3',
        'NameRow4': 'NameRow4',
        'Relationship  CapacityRow4': 'Relationship  CapacityRow4',
        'DateRow4': 'DateRow4',
        'NameRow5': 'NameRow5',
        'Relationship  CapacityRow5': 'Relationship  CapacityRow5',
        'DateRow5': 'DateRow5',
        'NameRow6': 'NameRow6',
        'Relationship  CapacityRow6': 'Relationship  CapacityRow6',
        'DateRow6': 'DateRow6',
        'NameRow7': 'NameRow7',
        'Relationship  CapacityRow7': 'Relationship  CapacityRow7',
        'DateRow7': 'DateRow7',
        'NameRow8': 'NameRow8',
        'Relationship  CapacityRow8': 'Relationship  CapacityRow8',
        'DateRow8': 'DateRow8',
        'NameRow9': 'NameRow9',
        'Relationship  CapacityRow9': 'Relationship  CapacityRow9',
        'DateRow9': 'DateRow9',
        'NameRow10': 'NameRow10',
        'Relationship  CapacityRow10': 'Relationship  CapacityRow10',
        'DateRow10': 'DateRow10',
        'NameRow11': 'NameRow11',
        'Relationship  CapacityRow11': 'Relationship  CapacityRow11',
        'DateRow11': 'DateRow11',
        'NameRow12': 'NameRow12',
        'Relationship  CapacityRow12': 'Relationship  CapacityRow12',
        'DateRow12': 'DateRow12',
        'NameRow13': 'NameRow13',
        'Relationship  CapacityRow13': 'Relationship  CapacityRow13',
        'DateRow13': 'DateRow13',
        'NameRow14': 'NameRow14',
        'Relationship  CapacityRow14': 'Relationship  CapacityRow14',
        'DateRow14': 'DateRow14',
        'NameRow15': 'NameRow15',
        'Relationship  CapacityRow15': 'Relationship  CapacityRow15',
        'DateRow15': 'DateRow15',
        'NameRow16': 'NameRow16',
        'Relationship  CapacityRow16': 'Relationship  CapacityRow16',
        'DateRow16': 'DateRow16',
        'NameRow17': 'NameRow17',
        'Relationship  CapacityRow17': 'Relationship  CapacityRow17',
        'DateRow17': 'DateRow17'
    }
    
    report_aff_dic = {
        'I': 'I',
        '0': '0',
        'estate': 'estate',
        'the late': 'the late',
        'Answer': 'Answer',
        'Answer_2': 'Answer_2',
        'Answer_3': 'Answer_3',
        'Signed and sworn toaffirmed before me at': 'Signed and sworn toaffirmed before me at',
        'This': 'This',
        'Day of': 'Day of',
        'in the year': 'in the year',
        'Area for which appointed': 'Area for which appointed'
    }



    
    fillpdfs.write_fillable_pdf('forms/J155 - Undertaking and Acceptance of Masters Directions.pdf', 'test/J155 - Undertaking and Acceptance of Masters Directions_filled.pdf', MasterDir_data_dic, False)
    fillpdfs.write_fillable_pdf('forms/J190 - Acceptance of Trust as Executor.pdf', 'test/J190 - Acceptance of Trust as Executor_filled.pdf', Executor_data_dic, False)
    fillpdfs.write_fillable_pdf('forms/J192 - Next of Kin Affidavit.pdf', 'test/J192 - Next of Kin Affidavit_filled.pdf', NextOfKin_data_dic, False)
    fillpdfs.write_fillable_pdf('forms/J243 - Estate Inventory.pdf', 'test/J243 - Estate Inventory_filled.pdf', estate_inv_dic, False)
    fillpdfs.write_fillable_pdf('forms/J294 - Death Notice.pdf', 'test/J294 - Death Notice_filled.pdf', death_data_dic, False)
    fillpdfs.write_fillable_pdf('forms/Marital Status Declaration.pdf', 'test/Marital Status Declaration_filled.pdf', marital_stat__dic, False)
    fillpdfs.write_fillable_pdf('forms/Nomination to Act as Executor or Masters Representative.pdf', 'test/Nomination to Act as Executor or Masters Representative_filled.pdf', NomRep_dic, False)
    #unable to use apostrophe in "Master's" so the file was renamed to "Masters" instead 
    fillpdfs.write_fillable_pdf('forms/Reporting Affidavit.pdf', 'test/Reporting Affidavit_filled.pdf', report_aff_dic, False)
    




if __name__ == "__main__":
    run()