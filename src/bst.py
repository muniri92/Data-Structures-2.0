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

    def reset(self):
        """Reset class variables for testing."""
        self.check_set = set()
        self.top = None

    def __init__(self, values=[]):
        """Initialize BST class."""
        self.reset()
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
        if self.top is None:
            return 0
        elif self.top.left is None and self.top.right is None:
            return 1
        else:


# # -*- coding: utf-8 -*-
# """Binary Search Tree Module."""


# class Node(object):
#     """Define a node class."""

#     def __init__(self, value=None, parent=None, left=None, right=None):
#         """Initialize a Node object."""
#         self.value = value
#         self.parent = parent
#         self.left = left
#         self.right = right


# class BST(object):
#     """Define Binary Search Tree class(BST)."""

#     def reset(self):
#         """Reset class variables for testing."""
#         self.check_set = set()
#         self.top = None
#         self.right_level = 0
#         self.left_level = 0

#     def __init__(self, values=[]):
#         """Initialize BST class."""
#         self.reset()
#         if isinstance(values, list):
#             for value in values:
#                 self.insert(value)
#         else:
#             raise TypeError("Please package your item into a list!")

#     def insert(self, value):
#         """Insert a value into the binary heap."""
#         if value in self.check_set:
#             pass
#         else:
#             cursor = self.top
#             new_node = BST(value)
#             old_cursor = None
#             if self.top is None:
#                 self.top = new_node
#             else:
#                 while cursor is not None:
#                     if cursor.value > new_node.value:
#                         old_cursor = cursor
#                         cursor = cursor.left
#                     else:
#                         old_cursor = cursor
#                         cursor = cursor.right
#                 if old_cursor.value > new_node.value:
#                     new_node.parent = old_cursor
#                     old_cursor.left = new_node
#                 else:
#                     new_node.parent = old_cursor
#                     old_cursor.right = new_node
#             self.check_set.add(new_node.value)

#     def contains(self, value):
#         """Return a boolean if the node value is contained."""
#         if value in self.check_set:
#             return True
#         return False

#     def size(self):
#         """Return the values in the tree."""
#         print(self.check_set)
#         return len(self.check_set)

#     def depth(self):
#         """Return the number of levels in the tree."""
#         if self.top is None:
#             return 0
#         elif self.top.left is None and self.top.right is None:
#             return 1
#         # else:
#         #     left_depth = self.left.depth() if self.left is not None else 0
#         #     print(left_depth)
#         #     right_depth = self.right.depth() if self.right is not None else 0
#         #     print(right_depth)
#         #     return max(left_depth, right_depth) + 1


#         #     self.l_level = 1
#         #     to_search = [cursor]
#         #     seen = set()
#         #     while to_search:
#         #         if to_search[0].left is None and to_search[0].right is None:
#         #             l_level += 1
#         #             seen.add(to_search[0])
#         #             del to_search[0]
#         # if l_level > r_level:
#         #     return l_level
#         # return r_level

#     def balance(self):
#         """Return a value representing the right to left balance."""
#         print(self.l_level - self.r_level)
#         return self.l_level - self.r_level


# # if __name__ == '__main__':
# #     b = BST()
# #     b.insert(20)
# #     b.insert(16)
# #     b.insert(14)
# #     b.insert(17)
# #     b.insert(23)
# #     result = b.depth()
# #     nex = b.depth()
