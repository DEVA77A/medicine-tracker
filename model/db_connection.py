
import pyodbc

def get_connection():
    return pyodbc.connect(
        'DRIVER={MySQL ODBC 9.4 Unicode Driver};'
        'SERVER=localhost;DATABASE=expiry_tracker;'
        'USER=deva;PASSWORD=12345678;'
    )
