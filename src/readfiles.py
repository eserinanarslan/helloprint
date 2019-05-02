# -*- coding: utf-8 -*-
"""
Created on Tuesday April 30 2019

@author: eser.arslan
"""

import os
import json
import src.utils as utils
import src.dbutils as dbutils

from multiprocessing import pool

files = []

db = dbutils.create_connection()
print("****** DB Connection Created.******")
dbutils.create_requests_table(db)

def process_line(line):
    return line

def get_lines(file_name):

    conf = utils.loadConfig()
    pool_size = conf["THREAD_POOL_SIZE"]
    thread_pool_size = int(pool_size)

    thread_pool = pool.ThreadPool(thread_pool_size)
    with open(file_name) as source_file:
        # chunk the work into batches of 4 lines at a time
        results = thread_pool.map(process_line, source_file, 4)

        for row in results:
            dbutils.insert_request(db, json.loads(row))

        print(results)
    thread_pool.close()

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


