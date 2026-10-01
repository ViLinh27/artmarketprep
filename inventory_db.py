import streamlit as st
import sqlite3
import pandas as pd

def init_inventory_db():
    conn = sqlite3.connect('main_inventory.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_inventory_item(item_name,stock_quantity,price,notes):
    conn = sqlite3.connect('main_inventory.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO inventory (item_name, quantity, price, notes)
        VALUES (?, ?, ?, ?)
    ''', (item_name, stock_quantity, price, notes))
    conn.commit()
    conn.close()

def get_inventory_items():
    conn = sqlite3.connect('main_inventory.db')
    df = pd.read_sql_query("SELECT * FROM inventory", conn)
    conn.close()
    return df

def delete_inventory_item(item_id):
    conn = sqlite3.connect('main_inventory.db')
    c = conn.cursor()
    c.execute('DELETE FROM inventory WHERE id = ?', (item_id,))
    conn.commit()
    conn.close()

def update_inventory_stock(item_name, new_quantity):
    conn = sqlite3.connect('main_inventory.db')
    c = conn.cursor()
    c.execute('UPDATE inventory SET quantity = ? WHERE item_name = ?', (new_quantity, item_name))
    conn.commit()
    conn.close()

def search_item_name(item_name):
    conn = sqlite3.connect('main_inventory.db')
    df = pd.read_sql_query("SELECT * FROM inventory WHERE item_name LIKE ?", conn, params=('%' + item_name + '%',))
    conn.close()
    return df

def delete_all_inventory_items():
    conn = sqlite3.connect('main_inventory.db')
    c = conn.cursor()
    c.execute('DELETE FROM inventory')
    conn.commit()
    conn.close()