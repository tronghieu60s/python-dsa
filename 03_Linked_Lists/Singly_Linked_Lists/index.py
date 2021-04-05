import unittest
from LinkedLists import LinkedLists, ListsEmptyException


class UnitTest(unittest.TestCase):

    def testLength(self):
        newList = LinkedLists()
        self.assertEqual(newList.length(), 0)

        # add item and retest
        newList.addLast("add more item")
        self.assertEqual(newList.length(), 1)  # linked lists had a item

    def testIsEmpty(self):
        newList = LinkedLists()

        self.assertEqual(newList.isEmpty(), True)

        # add item and retest
        newList.addLast("add more item")
        self.assertEqual(newList.isEmpty(), False)  # linked lists had a item

    def testIndexOf(self):
        newList = LinkedLists()

        # add item and test
        newList.addLast("item test")
        self.assertEqual(newList.indexOf("item test"), 0)

    def testAddLast(self):
        newList = LinkedLists()

        # add item
        newList.addLast("item 1")
        newList.addLast("item 2")
        newList.addLast("item 3")

        # find item index => test
        self.assertEqual(newList.indexOf("item 2"), 1)
        self.assertEqual(newList.length(), 3)
        # not found "item"
        self.assertEqual(newList.indexOf("item"), -1)

    def testAddFirst(self):
        newList = LinkedLists()

        # add item
        newList.addFirst("item 1")
        newList.addFirst("item 2")
        newList.addFirst("item 3")

        # find item index => test
        self.assertEqual(newList.indexOf("item 3"), 0)
        self.assertEqual(newList.length(), 3)
        # not found "item"
        self.assertEqual(newList.indexOf("item"), -1)

    def testRemoveFirst(self):
        newList = LinkedLists()

        # add item
        newList.addLast("item 1")
        newList.addLast("item 2")
        newList.addFirst("item 3")

        # remove first
        # current: item3 --> item1 --> item2 --> null
        newList.removeFirst()
        # after remove: item1 --> item2 --> null

        # test indexOf item and length
        self.assertEqual(newList.indexOf("item 1"), 0)
        self.assertEqual(newList.length(), 2)

    def testToString(self):
        newList = LinkedLists()

        # add item
        newList.addLast("item 1")
        newList.addLast("item 2")
        newList.addLast("item 3")

        # test
        expected = "item 1 --> item 2 --> item 3 --> null"
        self.assertEqual(newList.toString(), expected)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
