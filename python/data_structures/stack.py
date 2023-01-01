from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_

    def __str__(self):

        return f"{self.value}"


class Stack:
    """
    Put docstring here
    """

    def __init__(self, top=None):
        self.top = top

    def __str__(self):
        if self.head is None:
            return "Method not allowed on empty collection"


    def push(self, value):
        if self.top is None:
            self.top = Node(value)
            return

        old_top = self.top
        self.top = Node(value)
        self.top.next_ = old_top

        #self.top = (Node(value, self.top)) as thing as above

    def pop(self):
        if self.top is None:
            raise InvalidOperationError
        popped = self.top
        self.top = self.top.next_
        return popped.value

    def is_empty(self):
        if self.top is None:
            return True
        return False


    def peek(self):
        if self.top is None:
            raise InvalidOperationError
        return self.top.value



