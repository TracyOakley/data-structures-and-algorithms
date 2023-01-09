
class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def find_maximum_value(self):
        input_list = self.in_order()
        print(type(input_list))

        max_value = input_list[0]

        for i in range(len(input_list)):
            if max_value < input_list[i]:
                max_value = input_list[i]

        return max_value

    def pre_order(self, root=None, nodes=None):

        if root is None:
            root = self.root
        # this handles the transistion from actual root to the other nodes...

        if nodes is None:
            nodes = []
        # this handles the initial list creation and the rest append

        #this technique for recursion is really a deep understanding of how to handle the distinct phases of the function

        nodes.append(root.value)

        if root.left:
            self.pre_order(root.left, nodes)

        if root.right:
            self.pre_order(root.right, nodes)

        return nodes





    def post_order(self, root=None, nodes=None):
        """
        Return a list of nodes in a BT, in post order
            if root.left is not NULL
                postOrder(root.left)
            if root.right is not NULL
                 postOrder(root.right)
            OUTPUT <-- root.value
        """
        if root is None:
            root = self.root
        # this handles the transistion from actual root to the other nodes...

        if nodes is None:
            nodes = []

        if root.left:
            self.post_order(root.left, nodes)

        if root.right:
            self.post_order(root.right, nodes)

        nodes.append(root.value)

        return nodes

    def in_order(self, root=None, nodes=None):

        if root is None:
            root = self.root
        # this handles the transistion from actual root to the other nodes...

        if nodes is None:
            nodes = []

        if root.left:
            self.in_order(root.left, nodes)

        nodes.append(root.value)

        if root.right:
            self.in_order(root.right, nodes)

        return nodes


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

