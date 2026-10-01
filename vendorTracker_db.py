import streamlit as st
import sqlite3
import pandas as pd

def init_db():
    conn = sqlite3.connect('vendor_tracker.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS vendors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            instagram TEXT,
            status TEXT,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_vendor(name, instagram, status, notes):
    conn = sqlite3.connect('vendor_tracker.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO vendors (name, instagram, status, notes)
        VALUES (?, ?, ?, ?)
    ''', (name, instagram, status, notes))
    conn.commit()
    conn.close()

def get_vendors():
    conn = sqlite3.connect('vendor_tracker.db')
    df = pd.read_sql_query("SELECT * FROM vendors", conn)
    conn.close()
    return df

def delete_vendor(vendor_id):
    conn = sqlite3.connect('vendor_tracker.db')
    c = conn.cursor()
    c.execute('DELETE FROM vendors WHERE id = ?', (vendor_id,))
    conn.commit()
    conn.close()

def update_vendor_status(vendor_name, new_status):
    conn = sqlite3.connect('vendor_tracker.db')
    c = conn.cursor()
    c.execute('UPDATE vendors SET status = ? WHERE name = ?', (new_status, vendor_name))
    conn.commit()
    conn.close()

def search_vendor_name(vendor_name):
    conn = sqlite3.connect('vendor_tracker.db')
    df = pd.read_sql_query("SELECT * FROM vendors WHERE name LIKE ?", conn, params=('%' + vendor_name + '%',))
    conn.close()
    return df

def delete_all_vendors():
    conn = sqlite3.connect('vendor_tracker.db')
    c = conn.cursor()
    c.execute('DELETE FROM vendors')
    conn.commit()
    conn.close()
