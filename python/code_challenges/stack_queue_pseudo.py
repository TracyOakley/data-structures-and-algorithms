from data_structures.stack import Stack, Node

class PseudoQueue:

    def __init__(self):
        self.OutputStack = Stack()
        self.InputStack = Stack()


    def enqueue(self, value):
        if self.InputStack.top is None:
            self.InputStack.top = self.OutputStack.top = Node(value)
            return

        New_Output_Stack = Stack()
        New_Output_Stack.push(value)
        next_node = self.InputStack.top

        # create a copy of the input stack with a while and next_
        while next_node:
            New_Output_Stack.push(next_node.value)
            next_node = next_node.next_

        self.OutputStack = New_Output_Stack
        #self.InputStack = self.InputStack.push(value) because the push return nothing
        self.InputStack.push(value)

    def dequeue(self):
        new_Input_Stack = Stack()
        popped = self.OutputStack.pop()
        next_node = self.OutputStack.top

        while next_node:
            new_Input_Stack.push(next_node.value)
            next_node = next_node.next_

        self.InputStack.top = new_Input_Stack.top
        return popped









