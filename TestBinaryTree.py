#  File: TestBinaryTree.py
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


class Node(object):
    def __init__(self, data):
        self.data = data
        self.lChild = None
        self.rChild = None


class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if not self.root:
            self.root = new_node
            return

        current = self.root
        parent = self.root
        while current:
            parent = current
            if current.data > data:
                current = current.lChild
            else:
                current = current.rChild
        if parent.data > data:
            parent.lChild = new_node
        else:
            parent.rChild = new_node

    # Returns true if two binary trees are similar
    def is_similar(self, pNode):
        current = self.root
        other_current = pNode.root
        return self.is_similar_helper(current, other_current)

    def is_similar_helper(self, node, pNode):
        if node and pNode:
            if node.data == pNode.data:
                return self.is_similar_helper(node.lChild, pNode.lChild) \
                       and self.is_similar_helper(node.rChild, pNode.rChild)
            return False
        if not node and not pNode:
            return True
        return False

    # Returns a list of nodes at a given level from left to right
    def get_level(self, level):
        return self.get_level_helper(self.root, level)

    def get_level_helper(self, node, level):
        node_list = []
        if node is None:
            return node_list
        if level == 0:
            node_list.append(node)
            return node_list

        node_list += self.get_level_helper(node.lChild, level - 1)
        node_list += self.get_level_helper(node.rChild, level - 1)
        return node_list

    # Returns the height of the tree
    def get_height(self):
        return self.get_height_helper(self.root)

    def get_height_helper(self, current):
        if current is None:
            return -1
        height = 1
        height += max(self.get_height_helper(current.lChild),
                      self.get_height_helper(current.rChild))
        return height

    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes(self):
        return self.num_nodes_helper(self.root)

    def num_nodes_helper(self, node):
        if not node:
            return 0
        count = 1
        count += self.num_nodes_helper(node.lChild)
        count += self.num_nodes_helper(node.rChild)
        return count


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list(map(int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list(map(int, line))  # converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map(int, line))  # converts elements into ints

    tree1 = Tree()
    print('tree1')
    for item in tree1_input:
        tree1.insert(item)
    tree2 = Tree()
    print('tree2')
    for item in tree2_input:
        tree2.insert(item)
    tree3 = Tree()
    print('tree3')
    for item in tree3_input:
        tree3.insert(item)
    # Test your method is_similar()

    print('here')
    print(tree1.is_similar(tree2))

    # Print the various levels of two of the trees that are different
    print()
    print(tree2.get_level(9))

    # Get the height of the two trees that are different

    # Get the total number of nodes a binary search tree


if __name__ == "__main__":
    main()
