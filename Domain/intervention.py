from DataAccess.dbOp import DbOp




class Intervention:
    def __init__(self):
        self.libelle = ""
        self.id_Client = 0

    def createFromJson(self, json):
        if "libelle" in json:
            self.libelle = json["libelle"]

        if "id_Client" in json:
            self.id_Client = json["id_Client"]

    def putInDb(self):
        cmd = """INSERT INTO Intervention(libelle, id_Client) VALUES (?, ?)"""
        datas = (self.libelle, self.id_Client)
        try:
            dbObj = DbOp()
            dbObj.insert_into_db(cmd, datas)
            dbObj.commit()
            dbObj.close()
            return "ok"

        except Exception as exc:
            return f"Error in access db: {exc}"

    def createFromRecord(self, libelle, id_Client):
            self.libelle = libelle
            self.id_Client = id_Client

    def interInDico(self):
        dico = {
            'libelle': "'" + self.libelle + "'",
            'id_Client': "'" + self.id_Client + "'",
        }
        return dico

    def getAll(self):
        dbobj = DbOp()
        records = dbobj.getAllIntervention()
        interventions = []
        for row in records:
            my_inter = Intervention()
            my_inter.createFromRecord(row[1], row[5])
            interventions.append(my_inter)
        return interventions