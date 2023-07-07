from Node import Node


class Bst():
    def __init__(self, value=None):
        if value:
            self.root = Node(value)
        else:
            self.root = None
        self.ordered_list = []

    def append_bst(self, value, current_node=None):
        if not self.root:
            self.root = Node(value)
            return
        
        if not current_node:
            current_node = self.root
        
        if value < current_node.value:
            if current_node.left:
                self.append_bst(value, current_node.left)
            else:
                current_node.left = Node(value)
        elif value > current_node.value:
            if current_node.right:
                self.append_bst(value, current_node.right)
            else:
                current_node.right = Node(value)
        else:
            return 'Node already exists with that value.'

    def in_order(self, current_node=None):
        if not current_node:
            self.ordered_list = []
            current_node = self.root
        if current_node.left:
            self.in_order(current_node.left)
        self.ordered_list.append(current_node.value)
        if current_node.right:
            self.in_order(current_node.right)

    def from_list(self, lst):
        for n in lst:
            self.append_bst(n)


def test():
    tree = Bst()
    tree.from_list([5,2,3,1,6,8])
    tree.in_order()
    print(tree.ordered_list)
    
    



if __name__ == '__main__':
    test()