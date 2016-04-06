# -*- coding: utf-8 -*-
"""Binary Search Tree Module."""


class Node(object):
    """Define a node class."""

    def __init__(self, value, parent=None, left=None, right=None):
        """Initialize a Node object."""
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right


class BST(object):
    """Define Binart Search Tree class(BST)."""

    top = None

    def __init__(self, values):
        """Initialize BST class."""
        if isinstance(values, list):
            for value in values:
                self.insert(value)
        else:
            raise TypeError("Please package your item into a list!")

    def insert(self, value):
        """Insert a value into the binary heap."""
        # if self.contains(value):
        #     break
        # else:
        cursor = self.top
        new_node = Node(value)
        if self.top is None:
            self.top = new_node
        else:
            while cursor is not None:
                if cursor.value > new_node.value:
                    old_cursor = cursor
                    cursor = cursor.left
            new_node.parent = old_cursor
            old_cursor.left = new_node
