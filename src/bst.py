# -*- coding: utf-8 -*-
"""Binary Search Tree Module."""
from collections import deque


class Node(object):
    """Define a node class."""

    def __init__(self, value=None, parent=None, left=None, right=None):
        """Initialize a Node object."""
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def depth(self):
        """Return the number of levels in the tree."""
        if self.value is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        else:
            left_depth = self.left.depth() if self.left is not None else 0
            right_depth = self.right.depth() if self.right is not None else 0
            return max(left_depth, right_depth) + 1

    def balance(self):
        """Return a positive integer, 0, or negative integer."""
        if self.value is None:
            return 0
        elif self.left is None and self.right is None:
            return 0
        else:
            left_depth = self.left.depth() if self.left is not None else 0
            right_depth = self.right.depth() if self.right is not None else 0
            return (left_depth - right_depth)

    def pre_order(self):
        """Traverse a tree pre-order."""
        yield self.value
        if self.left:
            for ii in self.left.pre_order():
                yield ii
        if self.right:
            for ii in self.right.pre_order():
                yield ii

    def in_order(self):
        """Traverse a tree in-order."""
        if self.left:
            for ii in self.left.pre_order():
                yield ii
        yield self.value
        if self.right:
            for ii in self.right.pre_order():
                yield ii

    def post_order(self):
        """Traverse a tree post-order."""
        if self.left:
            for ii in self.left.pre_order():
                yield ii
        if self.right:
            for ii in self.right.pre_order():
                yield ii
        yield self.value


class BST(object):
    """Define Binart Search Tree class(BST)."""

    def _reset(self):
        """Reset class variables for testing."""
        self.check_set = set()
        self.top = None

    def __init__(self, values=[]):
        """Initialize BST class."""
        self._reset()
        if isinstance(values, list):
            for ii in values:
                self.insert(ii)
        else:
            raise TypeError("Please package your item into a list!")

    def insert(self, value):
        """Insert a value into the binary heap."""
        if self.contains(value):
            pass
        else:
            cursor = self.top
            new_node = Node(value)
            if self.top is None:
                self.top = new_node
            else:
                while cursor is not None:
                    if cursor.value > new_node.value:
                        old_cursor = cursor
                        cursor = cursor.left
                    else:
                        old_cursor = cursor
                        cursor = cursor.right
                if old_cursor.value > new_node.value:
                    new_node.parent = old_cursor
                    old_cursor.left = new_node
                else:
                    new_node.parent = old_cursor
                    old_cursor.right = new_node
            self.check_set.add(new_node.value)

    def contains(self, value):
        """Return a boolean if the node value is contained."""
        if value in self.check_set:
            return True
        return False

    def size(self):
        """Return the values in the tree."""
        return len(self.check_set)

    def depth(self):
        """Return the number of levels in the tree."""
        if not self.top:
            return 0
        return self.top.depth()

    def balance(self):
        """Return a value representing the right to left balance."""
        if not self.top:
            return 0
        return self.top.balance()

    def pre_order(self):
        """Return a generator of a pre-order traversal."""
        if self.top:
            for ii in self.top.pre_order():
                yield ii
        else:
            print('Empty Tree!')

    def in_order(self):
        """Return a generator of a in-order traversal."""
        if self.top:
            for ii in self.top.in_order():
                yield ii
        else:
            print('Empty Tree!')

    def post_order(self):
        """Return a generator of a post-order traversal."""
        if self.top:
            for ii in self.top.post_order():
                yield ii
        else:
            print('Empty Tree!')

    def breath_first(self):
        """
        Breadth First Traveral using a Deque as a queue.

        Is used as a generator.
        """
        d = deque([self.top])
        while d:
            vertex = d.popleft()
            yield vertex.value
            if vertex.left:
                d.append(vertex.left)
            if vertex.right:
                d.append(vertex.right)


# if __name__ == '__main__':
#     # b = BST()
#     b = BST([20])
#     b.insert(16)
#     b.insert(14)
#     b.insert(9)
#     b.insert(17)
#     b.insert(23)

#     # breath-first generator
#     # breath = b.breath_first()
#     # for ii in breath:
#     #     print(ii)

#     # pre-order generator
#     # pre = b.pre_order()
#     # for ii in pre:
#     #     print(ii)

#     # b = BST([20])
#     # b.contains(20)  # Best case this is an O(1)
#     # b.insert(19)
#     # b.insert(18)
#     # b.insert(17)
#     # b.insert(16)
#     # b.contains(16)  # Worst case this is also an O(1)
