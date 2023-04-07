class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def contains_list(self, list1, list2):
        current = list2.head
        while current is not None:
            if current.data == list1.head.data:
                temp_current = current
                temp_list1 = list1.head
                while temp_current is not None and temp_list1 is not None and temp_current.data == temp_list1.data:
                    temp_current = temp_current.next
                    temp_list1 = temp_list1.next
                if temp_list1 is None:
                    return True
            current = current.next
        return False

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

# Приклад використання

# Створення списків
list1 = DoublyLinkedList()
list1.add_node(1)
list1.add_node(2)
list1.add_node(3)

list2 = DoublyLinkedList()
list2.add_node(0)
list2.add_node(1)
list2.add_node(2)
list2.add_node(3)
list2.add_node(4)

# Роздрукування списків
print("List 1: ", end="")
list1.print_list()

print("List 2: ", end="")
list2.print_list()

# Перевірка наявності списку list1 в списку list2
if list2.contains_list(list1, list2):
    print("List 1 is a part of List 2")
else:
    print("List 1 is not a part of List 2")
