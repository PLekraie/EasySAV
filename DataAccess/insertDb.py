from dbConnect import DbConnect

################################################
# that file should care of database operations #
################################################



class InsertDb:
    def __init__(self):
        self.connexion = DbConnect("EasyDb").getconnection()

    def intervention(self, idClient, libelle, idTech):
        cmd = f"insert into intervention(id_Client, libelle, id_Tech ) " \
              f"values('{idClient}', '{libelle}', '{idTech}')"
        conn = self.connexion
        conn.cursor().execute(cmd)
        conn.commit()
        return
