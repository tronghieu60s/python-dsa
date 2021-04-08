import unittest
from Queue import Queue

class UnitTest(unittest.TestCase):

    def testQueue(self):
        queue = Queue(5)

        self.assertEqual(queue.empty(), True)
        with self.assertRaises(Exception):
            queue.dequeue()

        queue.enqueue(12)
        queue.enqueue(10)
        queue.enqueue(17)
        self.assertEqual(queue.arr, [12, 10, 17, None, None])

        queue.enqueue(7)
        queue.enqueue(21)
        self.assertEqual(queue.full(), True)

        queue.dequeue()
        queue.dequeue()
        self.assertEqual(queue.arr, [None, None, 17, 7, 21])

        queue.dequeue()
        self.assertEqual(queue.dequeue(), 7)

        queue.dequeue()
        self.assertEqual(queue.empty(), True)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
