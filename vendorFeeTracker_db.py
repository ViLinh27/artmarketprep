import streamlit as st
import sqlite3
import pandas as pd
from sqlalchemy import text

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