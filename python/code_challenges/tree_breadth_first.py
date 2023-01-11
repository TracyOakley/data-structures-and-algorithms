from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


def breadth_first(tree_input):
    if tree_input.root is None:
        return []
    result_list = []
    queue = Queue()

    def helper(node):
        #nonlocal result_list
        #nonlocal queue
        result_list.append(node.value)
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)
        if not queue.is_empty():
            helper(queue.dequeue())

    helper(tree_input.root)

    return result_list

