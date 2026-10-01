import streamlit as st
import sqlite3
import pandas as pd

def init_marketsapplied_db():
    conn = sqlite3.connect('marketsapplied.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS marketsapplied (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            market_name TEXT NOT NULL,
            market_theme TEXT NOT NULL,
            market_host TEXT NOT NULL,
            market_location TEXT NOT NULL,
            application_date TEXT NOT NULL,
            status TEXT NOT NULL,
            market_vendor_fee REAL NOT NULL,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_market_application(market_name, market_theme, market_host, market_location, application_date, status, market_vendor_fee, notes):
    conn = sqlite3.connect('marketsapplied.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO marketsapplied (market_name, market_theme, market_host, market_location, application_date, status, market_vendor_fee, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (market_name, market_theme, market_host, market_location, application_date, status, market_vendor_fee, notes))
    conn.commit()
    conn.close()

def get_market_applications():
    conn = sqlite3.connect('marketsapplied.db')
    df = pd.read_sql_query("SELECT * FROM marketsapplied", conn)
    conn.close()
    return df

def delete_market_application(application_id):
    conn = sqlite3.connect('marketsapplied.db')
    c = conn.cursor()
    c.execute('DELETE FROM marketsapplied WHERE id = ?', (application_id,))
    conn.commit()
    conn.close()

def update_market_application_status(application_id, new_status):
    conn = sqlite3.connect('marketsapplied.db')
    c = conn.cursor()
    c.execute('UPDATE marketsapplied SET status = ? WHERE id = ?', (new_status, application_id))
    conn.commit()
    conn.close()

def search_market_name(market_name):
    conn = sqlite3.connect('marketsapplied.db')
    df = pd.read_sql_query("SELECT * FROM marketsapplied WHERE market_name LIKE ?", conn, params=('%' + market_name + '%',))
    conn.close()
    return df

def delete_all_market_applications():
    conn = sqlite3.connect('marketsapplied.db')
    c = conn.cursor()
    c.execute('DELETE FROM marketsapplied')
    conn.commit()
    conn.close()
