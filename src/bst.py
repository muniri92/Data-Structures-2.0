# -*- coding: utf-8 -*-
"""Binary Search Tree Module."""


class BST(object):
    """Define Binart Search Tree class(BST)."""

    def __init__(self, value=[]):
        """Initialize BST class."""
        self.heap = []

    def contains(self, value):
        """Check to see if value is in heap."""
        for i in self.heap:
            if i == value:
                return True
        return False
