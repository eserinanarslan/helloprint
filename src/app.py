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

print(files)
process_pool = pool.Pool(mp.cpu_count())
json_list = process_pool.map(readfiles.get_lines, files)
process_pool.close()

readfiles.add_to_database(json_list)

report_attributes = []

operating_systems = analyze.report_os(db)
report_attributes.append("\n***Most used operating systems***\n")
for row in operating_systems:
        str_row = str(str(row[0])+'  '+str(row[1]))
        report_attributes.append(str_row)
print("\n")

browser = analyze.report_browser(db)
report_attributes.append("\n***Most used browsers***\n")
for row in browser:
        str_row = str(str(row[0])+'  '+str(row[1]))
        report_attributes.append(str_row)
print("\n")

referrers = analyze.report_referrers(db)
report_attributes.append("\n***Top referrers***\n")
for row in referrers:
        str_row = str(str(row[0])+'  '+str(row[1]))
        report_attributes.append(str_row)
print("\n")

paths = analyze.report_paths(db)
report_attributes.append("\n***Most visited paths***\n")
for row in paths:
        str_row = str(str(row[0])+'  '+str(row[1]))
        report_attributes.append(str_row)
print("\n")

visitor_count = analyze.report_visits(db)
report_attributes.append("\n***Visit counts by date for last 30 days***\n")
for row in visitor_count:
        str_row = str(str(row[0])+'  '+str(row[1]))
        report_attributes.append(str_row)
print("\n")

db.close()

print("****** DB Connection Closed.******")

report = open("report/HelloPrintReport.txt","w+")
report.writelines(report_attributes)
report.close()

#for att in report_attributes:
#    report.write(att)
#    print("%s is writen to report !\n\n", att)


print("Report process finished !")
