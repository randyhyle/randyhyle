#  File: TestLinkedList.py
#  Description:
#  Student Name: Hoang Randy Hy Le
#  Student UT EID: hhl385
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created:
#  Date Last Modified:

class Link(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList(object):
    # create a linked list
    # you may add other attributes
    def __init__(self):
        self.first = None

    # get number of links
    def get_num_links(self):
        current = self.first
        # If current is None, return 0
        if not current:
            return 0

        count = 1
        while current.next:
            current = current.next
            count += 1
        return count

    # add an item at the beginning of the list
    def insert_first(self, data):
        new_link = Link(data)
        # Just insert the item at the beginning of the linked list
        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, data):
        new_link = Link(data)

        current = self.first
        if current is None:
            self.first = new_link
            return
        # Iterate to the end of the list
        while current.next:
            current = current.next
        # Put the next pointer to the new link
        current.next = new_link

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order(self, data):
        new_link = Link(data)

        # Only if the list contains nothing will it return nothing.
        if self.first is None:
            new_link.next = None
            self.first = new_link
            return
        # Handles if the item should be inserted at the start
        if data <= self.first.data:
            self.insert_first(data)
            return

        current = self.first
        # Keep iterating either till None or when data is less then
        # next node.
        while current.next and current.next.data <= data:
            current = current.next

        new_link.next = current.next
        current.next = new_link

    # search in an unordered list, return None if not found
    def find_unordered(self, data):
        current = self.first

        # While there is still a list, keep iterating
        while current:
            if current.data == data:
                return current
            else:
                current = current.next
        return None

    # Search in an ordered list, return None if not found
    def find_ordered(self, data):
        current = self.first

        while current and current.data <= data:
            # If current node is equal to data passed in we have found
            # it
            if current.data == data:
                return current
            # Otherwise keep iterating
            else:
                current = current.next
        return None

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link(self, data):
        # Handles if the very first Link is the one to be deleted
        if self.first.data == data:
            found = self.first
            self.first = found.next
            return found
        current = self.first
        while current.next:
            # If found, set the currents next pointer to the one after
            # found
            if current.next.data == data:
                found = current.next
                current.next = found.next
                return found

            current = current.next

        return None

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__(self):
        current = self.first
        item = ''

        count = 0
        while current:
            item += str(current.data) + '  '
            current = current.next
            count += 1

            if count == 10:
                item += '\n'
                count = 0
        return item

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list(self):
        new_list = LinkedList()
        current = self.first
        while current:
            # Utilize insert_last while iterating
            new_list.insert_last(current.data)
            current = current.next
        return new_list

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list(self):
        new_list = LinkedList()
        current = self.first
        while current:
            # Utilize insert_first while iterating
            new_list.insert_first(current.data)
            current = current.next
        return new_list

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list(self):
        # Create a new linked list object
        new_list = LinkedList()
        current = self.first
        while current:
            # Iterating through original list, insert_in_order to the
            # new_list
            new_list.insert_in_order(current.data)
            current = current.next
        return new_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted(self):
        if self.is_empty():
            return True

        current = self.first
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next

        return True

    # Return True if a list is empty or False otherwise
    def is_empty(self):
        return self.first is None

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list(self, other):
        new_list = LinkedList()

        current = self.first
        other_current = other.first
        # Utilizing the insert_in_order method, the while loop will
        # keep inserting into the new list in sorted order until
        # None is reached.
        while current and other_current:
            new_list.insert_in_order(current.data)
            new_list.insert_in_order(other_current.data)
            current = current.next
            other_current = other_current.next
        return new_list

    # Test if two lists are equal, item by item and return True
    def is_equal(self, other):
        current = self.first
        other_current = other.first

        while current and other_current:
            if current.data != other_current.data:
                return False
            current = current.next
            other_current = other_current.next
        return True

    # Return a new list, keeping only the first occurrence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates(self):
        new_list = self.copy_list()
        present_nums = [new_list.first.data]

        current = new_list.first
        while current.next:
            # While iterating, check to see if there is a duplicate
            if current.next.data not in present_nums:
                present_nums.append(current.next.data)
                current = current.next
            else:
                current.next = current.next.next

        return new_list


def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    testlist = [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    mix_up = [1, 3, 5, 2, 4, 6, 8]
    merge_list1 = [0, 1, 2, 3, 4]
    merge_list2 = [5, 6, 7, 8, 9]

    print("testing insert_first")
    list1 = LinkedList()

    for item in testlist:
        list1.insert_first(item)
    print(list1)

    # Test method insert_last()
    list2 = LinkedList()

    for item in testlist:
        list2.insert_last(item)

    print("testing insert_last")
    print(list2)
    # Test method insert_in_order()
    list3 = LinkedList()

    for item in mix_up:
        list3.insert_in_order(item)
    print('testing insert_in_order')
    print(list3)

    # Test method get_num_links()
    print('testing get_num_links')
    print(list1.get_num_links())

    # Test method find_unordered()
    # Consider two cases - data is there, data is not there
    print('testing find_unordered')
    print(list3.find_unordered(4))

    # Test method find_ordered()
    # Consider two cases - data is there, data is not there
    print('testing find_ordered')
    print(list2.find_ordered(16))
    print(list2.find_ordered(17))

    # Test method delete_link()
    # Consider two cases - data is there, data is not there
    print('testing delete_link')
    list1.delete_link(10)
    print(list1)

    # Test method copy_list()
    print('testing copy_list')
    print('original', list1)
    print(list1.copy_list())

    # Test method reverse_list()
    print('testing reverse_list')
    print(list1.reverse_list())

    # Test method sort_list()
    list4 = LinkedList()
    for item in mix_up:
        list4.insert_last(item)
    print('testing sort_list')
    print(list4.sort_list())

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    list5 = LinkedList()
    for item in mix_up:
        list5.insert_last(item)
    print('testing is_sorted')
    print(list3.is_sorted())
    print(list5.is_sorted())

    # Test method is_empty()
    list6 = LinkedList()
    print('testing is_empty')
    print(list5.is_empty())
    print(list6.is_empty())

    # Test method merge_list()
    print('testing merge_list')
    list7 = LinkedList()
    list8 = LinkedList()
    for item in merge_list1:
        list7.insert_last(item)
    for item in merge_list2:
        list8.insert_last(item)
    print(list7.merge_list(list8))

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print('testing is_equal')
    print(list7.is_equal(list8))

    # Test remove_duplicates()
    testll = LinkedList()
    [testll.insert_last(i) for i in [1, 1, 2, 2]]
    print('testing remove_duplicates')
    print(testll)
    print(testll.remove_duplicates())
    print()


if __name__ == "__main__":
    main()
