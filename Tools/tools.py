class Tools :
    @staticmethod
    def formatInterventions(list):
        interventions = []
        for elt in list:
            dico = {}
            dico["libelle"] = elt.libelle
            dico["id_Client"] = elt.id_Client
            interventions.append(dico)
        return interventions