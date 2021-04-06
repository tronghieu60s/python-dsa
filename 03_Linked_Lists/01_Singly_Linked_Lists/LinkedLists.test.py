import unittest
from LinkedLists import LinkedLists


class UnitTest(unittest.TestCase):

    def testToString(self):
        newList = LinkedLists()

        # add item
        newList.push_front("item 1")
        newList.push_front("item 2")
        newList.push_front("item 3")

        expected = "item 3 --> item 2 --> item 1 --> null"
        self.assertEqual(newList.to_string(), expected)

    def testSize(self):
        newList = LinkedLists()
        self.assertEqual(newList.size(), 0)

        # add item
        newList.push_front("item 1")
        newList.push_front("item 2")
        newList.push_front("item 3")

        self.assertEqual(newList.size(), 3)

    def testEmpty(self):
        newList = LinkedLists()
        self.assertEqual(newList.empty(), True)

        # add item
        newList.push_front("item 1")
        newList.push_front("item 2")
        newList.push_front("item 3")

        self.assertEqual(newList.empty(), False)

    def testValueAt(self):
        newList = LinkedLists()
        self.assertEqual(newList.value_at(0), None)

        # add item
        newList.push_front("item 1")
        newList.push_front("item 2")
        newList.push_front("item 3")

        self.assertEqual(newList.value_at(1), "item 2")

    def testPushFront(self):
        # previous test also test push front
        pass

    def testPopFront(self):
        newList = LinkedLists()
        with self.assertRaises(OverflowError):
            newList.pop_front()

        # add item
        newList.push_front("item 1")
        newList.push_front("item 2")
        newList.push_front("item 3")

        self.assertEqual(newList.pop_front(), "item 3")
        self.assertEqual(newList.value_at(1), "item 1")

    def testPushBack(self):
        newList = LinkedLists()

        # add item
        newList.push_back("item 1")
        newList.push_back("item 2")
        newList.push_back("item 3")

        self.assertEqual(newList.value_at(0), "item 1")
        self.assertEqual(newList.value_at(2), "item 3")

    def testPopBack(self):
        newList = LinkedLists()
        with self.assertRaises(OverflowError):
            newList.pop_front()

        # add item
        newList.push_back("item 1")
        newList.push_back("item 2")
        newList.push_back("item 3")

        self.assertEqual(newList.pop_back(), "item 3")
        self.assertEqual(newList.value_at(2), None)

    def testFront(self):
        newList = LinkedLists()
        with self.assertRaises(OverflowError):
            newList.front()

        # add item
        newList.push_back("item 1")

        self.assertEqual(newList.front(), "item 1")

    def testBack(self):
        newList = LinkedLists()
        with self.assertRaises(OverflowError):
            newList.back()

        # add item
        newList.push_back("item 1")

        self.assertEqual(newList.back(), "item 1")

    def testInsert(self):
        newList = LinkedLists()

        # add item
        newList.push_back("item 1")
        newList.push_back("item 2")
        newList.push_back("item 3")

        newList.insert(1, "item 4")

        self.assertEqual(newList.value_at(1), "item 4")
        self.assertEqual(newList.value_at(2), "item 2")

    def testErase(self):
        newList = LinkedLists()
        with self.assertRaises(OverflowError):
            newList.erase(0)

        # add item
        newList.push_back("item 1")
        newList.push_back("item 2")
        newList.push_back("item 3")

        newList.erase(0)

        self.assertEqual(newList.value_at(0), "item 2")

    def testRemoveValue(self):
        newList = LinkedLists()

        # add item
        newList.push_back("item 1")
        newList.push_back("item 2")
        newList.push_back("item 3")

        newList.remove_value("item 1")

        self.assertEqual(newList.value_at(0), "item 2")

    def testValueNFromEnd(self):
        newList = LinkedLists()

        # add item
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
        # after reverse: item 3 --> item 2 --> item 1 --> null

        expected = "item 3 --> item 2 --> item 1 --> null"
        self.assertEqual(newList.to_string(), expected)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
