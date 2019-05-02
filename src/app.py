# -*- coding: utf-8 -*-
"""
Created on Tuesday April 30 2019

@author: eser.arslan
"""

import src.readfiles as readfiles
import src.dbutils as dbutils
import src.analyze as analyze
import  multiprocessing as mp


from multiprocessing import pool

db = dbutils.create_connection()
print("****** DB Connection Created.******")
dbutils.create_requests_table(db)

files = readfiles.get_files()

process_pool = pool.Pool(mp.cpu_count())
result = process_pool.map(readfiles.get_lines, files)
process_pool.close()

print(len(files))

db.commit()

analyze.report_os(db)
analyze.report_browser(db)
analyze.report_referrers(db)
analyze.report_paths(db)
analyze.report_visits(db)

db.close()
print("****** DB Connection Closed.******")

