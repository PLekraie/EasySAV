import unittest

from Domain.technicien import Technicien


class MyTestCase(unittest.TestCase):
    def test_creation_technicien(self):
        tech = Technicien(1, "Thierry", "Armand")
        self.assertIsNotNone(tech)


if __name__ == '__main__':
    unittest.main()
