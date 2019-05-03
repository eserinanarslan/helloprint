# -*- coding: utf-8 -*-
"""
Created on Tuesday April 30 2019

@author: eser.arslan
"""

import os
import json
import src.utils as utils
import src.dbutils as dbutils


files = []

db = dbutils.create_connection()
print("****** DB Connection Created VOL1.******")
dbutils.create_requests_table(db)

print("LEN OF FILES : ", len(files))

for counter in range(len(files)):
    if counter % 10000 == 9999:
        db.close()
        db = dbutils.create_connection()
        print("********************************************* DB Connection Created VOL1.******")
    else:
        db = dbutils.create_connection()


def process_line(line):
    return line

def get_lines(file_name):
    list = []
    with open(file_name) as source_file:
        for row in source_file:
            list.append(json.loads(row))

    return list

def add_to_database(list):
    key = 0
    for file in list:
        if(key % 100 == 99):
            db.commit()
        for row in file:
            if row:
                dbutils.insert_request(db, row)
        key += 1

    db.commit()

def get_files():
    conf = utils.loadConfig()
    json_path = conf["JSON_PATH"]

    print(conf)
    print(json_path)

    # r=root, d=directories, f = files
    for r, d, f in os.walk(json_path):
        for file in f:
            if '.json' in file and "facebook-backup" not in r:
                files.append(os.path.join(r, file))
    return files