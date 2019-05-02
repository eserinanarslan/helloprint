# -*- coding: utf-8 -*-
"""
Created on Tuesday April 30 2019

@author: eser.arslan
"""

import src.readfiles as readfiles
import src.dbutils as dbutils
import src.analyze as analyze
import multiprocessing as mp

from multiprocessing import pool

db = dbutils.create_connection()
print("****** DB Connection Created.******")
dbutils.create_requests_table(db)

files = readfiles.get_files()

print("LEN OF FILES-1 : ", len(files))

# results = files

# result = readfiles.get_lines(results)
print(files)
process_pool = pool.Pool(mp.cpu_count())
json_list = process_pool.map(readfiles.get_lines, files)
process_pool.close()

readfiles.add_to_database(json_list)

analyze.report_os(db)
print("\n")
analyze.report_browser(db)
print("\n")
analyze.report_referrers(db)
print("\n")
analyze.report_paths(db)
print("\n")
analyze.report_visits(db)
print("\n")

db.close()
print("****** DB Connection Closed.******")

