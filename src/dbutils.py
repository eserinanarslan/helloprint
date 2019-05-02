# -*- coding: utf-8 -*-
"""
Created on Tuesday April 30 2019

@author: eser.arslan
"""

from sqlite3 import Error
import sqlite3
import httpagentparser
import src.utils as utils

def create_connection():
    """ create a database connection to a SQLite database """
    try:
        # conn = sqlite3.connect(":memory:")
        conn = sqlite3.connect("sqlite/db/sqlite.db", check_same_thread=False)
        return conn
    except Error as e:
        print(e)

    return None
def create_requests_table(db):
    conf = utils.loadConfig()
    drop_requests_table_sql = conf["SQL"]["DROP_REQUESTS_TABLE"]

    try:
        c = db.cursor()
        c.execute(drop_requests_table_sql)
    except Error as e:
        print(e)

    create_requests_table_sql = conf["SQL"]["CREATE_REQUESTS_TABLE"]

    try:
        c = db.cursor()
        c.execute(create_requests_table_sql)
    except Error as e:
        print(e)

def insert_request(db, request):
    conf = utils.loadConfig()
    insert_requests_sql = conf["SQL"]["INSERT_REQUESTS"]
    user_agent = httpagentparser.detect(request['user_agent'])

    if 'id' in request['params']:
        id = request['params']['id']
    else:
        id = ''

    if 'oauth_proxy_redirect_host' in request['params']:
        oauth_proxy_redirect_host = request['params']['oauth_proxy_redirect_host']
    else:
        oauth_proxy_redirect_host = ''

    if 'os' in user_agent:
        user_agent_os = user_agent['os']['name']
    else:
        user_agent_os = ''

    if 'email' in request:
        email = request['email']
    else:
        email = 'no-email'

    if 'browser' in user_agent:
        user_agent_browser = user_agent['browser']['name']
        user_agent_browser_version = user_agent['browser']['version']
    else:
        user_agent_browser = ''
        user_agent_browser_version = ''

    row = (
        request['user_name'],
        email,
        request['request_id'],
        request['environment'],
        request['store'],
        request['time'],
        request['client_ip'],
        request['host'],
        request['method'],
        request['params']['module'],
        request['params']['controller'],
        request['params']['action'],
        id,
        oauth_proxy_redirect_host,
        request['path'],
        request['referrer'],
        user_agent_os,
        user_agent_browser,
        user_agent_browser_version
    )

    try:
        cur = db.cursor()
        cur.execute(insert_requests_sql, row)
    except Exception as err:
        print('INSERT_REQUESTS_SQL failed: %s\nError : %s ' % (insert_requests_sql, str(err)))

        pass

    if cur:
        return cur.lastrowid
    else:
        return False