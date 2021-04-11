import unittest

def binarySearch(arr, key):
    first = 0
    last = len(arr) - 1
    middle = (first + last) // 2

    while first <= last:
        if arr[middle] == key:
            return middle
        elif arr[middle] < key:
            first = middle + 1
        else:
            last = middle - 1
        middle = (first + last) // 2

    return -1

def binarySearchRecursion(arr, key, first, last):
    middle = (first + last) // 2

    if(first > last):
        return -1

    if arr[middle] == key:
        return middle
    elif arr[middle] < key:
        return binarySearchRecursion(arr, key, middle + 1, last)
    else:
        return binarySearchRecursion(arr, key, first, middle - 1)

class UnitTest(unittest.TestCase):

    def testBinarySearch(self):
        arr = [1, 2, 3, 3, 4, 6, 7, 8, 10]
        self.assertEqual(binarySearch(arr, 6), 5)
        self.assertEqual(binarySearch(arr, 1), 0)
        self.assertEqual(binarySearch(arr, 4), 4)

    def testBinarySearchRecursion(self):
        arr = [1, 2, 3, 3, 4, 6, 7, 8, 10]
        arrSize = len(arr) - 1
        self.assertEqual(binarySearchRecursion(arr, 6, 0, arrSize), 5)
        self.assertEqual(binarySearchRecursion(arr, 1, 0, arrSize), 0)
        self.assertEqual(binarySearchRecursion(arr, 4, 0, arrSize), 4)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(UnitTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
