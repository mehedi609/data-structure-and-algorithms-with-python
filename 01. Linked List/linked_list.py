class Node:
    def __init__(self, value, next = None):
        self.data = value
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display_list(self):
        pass

    def count_nodes(self):
        pass

    def search(self, d):
        pass

    def insert_in_beginning(self, d):
        pass

    def insert_at_end(self, d):
        pass

    def create_list(self):
        pass

    def insert_after(self, data, existing_value):
        pass

    def insert_before(self, data, existing_value):
        pass

    def insert_at_position(self, data, position):
        pass

    def delete_node(self, x):
        pass

    def delete_first_node(self):
        pass

    def delete_last_node(self):
        pass

    def reverse_list(self):
        pass

    def bubble_sort_exdata(self):
        pass

    def bubble_sort_exlinks(self):
        pass

    def has_cycle(self):
        pass

    def find_cycle(self):
        pass

    def remove_cycle(self):
        pass

    def insert_cycle(self, x):
        pass

    def merge2(self, list2):
        pass

    def _merge2(self, p1, p2):
        pass

    def merge_sort(self):
        pass

    def _merge_sort_rec(self, listStart):
        pass

    def _divide_list(self, p):
        pass


def display_options():
    print('1. Display list')
    print('2. Count the number of nodes')
    print('3. Search for an element')
    print('4. Insert at beginning')
    print('5. Insert at end')
    print('6. Insert after a specified node')
    print('7. Insert before a specified node')
    print('8. Insert at a given position')
    print('9. Delete first Node')
    print('10. Delete last node')
    print('11. Delete any node')
    print('12. Reverse the list')
    print('13. Bubble sort by exchanging data')
    print('14. Bubble sort by exchanging link')
    print('15. MargeSort')
    print('16. Insert cycle')
    print('17. Detect cycle')
    print('18. Delete cycle')
    print('19. Quit')
    print()


linked_list = SingleLinkedList()
linked_list.create_list()

while True:
    display_options()
    option = int(input('Enter Option: '))

    if option == 1:
        linked_list.display_list()
    elif option == 2:
        linked_list.count_nodes()
    elif option == 3:
        data = int(input('Enter the element to be searched: '))
        linked_list.search(data)
    elif option == 4:
        data = int(input('Enter your element to be inserted: '))
        linked_list.insert_in_beginning(data)
    elif option == 5:
        data = int(input('Enter your element to be inserted: '))
        linked_list.insert_at_end(data)
    elif option == 6:
        data = int(input('Enter your element to be inserted: '))
        element = int(input('Enter your element after which to insert: '))
    elif option == 7:
        data = int(input('Enter your element to be inserted: '))
        element = int(input('Enter your element before which to insert: '))
    elif option == 8:
        data = int(input('Enter your element to be inserted: '))
        element = int(input('Enter the position at which to insert: '))
    elif option == 9:
        linked_list.delete_first_node()
    elif option == 10:
        linked_list.delete_last_node()
    elif option == 11:
        data = int(input('Enter your element to be deleted: '))
        linked_list.delete_node(data)
    elif option == 12:
        linked_list.reverse_list()
    elif option == 13:
        linked_list.bubble_sort_exdata()
    elif option == 14:
        linked_list.bubble_sort_exlinks()
    elif option == 15:
        linked_list.merge_sort()
    elif option == 16:
        data = int(input('Enter the element at which the cycle has to be inserted: '))
        linked_list.insert_cycle(data)
    elif option == 17:
        if linked_list.has_cycle():
            print('List has a cycle')
        else:
            print('List does not have a cycle')
    elif option == 18:
        linked_list.remove_cycle()
    elif option == 19:
        break
    else:
        print('Invalid Input.')
    print()
