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

report_attributes = []
operating_systems = analyze.report_os(db)
report_attributes.append(operating_systems)
print("\n")
browser = analyze.report_browser(db)
report_attributes.append(browser)
print("\n")
referrers = analyze.report_referrers(db)
report_attributes.append(referrers)
print("\n")
paths = analyze.report_paths(db)
report_attributes.append(paths)
print("\n")
visitor_count = analyze.report_visits(db)
report_attributes.append(visitor_count)
print("\n")



db.close()
print("****** DB Connection Closed.******")

report = open("report/HelloPrintReport.txt","w+")

for att in report_attributes:
    report.write(att)
    print("%s is writen to report !", att)

print("Report process finished !")
