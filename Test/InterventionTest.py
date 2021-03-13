import unittest
from Domain.intervention import Intervention
from DataAccess.accessDatabase import AccessDatabase


class InterventionTest(unittest.TestCase):
    def test_creation_intervention(self):
        inter = Intervention("15SDk", "", 150)
        self.assertIsNotNone(inter)


if __name__ == '__main__':
    unittest.main()
