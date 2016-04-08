# -*- coding: utf-8 -*-
"""Binary Search Tree Module."""


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

    def in_order(self):
        """Return a list of node values in order."""
        if self.value is None:
            return []
        elif self.left is None and self.right is None:
            return [self.value]
        else:
            pass

    def pre_order(self):
        """Return a list of node values in order."""
        if self.value is None:
            return []
        elif self.left is None and self.right is None:
            return [self.value]
        else:
            pass

    def post_order(self):
        """Return a list of node values in order."""
        if self.value is None:
            return []
        elif self.left is None and self.right is None:
            return [self.value]
        else:
            pass

    def breath_first(self):
        """Return a list of node values in order."""
        if self.value is None:
            return []
        elif self.left is None and self.right is None:
            return [self.value]
        else:
            pass


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
            for value in values:
                self.insert(value)
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

    def in_order(self):
        """Return a list that is in value order min to max."""
        if not self.top:
            return []
        return self.top.in_order()

    def post_order(self):
        """Return a list that is in value max to min."""
        if not self.top:
            return []
        return self.top.post_order()

    def pre_order(self):
        """Return a list that orders left to right."""
        if not self.top:
            return []
        return self.top.pre_order()

    def breath_first(self):
        """Return a list left to right root to tips."""
        if not self.top:
            return []
        return self.top.breath_first()


if __name__ == '__main__':
    b = BST([20])
    b.contains(20)  # Best case this is an O(1)
    b.insert(19)
    b.insert(18)
    b.insert(17)
    b.insert(16)
    b.contains(16)  # Worst case this is also an O(1)
