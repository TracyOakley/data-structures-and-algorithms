from data_structures.queue import Queue
from data_structures.stack import Stack


def multi_bracket_validation(input):

    input_list = list(input)

    bracket_queue = Queue()
    bracket_stack_storage = Stack()

    if input == "":
        return True

    print(input_list)

    while input_list:
        add_to_queue = input_list.pop(0)
        if add_to_queue == "{" or add_to_queue == "}" or add_to_queue == "(" or add_to_queue == ")" or add_to_queue == "[" or add_to_queue == "]":
            bracket_queue.enqueue(add_to_queue)


    while not bracket_queue.is_empty() or not bracket_stack_storage.is_empty():
        dq = bracket_queue.dequeue()
        print(dq)

        if dq == ")" or dq == "}" or dq == "]":
            if bracket_stack_storage.is_empty():
                return False
            if bracket_stack_storage.peek()+dq == "()" or bracket_stack_storage.peek()+dq == "[]" or bracket_stack_storage.peek()+dq == "{}":
                dq = ""
                bracket_stack_storage.pop()
            else:
                return False

        if dq == "(" or dq == "{" or dq == "[":
            if dq+bracket_queue.peek() == "()" or dq+bracket_queue.peek() == "[]" or dq+bracket_queue.peek() == "{}":
                bracket_queue.dequeue()
            else:
                bracket_stack_storage.push(dq)

    return True




