from data_structures.linked_list import LinkedList
def zip_lists( list_one, list_two):

    result_list = LinkedList()
    list_one_current = list_one.head
    list_two_current = list_two.head

    while list_one_current:

        result_list.append(list_one_current)
        if list_two_current:
            result_list.append(list_two_current)
        list_one_current = list_one_current.next_
        if list_two_current:
            list_two_current = list_two_current.next_

    while list_two_current:
        result_list.append(list_two_current)
        list_two_current = list_two_current.next_
    return result_list
