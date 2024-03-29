from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    this class inherits from the Binary Tree so no __init__
    """
    #iterative version of add
    # def add(self, value):
    #     def walk(root, node_to_add):
    #
    #         if not root:
    #             return
    #
    #         if node_to_add.value < root.value:
    #             if root.left:
    #                 walk(root.left, node_to_add)
    #             else:
    #                 root.left = node_to_add
    #         else:
    #             if root.right:
    #                 walk(root.right, node_to_add)
    #             else:
    #                 root.right = node_to_add
    #
    #     node = Node(value)
    #
    #     if not self.root:
    #         self.root = node
    #         return
    #
    #     walk(self.root, node)

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

    #iterative version of contains
    def contains(self, value):
        def walk(value, root):
            if not root:
                return False

            return (
                    root.value == value or walk(value, root.left) or walk(value, root.right)
            )

        return walk(value, self.root)

    #def add(self, value):
        # check for empty BST
        # if self.root is None:
            #self.root = Node(value)
            #return

        # start pointer at root
        #current = self.root

        #while current:
            # if number of the added node is less than current node, check left
        # if value < current.value:
                # add node only if there's space
        #  if current.left is None:
        #   current.left = Node(value)
        #   return

                # if there's no space go left
        #  current = current.left

            # if number of the added node is greater than current node, check right
        # else:
                # add node only if there's space
        #  if current.right is None:
        #    current.right = Node(value)
        #    return

                # if there's no space go right
    # current = current.right
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


