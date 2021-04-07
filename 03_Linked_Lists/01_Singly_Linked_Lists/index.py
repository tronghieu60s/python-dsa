import unittest
from LinkedLists import LinkedLists
# from LinkedListsTail import LinkedListsTail as LinkedLists

class UnitTest(unittest.TestCase):

    def testToString(self):
        newList = LinkedLists()

        newList.push_front("item 1")
        newList.push_front("item 2")
        newList.push_front("item 3")

        expected = "item 3 --> item 2 --> item 1 --> null"
        self.assertEqual(newList.to_string(), expected)

    def testSize(self):
        newList = LinkedLists()
        self.assertEqual(newList.size(), 0)

        newList.push_front("item 1")
        self.assertEqual(newList.size(), 1)

    def testEmpty(self):
        newList = LinkedLists()
        self.assertEqual(newList.empty(), True)

        newList.push_front("item 3")
        self.assertEqual(newList.empty(), False)

    def testValueAt(self):
        newList = LinkedLists()
        self.assertEqual(newList.value_at(0), None)

        newList.push_front("item 1")
        self.assertEqual(newList.value_at(0), "item 1")

    def testPushFront(self):
        """
        previous test also test push front
        excample: self.testToString()
        """
        pass

    def testPopFront(self):
        newList = LinkedLists()
        with self.assertRaises(OverflowError):
            newList.pop_front()

        newList.push_front("item 1")
        newList.push_front("item 2")
        newList.push_front("item 3")

        self.assertEqual(newList.pop_front(), "item 3")

        expected = "item 2 --> item 1 --> null"
        self.assertEqual(newList.to_string(), expected)

    def testPushBack(self):
        newList = LinkedLists()

        newList.push_back("item 1")
        newList.push_back("item 2")
        newList.push_back("item 3")

        self.assertEqual(newList.value_at(0), "item 1")
        
        expected = "item 1 --> item 2 --> item 3 --> null"
        self.assertEqual(newList.to_string(), expected)

    def testPopBack(self):
        newList = LinkedLists()
        with self.assertRaises(OverflowError):
            newList.pop_front()

        newList.push_back("item 1")
        newList.push_back("item 2")
        newList.push_back("item 3")

        self.assertEqual(newList.pop_back(), "item 3")

        expected = "item 1 --> item 2 --> null"
        self.assertEqual(newList.to_string(), expected)

    def testFront(self):
        newList = LinkedLists()
        with self.assertRaises(OverflowError):
            newList.front()

        newList.push_back("item 1")
        self.assertEqual(newList.front(), "item 1")

    def testBack(self):
        newList = LinkedLists()
        with self.assertRaises(OverflowError):
            newList.back()

        newList.push_back("item 1")
        self.assertEqual(newList.back(), "item 1")

    def testInsert(self):
        newList = LinkedLists()

        newList.push_back("item 1")
        newList.push_back("item 2")
        newList.push_back("item 3")

        newList.insert(1, "item 4")
        self.assertEqual(newList.value_at(1), "item 4")

        expected = "item 1 --> item 4 --> item 2 --> item 3 --> null"
        self.assertEqual(newList.to_string(), expected)

    def testErase(self):
        newList = LinkedLists()
        with self.assertRaises(OverflowError):
            newList.erase(0)

        newList.push_back("item 1")
        newList.push_back("item 2")
        newList.push_back("item 3")

        newList.erase(0)
        self.assertEqual(newList.value_at(0), "item 2")

        newList.erase(1)
        expected = "item 2 --> null"
        self.assertEqual(newList.to_string(), expected)
    
    def testValueNFromEnd(self):
        newList = LinkedLists()

        newList.push_back("item 1")
        newList.push_back("item 2")
        newList.push_back("item 3")

        self.assertEqual(newList.value_n_from_end(1), "item 3")
        self.assertEqual(newList.value_n_from_end(3), "item 1")

    def testReverse(self):
        newList = LinkedLists()

        # add item
        newList.push_back("item 1")
        newList.push_back("item 2")
        newList.push_back("item 3")

        # current: item 1 --> item 2 --> item 3 ---> null
        newList.reverse()
        newList.push_back("item 4")
        # after reverse: item 3 --> item 2 --> item 1 --> null

        expected = "item 3 --> item 2 --> item 1 --> item 4 --> null"
        self.assertEqual(newList.to_string(), expected)

    def testRemoveValue(self):
        newList = LinkedLists()

        newList.push_back("item 1")
        newList.push_back("item 2")
        newList.push_back("item 3")

        newList.remove_value("item 1")
        self.assertEqual(newList.value_at(0), "item 2")

        expected = "item 2 --> item 3 --> null"
        self.assertEqual(newList.to_string(), expected)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
