# -*- coding: utf8 -*-
from pumpilo.sources.jsonl import JSONLinesSource
from pumpilo.


XLS_KEYS = ['territory', 'years', 'id', 'fullname', 'shortname', 'okopf', 'postindex', 'address', 'leader_surname', 'leader_firstname',
        'leader_midname', 'phone', 'fax', 'email', 'numlic', 'lic_date', 'licend_date', 'functions', 'smoreg_date']

XLSX_KEYS = ['id', 'orgname', 'address', 'ogrn_text', 'license', 'reg_date']

def test_bson():
    source = BSONSource(filename='data.bson', stream=None)
    for row in source:
        print(row)


def test_csv():
    source = CSVSource(filename='data.csv', stream=None)
    for row in source:
        print(row)

def test_xls():
    source = XLSSource(filename='data.xls', stream=None, keys=XLS_KEYS)
    for row in source:
        print(row)

def test_xlsx():
    source = XLSXSource(filename='data.xlsx', stream=None, keys=XLSX_KEYS)
    for row in source:
        print(row)



def test_zipxml():
    source = ZIPXMLSource(filename='data.zip', tagname="Документ")
    for row in source.read_bulk(5000):
        print(row)

def test_xml():
    source = XMLSource(filename='data.xml', stream=None, tagname="Документ")
    for row in source:
        print(row)

def test_jsonl():
    source = JSONLinesSource(filename='data.jsonl', stream=None)
    for row in source:
        print(row)

def test_csv():
    source = CSVSource(filename='data.csv', stream=None)
    for row in source:
        print(row)


if __name__ == "__main__":
#    test_bson()
#    test_xlsx()
#    test_xls()
#    test_zipxml()
#    test_xml()
    test_csv()
#    test_jsonl()