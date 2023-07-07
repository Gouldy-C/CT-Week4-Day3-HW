class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f'<Node: {self.value}>'

if __name__ == '__main__':
    print('Node: File Ran')
