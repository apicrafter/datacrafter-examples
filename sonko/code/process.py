#!/usr/bin/env python
import os
import typer
import json as json
import pymongo

RAW_FILEPATH = '../output/data.bson'
NGO_TABLE = 'orgprofiles2'
RAW_COLLNAME = 'sonko_raw'
STG_COLLNAME = 'sonko_stg'
DB_NAME = 'openngo'

app = typer.Typer()

@app.command()
def loadraw():
    os.system('mongorestore -d %s -c %s %s' % (DB_NAME< RAW_COLLNAME, RAW_FILEPATH))

@app.command()
def stage():
    client = pymongo.MongoClient()
    db = client[DB_NAME]
    db[STG_COLLNAME].drop()
    coll = db[STG_COLLNAME]     
    all_inn = db[RAW_COLLNAME].distinct('inn')
    for inn in all_inn: 
        rows = list(db[RAW_COLLNAME].find({'inn' : inn}))
        org = {}
        for k in ['inn', 'fullname', 'shortname', 'ogrn']:
            org[k] = rows[0][k]
        org['records'] = rows
        print(org['inn'])
        coll.insert_one(org)
    pass

@app.command()
def enrich():
    client = pymongo.MongoClient()
    db = client[DB_NAME]
    ngocoll = db[NGO_TABLE]
    sonkocoll = db[STG_COLLNAME]     
    allinn = sonkocoll.distinct('inn')
    for inn in allinn:
        org = ngocoll.find_one({'inn' : inn})
        if org:
            addon = {}
            for k in ['egrulStatus', 'tags', 'orglists', 'regionCode', 'regionName', 'minjustStatus']:
                if k in org.keys():
                    addon[k] = org[k]
            sonkocoll.update_one({'inn' : inn}, {'$set' : addon})
            print('Updated %s' % (org['inn']))

if __name__ == '__main__':
    app()
    