from Node import Node
from BinaryST import Bst


class Dll():
    def __init__(self, value=None):
        self.head = value
        self.tail = value
        if self.head:
            self.length = 1
        else:
            self.length = 0
    
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.right

    
    def __repr__(self):
        res = 'Head -> '
        for node in self:
            res = res + f'{node.value} ' + '<--> ' if node.right else res + f'{node.value} ' + '<- '
        res = res + 'Tail'
        return f'Linked List: {res}'
    
    
    def append_dll(self, new_value):
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.length += 1
        else:
            self.tail.right = new_node
            new_node.left = self.tail
            self.tail = new_node
            self.length += 1
    
    
    def sorted_dll(self, lst):
        tree = Bst()
        tree.from_list(lst)
        tree.in_order()
        for n in tree.ordered_list:
            self.append_dll(n)
        print(self)


def test():
    linked_list = Dll() 
    linked_list.sorted_dll([50, 45, 56,5,50,57,48,44,42,41,43])


if __name__ == "__main__":
    test()