# -*- coding: utf-8 -*-
"""
Created on Tuesday April 30 2019

@author: eser.arslan
"""

import src.utils as utils
############### ANALYZE OS #####################

def analyze_os(db):
    conf = utils.loadConfig()
    analyze_os_sql = conf["SQL"]["ANALYZE_OS"]
    cur = db.cursor()
    cur.execute(analyze_os_sql)
    return cur.fetchall()

################ REPORT OS ####################

def report_os(db):
    data = analyze_os(db)
    print('Most used operating systems')
    for row in data:
        print(row[0], '  ', row[1])

################ ANALYZE BROWSER ####################

def analyze_browser(db):
    conf = utils.loadConfig()
    analyze_browser_sql = conf["SQL"]["ANALYZE_BROWSER"]
    cur = db.cursor()
    cur.execute(analyze_browser_sql)
    return cur.fetchall()

################ REPORT BROWSER ####################

def report_browser(db):
    data = analyze_browser(db)
    print('Most used browsers')
    for row in data:
        print(row[0], '  ', row[1])

################ ANALYZE PATHS ####################

def analyze_paths(db):
    conf = utils.loadConfig()
    analyze_paths_sql = conf["SQL"]["ANALYZE_PATHS"]
    cur = db.cursor()
    cur.execute(analyze_paths_sql)
    return cur.fetchall()

################ REPORT PATHS ####################

def report_paths(db):
    data = analyze_paths(db)
    print('Most visited paths')
    for row in data:
        print(row[0], '  ', row[1])

################ ANALYZE REFERRES ####################

def analyze_referrers(db):
    conf = utils.loadConfig()
    analyze_referrers_sql = conf["SQL"]["ANALYZE_REFERRERS"]
    cur = db.cursor()
    cur.execute(analyze_referrers_sql)
    return cur.fetchall()

################ REPORT REFERRES ####################

def report_referrers(db):
    data = analyze_referrers(db)
    print('Top referrers')
    for row in data:
        print(row[0], '  ', row[1])

################ ANALYZE VISITS ####################

def analyze_visits(db):
    conf = utils.loadConfig()
    analyze_visits_sql = conf["SQL"]["ANALYZE_VISITS"]
    cur = db.cursor()
    cur.execute(analyze_visits_sql)
    return cur.fetchall()

################ REPORT VISITS ####################

def report_visits(db):
    data = analyze_visits(db)
    print('Visit counts by date for last 30 days')
    for row in data:
        print(row[1], '  ', row[0])