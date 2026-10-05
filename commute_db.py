import streamlit as st
import sqlite3
import pandas as pd

def init_commute_db():
    conn = sqlite3.connect('commuteplanner.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS commuteplanner(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              commute_step INTEGER NOT NULL,
              market_date TEXT NOT NULL,
              time_to_leave TEXT NOT NULL,
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