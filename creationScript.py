import sqlite3


def create_database():
    connexion = sqlite3.connect("EasySAV.db")
    curseur = connexion.cursor()

    sqlCreateTechTable = f"CREATE TABLE IF NOT EXISTS TECHNICIEN(" \
                         f"id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE," \
                         f"nom TEXT," \
                         f"prenom TEXT)"

    sqlCreateInterTable = f"CREATE TABLE IF NOT EXISTS INTERVENTION(" \
                          f"code INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE," \
                          f"modalite TEXT," \
                          f"etat VARCHAR," \
                          f"duree FLOAT," \
                          f"id_technicien INTEGER," \
                          f"id_client INTEGER," \
                          f"FOREIGN KEY(id_technicien) REFERENCES TECHNICIEN(id))"

    curseur.execute(sqlCreateTechTable)
    curseur.execute(sqlCreateInterTable)
    connexion.commit()
