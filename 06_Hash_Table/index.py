import unittest
from HashTable import HashTable

class UnitTest(unittest.TestCase):

    def testHashTable(self):
        hash = HashTable()

        hash.add("march 6", 130)
        hash.add("march 7", 783)
        hash.add("march 8", 130)
        hash.add("march 17", 63457)

        self.assertEqual(hash.exists("march 8"), True)
        self.assertEqual(hash.get("march 6"), 130)
        self.assertEqual(hash.get("march 17"), 63457)

        hash.add("march 17", 23421)
        self.assertEqual(hash.remove("march 17"), ('march 17', 23421))
        self.assertEqual(hash.exists("march 17"), False)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
