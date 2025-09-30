class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):  # O(1)
        new_node = DNode(data)
        if self.head:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def traverse_forward(self):  # O(n)
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")