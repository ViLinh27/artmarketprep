import streamlit as st
import sqlite3
import pandas as pd

def init_itinerary_db():
    conn = sqlite3.connect('itinerary.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS itinerary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_date TEXT NOT NULL,
            event_time TEXT NOT NULL,
            event_name TEXT NOT NULL,
            event_location TEXT NOT NULL,
            event_description TEXT NOT NULL,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_event(event_date, event_time, event_name, event_location, event_description, notes):
    conn = sqlite3.connect('itinerary.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO itinerary (event_date, event_time, event_name, event_location, event_description, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (event_date, event_time, event_name, event_location, event_description, notes))
    conn.commit()
    conn.close()

def get_itinerary():
    conn = sqlite3.connect('itinerary.db')
    df = pd.read_sql_query("SELECT * FROM itinerary", conn)
    conn.close()
    return df

def delete_event(event_name):
    conn = sqlite3.connect('itinerary.db')
    c = conn.cursor()
    c.execute('DELETE FROM itinerary WHERE event_name = ?', (event_name,))
    conn.commit()
    conn.close()

def update_event_time(event_name, new_time):
    conn = sqlite3.connect('itinerary.db')
    c = conn.cursor()
    c.execute('UPDATE itinerary SET event_time = ? WHERE event_name = ?', (new_time, event_name))
    conn.commit()
    conn.close()

def search_event_name(event_name):
    conn = sqlite3.connect('itinerary.db')
    df = pd.read_sql_query("SELECT * FROM itinerary WHERE event_name LIKE ?", conn, params=('%' + event_name + '%',))
    conn.close()
    return df

def delete_all_events():
    conn = sqlite3.connect('itinerary.db')
    c = conn.cursor()
    c.execute('DELETE FROM itinerary')
    conn.commit()
    conn.close()
