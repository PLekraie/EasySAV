import unittest

from Domain.intervention import Intervention
from Tools.tools import Tools


class MyTestCase(unittest.TestCase):
    def test_formatIntervention(self):
        list = []
        inter = Intervention()
        inter.libelle = "test"
        inter.id_Client = 36
        list.append(inter)

        interventions = Tools.formatInterventions(list)

        self.assertEqual("test", interventions[0]["libelle"])
        self.assertEqual(36, interventions[0]["id_Client"])


if __name__ == '__main__':
    unittest.main()
