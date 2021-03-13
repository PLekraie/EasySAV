from typing import List

from Domain.intervention import Intervention


class Technicien:
    def __init__(self, id, nom, prenom):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.interventions: List[Intervention] = list()