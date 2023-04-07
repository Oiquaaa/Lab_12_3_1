import unittest
from laba12_3_1 import DoublyLinkedList

class TestDoublyLinkedList(unittest.TestCase):
    def setUp(self):
        self.list1 = DoublyLinkedList()
        self.list1.add_node(1)
        self.list1.add_node(2)
        self.list1.add_node(3)

        self.list2 = DoublyLinkedList()
        self.list2.add_node(0)
        self.list2.add_node(1)
        self.list2.add_node(2)
        self.list2.add_node(3)
        self.list2.add_node(4)
        
    def test_contains_list(self):
        self.assertTrue(self.list2.contains_list(self.list1, self.list2))
        self.assertFalse(self.list1.contains_list(self.list2, self.list1))

if __name__ == '__main__':
    unittest.main()
