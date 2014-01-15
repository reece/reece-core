import marshall
import os
import sqlite3
import zlib

class SQLiteCache(object):
    create_ddl_sql = 'CREATE TABLE cache (key text primary key, created timestamp 

    def __init__(self,db_path):
