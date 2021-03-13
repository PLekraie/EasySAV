class Intervention:
    def __init__(self, code, modalite, id_client):
        self.code = code
        self.modalite = modalite
        self.etat = "non attribuée"
        self.duree = 0
        self.id_technicien = None
        self.id_client = id_client