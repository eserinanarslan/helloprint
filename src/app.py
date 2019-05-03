# -*- coding: utf-8 -*-
"""
Created on Tuesday April 30 2019

@author: eser.arslan

"""
import datetime

import src.readfiles as readfiles
import src.dbutils as dbutils
import src.createreport as report
import multiprocessing as mp

from multiprocessing import pool

def app():
    start_time = datetime.datetime.now()

#   Create SQLITE Database
    db = dbutils.create_connection()
    print("****** DB Connection Created.******")
    dbutils.create_requests_table(db)

    table_creation_finish = datetime.datetime.now()
    table_creation_time = table_creation_finish - start_time

#   Read files into different folder
    get_file_start_time = datetime.datetime.now()
    files = readfiles.get_files()
    get_file_finish_time = datetime.datetime.now()
    get_file_time = get_file_finish_time - get_file_start_time

#   Create Multiprocess
    process_pool = pool.Pool(mp.cpu_count())
    get_line_start_time = datetime.datetime.now()

#   Read lines into JSON file
    json_list = process_pool.map(readfiles.get_lines, files)
    get_line_finish_time = datetime.datetime.now()
    get_line_time = get_line_finish_time - get_line_start_time
    process_pool.close()

#   Write messages to DB
    db_insert_start_time = datetime.datetime.now()
    readfiles.add_to_database(json_list)
    db.commit()
    db_insert_finish_time = datetime.datetime.now()
    db_insert_time = db_insert_finish_time - db_insert_start_time

#   Create analyze reports
    analyze_report = report.create_analyze_report(start_time,table_creation_time, get_file_time,get_line_time, db_insert_time)

if __name__ == "__main__":
    app()