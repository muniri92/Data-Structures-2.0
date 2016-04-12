# -*- coding: utf-8 -*-
"""Binary Search Tree Module."""
from collections import deque
import random
import io


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

    def _get_dot(self):
        """Recursively prepare a dot graph entry for this node."""
        if self.left is not None:
            yield "\t%s -> %s;" % (self.value, self.left.value)
            for i in self.left._get_dot():
                yield i
        elif self.right is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)
        if self.right is not None:
            yield "\t%s -> %s;" % (self.value, self.right.value)
            for i in self.right._get_dot():
                yield i
        elif self.left is not None:
            r = random.randint(0, 1e9)
            yield "\tnull%s [shape=point];" % r
            yield "\t%s -> null%s;" % (self.value, r)



class BST(object):
    """Define Binart Search Tree class(BST)."""

    def _reset(self):
        """Reset class variables for testing."""
        self.length = 0
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
            self.length += 1

    def contains(self, value):
        """Return a boolean if the node value is contained."""
        if self.top:
            cursor = self.top
            while cursor is not None:
                if value == cursor.value:
                    return True
                if cursor.value > value:
                    cursor = cursor.left
                else:
                    cursor = cursor.right
        return False

    def size(self):
        """Return the values in the tree."""
        return self.length

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
            if vertex:
                yield vertex.value
                if vertex.left:
                    d.append(vertex.left)
                if vertex.right:
                    d.append(vertex.right)

    def _no_children(self, delete_node):
        """Delete the desired node with no children and return None."""
        if delete_node.value > delete_node.parent.value:
            delete_node.parent.right = None
        else:
            delete_node.parent.left = None

    def _one_child(self, delete_node, child_direction):
        """Delete a node with one child and return None."""
        if child_direction == 'left':
            if delete_node.value < delete_node.parent.value:
                delete_node.parent.left = delete_node.left
                delete_node.left.parent = delete_node.parent
            else:
                delete_node.parent.left = delete_node.right
                delete_node.right.parent = delete_node.parent
        if child_direction == 'right':
            if delete_node.value > delete_node.parent.value:
                delete_node.parent.right = delete_node.right
                delete_node.right.parent = delete_node.parent
            else:
                delete_node.parent.right = delete_node.left
                delete_node.left.parent = delete_node.parent

    def _two_children(self, delete_node):
        """Delete a node with two children."""
        cursor = delete_node.right
        while cursor.left is not None:
            cursor = cursor.left
        delete_node.value = cursor.value
        if cursor.right:
            self._one_child(cursor, 'right')
        self._no_children(cursor)

    def delete(self, val):
        """Remove the value of choice from the BST."""
        if self.top:
            cursor = self.top
            while cursor is not None:
                if val == cursor.value:
                    if cursor.left and cursor.right:
                        self._two_children(cursor)
                    elif cursor.left:
                        self._one_child(cursor, 'left')
                    elif cursor.right:
                        self._one_child(cursor, 'right')
                    else:
                        self._no_children(cursor)
                    break
                if cursor.value > val:
                    cursor = cursor.left
                else:
                    cursor = cursor.right

    def write_graph(self):
        """Write dots to a file."""
        file = io.open('graph.gv', 'w')
        file.write(self.get_dot())
        file.close()
        print('graph.gv is update')

    def get_dot(self):
        """Return the tree with root 'self' as a dot graph."""
        return "digraph G{\n%s}" % ("" if self.top is None else (
            "\t%s;\n%s\n" % (
                self.top.value,
                "\n".join(self.top._get_dot())
            )
        ))


if __name__ == '__main__':
    b = BST([20])
    b.contains(20)  # Best case this is an O(n)
    b.insert(19)
    b.insert(18)
    b.insert(17)
    b.insert(16)
    b.insert(23)
    b.contains(16)  # Worst case this is also an O(n)
    b.write_graph()
