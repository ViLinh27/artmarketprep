import streamlit as st
import datetime
import sqlite3
import pandas as pd

#adapts time object to string
def adapt_time(t):
    return t.isoformat()
#converts string back to time
def convert_time(s):
    return datetime.time.fromisoformat(s.decode('utf-8'))

sqlite3.register_adapter(datetime.time, adapt_time)
sqlite3.register_converter("TIME", convert_time)

#opens connection with type detection enabled
conn = sqlite3.connect(":memory:", detect_types=sqlite3.PARSE_DECLTYPES)
# PARSE_DECLTYPES forces sqlite3 to look at delclared column TIME
cursor = conn.cursor()

def init_commute_db():
    conn = sqlite3.connect('commuteplanner.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS commuteplanner(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              commute_step INTEGER NOT NULL,
              market_date TEXT NOT NULL,
              time_to_leave TIMESTAMP NOT NULL,
              eta TEXT NOT NULL,
              traffic TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_commute_step(commute_step, market_date,time_to_leave,eta, traffic):
    conn = sqlite3.connect('commuteplanner.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO commuteplanner (commute_step, market_date,time_to_leave,eta, traffic)
        VALUES (?, ?, ?, ?, ?)
    ''', (commute_step, market_date,time_to_leave,eta, traffic))
    conn.commit()
    conn.close()

def get_commute_plan():
    conn = sqlite3.connect('commuteplanner.db')
    df = pd.read_sql_query("SELECT * FROM commuteplanner", conn)
    conn.close()
    return df

def delete_commute_step(commute_step):
    conn = sqlite3.connect('commuteplanner.db')
    c = conn.cursor()
    c.execute('DELETE FROM commuteplanner WHERE commute_step = ?', (commute_step,))
    conn.commit()
    conn.close()

def update_commute_step(commute_step,new_time_to_leave):
    conn = sqlite3.connect('commuteplanner.db')
    c = conn.cursor()
    c.execute('UPDATE commuteplanner time_to_leave = ? WHERE commute_step = ?', (commute_step, new_time_to_leave))
    conn.commit()
    conn.close()

def delete_all_commute_plan():
    conn = sqlite3.connect('commuteplanner.db')
    c = conn.cursor()
    c.execute('DELETE from commmuteplanner')
    conn.commit()
    conn.close()