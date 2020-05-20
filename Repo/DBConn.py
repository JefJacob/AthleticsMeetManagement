import pyodbc

class DBConn:
    def __init__(self):
        self.connection=None

    def __enter__(self) -> pyodbc.Connection:
        self.connection=  pyodbc.connect('Driver={SQL Server};'
                        'Server=VAIO;'
                       'Database=AO_TESTDB_V8;'
                       'Trusted_Connection=yes;')
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if(exc_type or exc_tb or exc_val):
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
