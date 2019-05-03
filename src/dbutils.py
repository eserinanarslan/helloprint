# -*- coding: utf-8 -*-
"""
Created on Tuesday April 30 2019

@author: eser.arslan
"""

from sqlite3 import Error
import sqlite3
import httpagentparser
import src.utils as utils

#   Create COnnection
def create_connection():
    """ create a database connection to a SQLite database """
    try:
        # conn = sqlite3.connect(":memory:")
        conn = sqlite3.connect("sqlite/db/sqlite.db", check_same_thread=False)
        return conn
    except Error as e:
        print(e)
    return None

#   Create requests table
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

#   Insert lines to DB from JSON files
def insert_request(db, request):
    conf = utils.loadConfig()
    insert_requests_sql = conf["SQL"]["INSERT_REQUESTS"]
    user_agent = httpagentparser.detect(request['user_agent'])

    if 'id' in request['params']:
        params_id = request['params']['id']
    else:
        params_id = ''

    if 'date-count' in request['params']:
        params_date_count = request['params']['date-count']
    else:
        params_date_count = ''

    if 'date-unit' in request['params']:
        params_date_unit = request['params']['date-unit']
    else:
        params_date_unit = ''

    if 'date-start' in request['params']:
        params_date_start = request['params']['date-start']
    else:
        params_date_start = ''

    if 'date-end' in request['params']:
        params_date_end = request['params']['date-end']
    else:
        params_date_end = ''

    if 'users' in request['params']:
        params_users = request['params']['users']
    else:
        params_users = ''

    if 'resource-group' in request['params']:
        params_resource_group = request['params']['resource-group']
    else:
        params_resource_group = ''

    if 'sort-measure' in request['params']:
        params_sort_measure = request['params']['sort-measure']
    else:
        params_sort_measure = ''

    if 'token' in request['params']:
        params_token = request['params']['token']
    else:
        params_token = ''

    if 'divID' in request['params']:
        params_divID = request['params']['divID']
    else:
        params_divID = ''

    if 'oauth_proxy_redirect_host' in request['params']:
        params_oauth_proxy_redirect_host = request['params']['oauth_proxy_redirect_host']
    else:
        params_oauth_proxy_redirect_host = ''

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
        params_id,
        params_date_count,
        params_date_unit,
        params_date_start,
        params_date_end,
        params_users,
        params_resource_group,
        params_sort_measure,
        params_oauth_proxy_redirect_host,
        params_divID,
        params_token,
        request['path'],
        request['referrer'],
        user_agent_os,
        user_agent_browser,
        user_agent_browser_version
    )

    print(row)

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