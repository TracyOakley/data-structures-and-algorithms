
class Node:
    def __init__(self, value, next1=None):
        self.value = value
        self.next1 = next1

    def __str__(self):
        return f"{ {self.value} }"


class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.linked_list = []
        self.head = None

    def append(self, value):
        self.linked_list.append(Node(value))

    def insert_before(self, looking_for, value2):
        old_list = []
        if len(self.linked_list) > 0:
            old_list = self.linked_list
            self.linked_list = []

        for node1 in old_list:
            if node1.value == looking_for:
                self.linked_list.append(Node(value2))
            self.linked_list.append(node1)

    def insert_after(self, looking_for, value2):
        old_list = []
        if len(self.linked_list) > 0:
            old_list = self.linked_list
            self.linked_list = []

        for node1 in old_list:
            self.linked_list.append(node1)
            if node1.value == looking_for:
                self.linked_list.append(Node(value2))

    def insert(self, value):
        old_list = []
        if len(self.linked_list) > 0:
            old_list = self.linked_list
        self.linked_list = [Node(value)]
        for item in old_list:
            self.linked_list.append(item)
        self.head = self.linked_list[0]

    def includes(self, looking_for):
        included = False
        for node in self.linked_list:
            if node.value == looking_for:
                included = True
        return included

    def __str__(self):
        list_string = ""
        if(len(self.linked_list) == 0):
            return "NULL"
        else:
            nodes_from_list = [str(member) for member in self.linked_list]

            list_string =  " -> ".join(nodes_from_list)

        return list_string + " -> NULL"




class TargetError:
    pass
