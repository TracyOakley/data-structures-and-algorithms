from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    this class inherits from the Binary Tree so no __init__
    """

    def add(self, value, root=None):

        # I was able to get the value to add to the correct location in the tree
        # But I have to reorder the tree so the root is in the middle

        #if self.root.in_order() > 2 then i need to move the root to the middle
        ####************ actually not required I was just calling the recursion to add incorrectly

        if self.root is None:
            self.root = Node(value)
            return

        if root is None:
            root = self.root

        if value > root.value:
            if root.right is None:
                root.right = Node(value)
                return
            else:
                self.add(value, root.right)

            return

        if value < root.value:
            if root.left is None:
                root.left = Node(value)

                return
            else:
                self.add(value, root.left)
            return


    def contains(self, value, root=None):

        if self.root is None:
            return False


        if root is None:
            root = self.root

        print(root.value)

        if root.value == value:
            return True

        if value < root.value:
            if root.left is None:
                return False
            else:
                return self.contains(value, root.left)

        if value > root.value:
            if root.right is None:
                return False
            else:
                return self.contains(value, root.right)


