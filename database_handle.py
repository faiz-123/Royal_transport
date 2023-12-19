import mysql.connector
from tkinter import messagebox
from mysql.connector.locales.eng import client_error
from mysql.connector.plugins import caching_sha2_password
from mysql.connector.plugins import mysql_native_password

# def get_db(database_name):
# password="Python@123",
db = mysql.connector.connect(
     host="localhost",
     user="root",
    password="Python@123",
     database='royal_transport')

def execute_query(query):
    try:
        cursor = db.cursor()
        cursor.execute(query)
        db.commit()
        return True
    except mysql.connector.Error as err:
        # Handle the exception and show an error message
        messagebox.showerror("Error", f"Error occurred: {err}")
        return False



def fetch_data(table_name):
    try:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        cursor.close()
        return data
    except mysql.connector.Error as err:
        # Handle the exception and show an error message
        messagebox.showerror("Error", f"Error occurred: {err}")
        return False

def fetch_colum_data(query):
    try:
        cursor = db.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        return data
    except mysql.connector.Error as err:
        # Handle the exception and show an error message
        messagebox.showerror("Error", f"Error occurred: {err}")
        return False


