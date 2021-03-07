from Domain.technicien import Technicien
from Domain.client import Client
from dbInit import DbInit

mydb = DbInit("EasyDb")
conn = mydb.connect()
curseur = conn.cursor()

# makes tables in database
sqlCreateTechTable = f"CREATE TABLE Technicien( id BIGINT," \
                 f"                             nom VARCHAR(15), " \
                 f"                             prenom VARCHAR(15), " \
                 f"                             PRIMARY KEY(id))"

sqlCreateClientTable = f"CREATE TABLE Client( id_Client BIGINT, " \
                       f"                     nom VARCHAR(15), " \
                       f"                     adresse VARCHAR(50), " \
                       f"                     PRIMARY KEY(Id_Client))"

sqlCreateInterventionTable = f"CREATE TABLE Intervention(Id_Intervention BIGINT," \
                             f"                          libelle VARCHAR(50)," \
                             f"                          actif BOOLEAN," \
                             f"                          debut DATETIME," \
                             f"                          fin DATETIME," \
                             f"                          id_Client BIGINT NOT NULL," \
                             f"                          id BIGINT NOT NULL," \
                             f"                          PRIMARY KEY(id_Intervention)," \
                             f"                          FOREIGN KEY(id_Client) REFERENCES Client(Id_Client)," \
                             f"                          FOREIGN KEY(id) REFERENCES Technicien(id))"

curseur.execute(sqlCreateTechTable)
curseur.execute(sqlCreateClientTable)
curseur.execute(sqlCreateInterventionTable)
conn.commit()

# feed Technician table
list = []

list.append(Technicien("Thierry", "Armand"))
list.append(Technicien("Sebastien", "Letech"))
list.append(Technicien("Lahcene", "Mahidi"))
list.append(Technicien("Sergent", "Garcia"))
list.append(Technicien("Pauline", "Lekraie"))
list.append(Technicien("Capitaine", "Flam"))
list.append(Technicien("Dragon", "BallZ"))
list.append(Technicien("Lopes", "Enrique"))
list.append(Technicien("Rachid", "Berki"))
list.append(Technicien("Olivier", "Dublé"))

for tech in list:
    cmd = f"INSERT INTO Technicien(nom, prenom) VALUES('{tech.nom}', '{tech.prenom}')"
    curseur.execute(cmd)

conn.commit()

# feed Client table
list.clear()
list.append(Client("Duchateau", "13 rue de la Cordillère, Dijon"))
list.append(Client("Duvalon", "56 rue du Chateau, Lille"))
list.append(Client("Totoro", "La Plaine Saint Denis, Saint-Denis"))
list.append(Client("Mahidi", "61 rue du docteur schweitzer, Tourcoing"))
list.append(Client("Duchateau", "27 rue du chemin, Routes"))

for client in list:
    cmd = f"INSERT INTO Client(nom, adresse) VALUES('{client.nom}', '{client.addr}')"
    curseur.execute(cmd)

conn.commit()








