#  File: Poly.py
#  Description:
#  Student Name: Hoang Randy Hy Le
#  Student UT EID: hhl385
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created:
#  Date Last Modified:

import sys


class Link(object):
    def __init__(self, coeff=1, exp=1, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__(self):
        return '(' + str(self.coeff) + ', ' + str(self.exp) + ')'


class LinkedList(object):
    def __init__(self):
        self.first = None

    # keep Links in descending order of exponents
    def insert_in_order(self, coeff, exp):
        new_link = Link(coeff, exp)

        # Only if the list contains nothing will it return nothing.
        if self.first is None:
            new_link.next = None
            self.first = new_link
            return
        # Handles if the item should be inserted at the start
        if exp > self.first.exp:
            new_link.next = self.first
            self.first = new_link
            return
        if exp == self.first.exp:
            self.first.coeff += coeff
            return

        current = self.first
        # Keep iterating either till None or when data is less then
        # next node.
        while current.next and current.next.exp > exp:
            current = current.next

        if current.next and current.next.exp == exp:
            current.next.coeff += coeff
            return
        new_link.next = current.next
        current.next = new_link

    # add polynomial p to this polynomial and return the sum
    def add(self, p):
        current = self.first
        other_current = p.first

        if current is None:
            return p
        elif other_current is None:
            return self

        return self.add_helper(current, other_current)

    def add_helper(self, current, other_current):
        new_list = LinkedList()
        while current and other_current:
            if current.exp == other_current.exp:
                new_list.insert_in_order((current.coeff + other_current.coeff),
                                         current.exp)
                current = current.next
                other_current = other_current.next
            elif current.exp > other_current.exp:
                new_list.insert_in_order(current.coeff, current.exp)
                current = current.next
            else:
                new_list.insert_in_order(other_current.coeff,
                                         other_current.exp)
                other_current = other_current.next
        while current:
            if current.coeff:
                new_list.insert_in_order(current.coeff, current.exp)
            current = current.next
        while other_current:
            if other_current.coeff:
                new_list.insert_in_order(other_current.coeff,
                                         other_current.exp)
            other_current = other_current.next
        return new_list

    # multiply polynomial p to this polynomial and return the product
    def mult(self, p):
        current = self.first
        new_list = LinkedList()

        while current:
            other_current = p.first
            temp = LinkedList()
            while other_current:
                new_coeff = current.coeff * other_current.coeff
                new_exp = current.exp + other_current.exp
                temp.insert_in_order(new_coeff, new_exp)
                other_current = other_current.next
            current = current.next
            new_list = new_list.add(temp)
        return new_list

    # create a string representation of the polynomial
    def __str__(self):
        current = self.first
        if not current:
            return ''
        p = f'{current}'
        while current and current.next:
            current = current.next
            p += f' + {current}'
        return p


def make_new_list(n):
    list1 = LinkedList()
    for i in range(n):
        coeff, exp = [int(j) for j in sys.stdin.readline().strip().split(' ')]
        list1.insert_in_order(coeff, exp)
    return list1


def main():
    # read data from file poly.in from stdin
    n = int(sys.stdin.readline().strip())
    list1 = make_new_list(n)
    sys.stdin.readline().strip()
    # create polynomial p
    p = list1
    # create polynomial q
    n2 = int(sys.stdin.readline().strip())
    list2 = make_new_list(n2)
    q = list2
    # get sum of p and q and print sum
    sum_list = p.add(q)
    print(sum_list)
    # get product of p and q and print product
    product_list = p.mult(q)
    print(product_list)


if __name__ == "__main__":
    main()
