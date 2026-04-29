# Node class
class Node:
    def __init__(self, item):
        self.__item = item
        self.__left = None
        self.__right = None

    def item(self):
        return self.__item
    
    def left(self, left = None):
        if left == None:
            return self.__left
        self.__left = left

    def right(self, right = None):
        if right == None:
            return self.__right
        self.__right = right

# BST
class BST:
    def __init__(self, root):
        self.__root = Node(root)

    def search(self, item):
        parent = self.__root.item()
        while True:
            if item == None:
                return False
            elif item == parent:
                return True
            elif item < parent:
                parent = parent.left().item()
            else:
                parent = parent.right().item()

# Building a tree for testing
def BuildTree(alist):
    return # To do

#bst = BuildTree([5, 6, 8, 2, 4, 5, 1, 0, 8, 7, 5, 4])