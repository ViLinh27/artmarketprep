import streamlit as st
import sqlite3
import pandas as pd

def init_vendorfee_db():
    conn = sqlite3.connect('vendor_fee_tracker.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS vendors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            instagram TEXT,
            fee_status TEXT,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

def get_vendor_fees():
    conn = sqlite3.connect('vendor_fee_tracker.db')
    df = pd.read_sql_query("SELECT * FROM vendors", conn)
    conn.close()
    return df

def add_vendor_fee_info(name, instagram, fee_status, notes):
    conn = sqlite3.connect('vendor_fee_tracker.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO vendors (name, instagram, fee_status, notes)
        VALUES (?, ?, ?, ?)
    ''', (name, instagram, fee_status, notes))
    conn.commit()
    conn.close()