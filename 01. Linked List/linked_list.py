class Node:
    def __init__(self, value, next = None):
        self.data = value
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def display_list(self):
        if self.head is None:
            print('List is empty')
        else:
            node = self.head

            print('The list is: ', end='')
            while node is not None:
                print(f"{node.data} ", end='')
                node = node.next
            print()

    def count_nodes(self):
        counter = 0
        node = self.head

        while node is not None:
            counter += 1
            node = node.next

        print(f'Number of nodes in the list = {counter}')

    def search(self, d):
        position = 1
        node = self.head

        while node is not None:
            if node.data == d:
                print(f"{d} is at position {position}")
                break
            node = node.next
            position += 1
        else:
            print(f"{d} not found in the list")

    def insert_in_beginning(self, d):
        temp_node = Node(d, self.head)
        self.head = temp_node

    def insert_at_end(self, d):
        temp_node = Node(d)

        if self.head is None:
            self.head = temp_node
            return
        else:
            node = self.head
            while node.next is not None:
                node = node.next
            node.next = temp_node

    def create_list(self):
        n = int(input('Enter the number of nodes: '))
        if n == 0:
            return
        for _ in range(n):
            d = int(input('Enter the element: '))
            self.insert_at_end(d)
        print()

    def insert_after(self, data, existing_value):
        node = self.head

        while node is not None:
            if node.data == existing_value:
                break
            node = node.next
        else:
            print(f"{existing_value} not present in the list")
            return

        temp_node = Node(data, node.next)
        node.next = temp_node

    def insert_before(self, data, existing_value):
        # if list is empty
        if self.head is None:
            print('List is empty')
            return

            # if data is in first node and new node is to be inserted before the first node
        node = self.head
        if existing_value == node.data:
            temp_node = Node(data, node)
            self.head = temp_node
            return

        while node.next is not None:
            if node.next.data == existing_value:
                break
            node = node.next
        else:
            print(f"{existing_value} not present in the list")
            return

        temp_node = Node(data, node.next)
        node.next = temp_node

    def insert_at_position(self, data, position):
        if self.head is None:
            print('List is empty')
            return

        node = self.head
        if position == 1:
            temp_node = Node(data, node.next)
            node.next = temp_node
            return

        i = 1
        while i < position - 1 and node is not None:
            node = node.next
            i += 1

        if node is None:
            print(f'You can insert only upto position {i}')
        else:
            temp_node = Node(data, node)
            node.next = temp_node

    def delete_node(self, x):
        if self.head is None:
            print('List is Empty')
            return

            # Deletion of first node
        node = self.head
        if node.data == x:
            self.head = node.next
            return

            # Delete in between or end the end
        while node.next is not None:
            if node.next.data == x:
                break
            node = node.next
        else:
            print(f"{x} is not in the list")
            return

        node.next = node.next.next

    def delete_first_node(self):
        if self.head is None:
            print('List is Empty')
        else:
            self.head = self.head.next

    def delete_last_node(self):
        if self.head is None:
            print('List is Empty')
            return

        if self.head.next is None:
            self.head = None
            return

        node = self.head
        while node.next.next is not None:
            node = node.next
        node.next = None

    def reverse_list(self):
        prev_node = None
        cur_node = self.head

        while cur_node is not None:
            next_node = cur_node.next
            cur_node.next = prev_node
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node

    def bubble_sort_exdata(self):
        end = None
        while end is not self.head.next:
            cur_node = self.head
            while end is not cur_node.next:
                next_node = cur_node.next
                if cur_node.data > next_node.data:
                    cur_node.data, next_node.data = next_node.data, cur_node.data
                cur_node = next_node
            end = cur_node

    def bubble_sort_exlinks(self):
        end = None
        while end is not self.head.next:
            cur_node = prev_node = self.head
            while end is not cur_node.next:
                next_node = cur_node.next
                if cur_node.data > next_node.data:
                    cur_node.next = next_node.next
                    next_node.next = cur_node
                    if cur_node is self.head:
                        self.head = next_node
                    else:
                        prev_node.next = next_node
                    cur_node, next_node = next_node, cur_node
                    prev_node = cur_node
                    cur_node = cur_node.next
            end = cur_node

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
