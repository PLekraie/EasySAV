import sqlite3

from Domain.intervention import Intervention


class AccessDatabase:
    def __init__(self):
        # Connect to database
        self.connexion = sqlite3.connect("EasySAV.db")
        self.curseur = self.connexion.cursor()

    def select_interventions(self):
        # retrieve interventions from database
        cmd = f"SELECT * FROM INTERVENTION"
        self.curseur.execute(cmd)
        self.connexion.commit()

        return self.curseur.fetchall()

    def insert_intervention(self, intervention):
        # add intervention to database
        # retourne validation ?
        cmd = f"INSERT INTO INTERVENTION(modalite, etat, duree, id_technicien, id_client) VALUES('{intervention.modalite}'," \
              f"'{intervention.etat}', '{intervention.duree}', '{intervention.id_technicien}', '{intervention.id_client}')"
        self.curseur.execute(cmd)
        self.connexion.commit()