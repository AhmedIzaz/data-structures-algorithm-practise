class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)

class LinkedList:
    def __init__(self):
        self.head = Node()

    def __repr__(self):
        nodes = []
        current_node = self.head.next
        while current_node:
            nodes.append(repr(current_node))
            current_node = current_node.next
        return ",".join(nodes)

    def prepand(self, data):
        node = Node(data, self.head.next)
        self.head.next = node
    
    def append(self, data):
        node = Node(data)
        if self.head.next == None:
            self.head.next = node
            return
        current_node = self.head.next
        while current_node.next:
            current_node = current_node.next
        current_node.next = node    
    
    def search(self, item):
        current_node = self.head.next
        while current_node:
            if current_node.data == item:
                return current_node
            current_node = current_node.next
        return None
        `