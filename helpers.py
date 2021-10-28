"""Contains helper methods that are called from various routes in the main application"""
import os
import requests
import urllib.parse

from errors import DatabaseError
from flask import redirect, render_template, request, session
from functools import wraps

from classes import Product

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.
        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def create_inventory(mysql):
    """Queries the database. Builds and returns a list of products."""
    inventory = []
    records = query_database(mysql, f"SELECT product.id, name, price, stock_count FROM catalogue LEFT JOIN product ON catalogue.product_id = product.id ORDER BY product.id;")
    for record in records:
        inventory.append(Product(record))
    return inventory

def get_users_inventory(mysql, user_id):
    """Queries the database. Builds and returns a list of products found in the specified user's catalogue."""
    inventory = []
    records = query_database(mysql, f"SELECT product.id, name, price, stock_count FROM catalogue LEFT JOIN product ON catalogue.product_id = product.id WHERE catalogue.seller_id = {user_id} ORDER BY product.id;")
    for record in records:
        inventory.append(Product(record))
    return inventory

def query_database(mysql, query_string):
    """Opens connection to database, queries, closes connection, returns result of query"""
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(query_string)
        results = cursor.fetchall()
        cursor.close()
        return results
    except:
        raise DatabaseError("ERROR: The database has not been updated")

def update_database(mysql, query_string):
    """Opens connection to database, updates database, closes connection"""
    try:
        cursor = mysql.connection.cursor()
        cursor.execute(query_string)
        mysql.connection.commit()
        cursor.close()
        return
    except:
        raise DatabaseError("ERROR: The database has not been updated")
