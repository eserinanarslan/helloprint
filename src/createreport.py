# -*- coding: utf-8 -*-
"""
Created on Thursday May 02 2019

@author: eser.arslan

"""
import datetime

import src.dbutils as dbutils
import src.analyze as analyze

#   Create Connection and main table
db = dbutils.create_connection()
print("****** DB Connection Created For Reporting.******")
dbutils.create_requests_table(db)

def append_report(report_attributes, file_name):
    for row in file_name:
        str_row = str(str(row[0]) + '  ' + str(row[1]) + '\n')
        report_attributes.append(str_row)

def create_analyze_report(start_time,table_creation_time, get_file_time,get_line_time, db_insert_time):
    report_attributes = []

#   Preparing report parametres
    operating_systems = analyze.report_os(db)
    report_attributes.append("\n\n***Most used operating systems***\n")
    append_report(report_attributes, operating_systems)
    print("\n")

    browser = analyze.report_browser(db)
    report_attributes.append("\n\n***Most used browsers***\n")
    append_report(report_attributes, browser)
    print("\n")

    referrers = analyze.report_referrers(db)
    report_attributes.append("\n\n***Top referrers***\n")
    append_report(report_attributes, referrers)
    print("\n")

    paths = analyze.report_paths(db)
    report_attributes.append("\n\n***Most visited paths***\n")
    append_report(report_attributes, paths)
    print("\n")

    visitor_count = analyze.report_visits(db)
    report_attributes.append("\n\n***Visit counts by date for last 30 days***\n")
    append_report(report_attributes, visitor_count)
    print("\n")

    db.close()

    print("****** DB Connection Closed.******")

    str_1 = ("\n\nTable creation time           = " + str(table_creation_time) + "\n")
    report_attributes.append(str_1)
    str_2 = ("\n\nCollecting files time         = " + str(get_file_time) + "\n")
    report_attributes.append(str_2)
    str_3 = ("\n\nReading JSON messages time    = " + str(get_line_time) + "\n")
    report_attributes.append(str_3)
    str_4 = ("\n\nSQLITE insertion time         = " + str(db_insert_time) + "\n")
    report_attributes.append(str_4)

    finish_time = datetime.datetime.now()
    process_time = finish_time - start_time

    str_5 = ("\n\nEnd to End process time        = " + str(process_time) + "\n")
    report_attributes.append(str_5)

    report = open("report/HelloPrintReport.txt", "w+")
    report.writelines(report_attributes)
    report.close()

    print("Report process finished !")