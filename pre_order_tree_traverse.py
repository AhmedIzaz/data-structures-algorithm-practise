class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def __repr__(self):
        return repr(self.data)

def pre_order(Node):
    print(Node)

    if Node.left:
        pre_order(Node.left)
    if Node.right:
        pre_order(Node.right)

if __name__ == "__main__":


    seven = Node(7)
    one = Node(1)
    three = Node(3)
    nine = Node(9)
    two = Node(2)
    five = Node(5)
    six = Node(6)
    ten = Node(10)
    eleven = Node(11)
    fifteen = Node(15)
    seventeen = Node(17)
    seven.left = one
    seven.right = six
    one.left = three
    one.right = nine
    nine.left = two
    nine.right = five
    six.left = ten
    six.right = eleven
    ten.left = fifteen
    ten.right = seventeen

    pre_order(seven)