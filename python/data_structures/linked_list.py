
class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next_ = next_

    def __str__(self):

        return f"{self.value}"



class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None



    def kth_from_end(self, position):

        current = self.head
        length_of_list = 0
        i = 0

        while current:
            length_of_list += 1
            current = current.next_

        if position < 0:
            raise TargetError

        if length_of_list - 1 < position:
            raise TargetError

        search_here = length_of_list - position - 1

        current = self.head

        while current:
            if search_here == i:
                return current.value
            i += 1
            current = current.next_



    def append(self, value):

        current = self.head

        if current is None:
            self.head = Node(value)
        else:

            while current:
                if current.next_ is None:
                    current.next_ = Node(value)
                    break
                current = current.next_



    def insert_before(self, looking_for, value2):

        current = self.head

        if current is None:
            raise TargetError

        if current.next_ is None and current.value == looking_for:
            old_head = current
            self.head = Node(value2)
            self.head.next_ = old_head
            return

        while current:
            if current.next_ is not None and current.next_.value == looking_for:
                old_next = current.next_
                current.next_ = Node(value2)
                current.next_.next_ = old_next
                return
            current = current.next_

        raise TargetError
    def insert_after(self, looking_for, value2):

        current = self.head

        if current is None:
            raise TargetError

        while current:
            if current.value == looking_for:
                old_next = current.next_
                current.next_ = Node(value2)
                current.next_.next_ = old_next
                return
            current = current.next_
        raise TargetError

    def insert(self, val):
        #insert should as to front of list

        node_to_insert = Node(val)
        old_head = self.head

        self.head = node_to_insert
        self.head.next_ = old_head


    def includes(self, looking_for):
        included = False

        current = self.head

        while current:
            if current.value == looking_for:
                included = True
                break
            else:
                current = current.next_

        return included

    def __str__(self):
        list_string = ""

        if(self.head is None):
            return "NULL"
        current = self.head

        while current:

            node_string = "{ " + str(current.value) +" } -> "
            list_string += node_string
            current = current.next_

        return list_string + "NULL"




class TargetError(Exception):
    pass
