import unittest
from Queue import Queue

class UnitTest(unittest.TestCase):

    def testQueue(self):
        queue = Queue()

        with self.assertRaises(Exception):
            queue.dequeue()

        queue.enqueue(12)
        queue.enqueue(10)
        queue.enqueue(17)
        queue.enqueue(7)
        queue.enqueue(21)
        self.assertEqual(queue.head.data, 12)
        self.assertEqual(queue.tail.data, 21)

        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.head.data, 17)

        self.assertEqual(queue.dequeue(), 17)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
