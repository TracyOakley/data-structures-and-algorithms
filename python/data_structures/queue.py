from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_

    def __str__(self):

        return f"{self.value}"



class Queue:
    """
    Put docstring here
    """

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        if self.front is None:
            self.front = self.rear = Node(value)
            #self.front = Node(value) bc creating a new Node and not the same reference even though same value
            #self.rear = Node(value)

            return

        if self.front == self.rear:

            self.front.next_ = self.rear = Node(value)
            # self.front.next_ = Node(value)
            # self.rear = Node(value)
            return


        old_back = self.rear
        self.rear = old_back.next_ = Node(value)


        #the next is the one behind in line ***********************

    def dequeue(self):
        if self.front is None:
            raise InvalidOperationError

        deq = self.front
        self.front = deq.next_
        return deq.value

    def peek(self):
        if self.front is None:
            raise InvalidOperationError
        return self.front.value


    def is_empty(self):
        if self.front is None:
            return True
        return False
