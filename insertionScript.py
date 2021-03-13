import sqlite3

from Domain.intervention import Intervention
from Domain.technicien import Technicien

def insertion_database():
    connexion = sqlite3.connect("EasySAV.db")
    curseur = connexion.cursor()

    # feed Technician table
    lstTech = []

    lstTech.append(Technicien(1, "Thierry", "Armand"))
    lstTech.append(Technicien(2, "Sebastien", "Letech"))
    lstTech.append(Technicien(3, "Lahcene", "Mahidi"))
    lstTech.append(Technicien(4, "Sergent", "Garcia"))
    lstTech.append(Technicien(5, "Pauline", "Lekraie"))
    lstTech.append(Technicien(6, "Capitaine", "Flam"))
    lstTech.append(Technicien(7, "Dragon", "BallZ"))
    lstTech.append(Technicien(8, "Lopes", "Enrique"))
    lstTech.append(Technicien(9, "Rachid", "Berki"))
    lstTech.append(Technicien(10, "Olivier", "Dublé"))

    for tech in lstTech:
        cmd = f"INSERT INTO TECHNICIEN(nom, prenom) VALUES('{tech.nom}', '{tech.prenom}')"
        curseur.execute(cmd)

    # feed Intervention table
    lstInter = []

    lstInter.append(Intervention(1, "", 1))
    lstInter.append(Intervention(2, "", 2))
    lstInter.append(Intervention(3, "", 3))
    lstInter.append(Intervention(4, "", 4))
    lstInter.append(Intervention(5, "", 5))
    lstInter.append(Intervention(6, "", 6))
    lstInter.append(Intervention(7, "", 7))
    lstInter.append(Intervention(8, "", 8))
    lstInter.append(Intervention(9, "", 9))
    lstInter.append(Intervention(10, "", 10))

    for inter in lstInter:
        cmd = f"INSERT INTO INTERVENTION(modalite, etat, duree, id_technicien, id_client) VALUES('{inter.modalite}'," \
              f"'{inter.etat}', '{inter.duree}', '{inter.id_technicien}', '{inter.id_client}')"
        curseur.execute(cmd)
    connexion.commit()