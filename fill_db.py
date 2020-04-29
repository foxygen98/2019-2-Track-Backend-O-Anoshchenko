#!/usr/bin/env python3

import psycopg2
import psycopg2.extras
from datetime import datetime
from db_config import *
import factory

def main():
    conn = psycopg2.connect(f"dbname={DB_NAME} user={DB_USER} host='localhost' password={DB_PASSWORD}")
    cur = conn.cursor
    for i in range(5):
        topic = 'topic'+str(i)
        user = 1
        cur.execute('INSERT INTO chats_chat (id, is_group_chat, topic) VALUES (%s, %s)', (i, false, topic))
    cur.close()
    conn.close()
