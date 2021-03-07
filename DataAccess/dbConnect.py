import sqlite3


# Initialise connection
class DbConnect:
    def __init__(self, dbname):
        self.dbName = dbname
        self.idConnect = ""

    def getconnection(self):
        try:
            self.idConnect = sqlite3.connect(self.dbName)
            return self.idConnect
        except Exception as exc:
            print(exc)
