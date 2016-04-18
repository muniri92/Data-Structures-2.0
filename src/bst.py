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

    def balance_tree(self):
        """Balance the tree to optimal structure and minimize O(n) calls."""
        while self:
            if self.balance() > 1:
                b, c = self, self.left
                if c.balance() > 0:
                    b._rotate_right()
                elif c.balance() < 0:
                    b._pull_left()
                    b.balance_tree()
                else:
                    b._rotate_right()
            elif self.balance() < -1:
                b, c = self, self.right
                if c.balance() < 0:
                    b._rotate_left()
                elif c.balance() > 0:
                    b._pull_right()
                    b.balance_tree()
                else:
                    b._rotate_left()
            cursor = self
            self = self.parent
        return cursor

    def _pull_left(self):
        """Pull the node balance to load left side strong."""
        c = self.left
        if c.left is None:
            c.value, c.right.value = c.right.value, c.value
            c.left, c.right = c.right, None
        else:
            c._rotate_left()

    def _pull_right(self):
        """Pull the node balance to load left side strong."""
        c = self.right
        if c.right is None:
            c.value, c.left.value = c.left.value, c.value
            c.right, c.left = c.left, None
        else:
            c._rotate_right()

    def _rotate_right(self):
        """Rotate self around right to rebalance."""
        a, b, c = self.parent, self, self.left
        if a is None:
            try:
                c.parent, b.parent = a, c
                b.left, c.right.parent, c.right = c.right, b, b
            except AttributeError:
                c.parent, b.parent = a, c
                b.left, c.right = c.right, b
        else:
            try:
                if a.value > b.value:
                    c.parent, b.parent, a.left = a, c, c
                    b.left, c.right.parent, c.right = c.right, b, b
                else:
                    c.parent, b.parent, a.right = a, c, c
                    b.left, c.right.parent, c.right = c.right, b, b
            except AttributeError:
                if a.value > b.value:
                    c.parent, b.parent, a.left = a, c, c
                    b.left, c.right = c.right, b
                else:
                    c.parent, b.parent, a.right = a, c, c
                    b.left, c.right = c.right, b

    def _rotate_left(self):
        """Rotate self around left to rebalance."""
        a, b, c = self.parent, self, self.right
        if a is None:
            try:
                c.parent, b.parent = a, c
                b.right, c.left.parent, c.left = c.left, b, b
            except AttributeError:
                c.parent, b.parent = a, c
                b.right, c.left = c.left, b
        else:
            try:
                if a.value < b.value:
                    c.parent, b.parent, a.right = a, c, c
                    b.right, c.left.parent, c.left = c.left, b, b
                else:
                    c.parent, b.parent, a.left = a, c, c
                    b.right, c.left.parent, c.left = c.left, b, b
            except AttributeError:
                if a.value < b.value:
                    c.parent, b.parent, a.right = a, c, c
                    b.right, c.left = c.left, b
                else:
                    c.parent, b.parent, a.left = a, c, c
                    b.right, c.left = c.left, b

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
            for value in values:
                self.insert(value)
        else:
            raise TypeError("Please package your item into a list!")

    def insert(self, value):
        """Insert a value into the binary heap."""
        try:
            float(value)
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
                    self.top = old_cursor.balance_tree()
                self.length += 1
        except (ValueError, AttributeError):
            raise TypeError("This tree only accepts integers or floats.")

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
        if delete_node.parent is not None:
            if delete_node.value > delete_node.parent.value:
                delete_node.parent.right = None
            else:
                delete_node.parent.left = None
        else:
            self.top = delete_node = None

    def _one_child(self, delete_node, child_direction):
        """Delete a node with one child and return None."""
        if delete_node.parent:
            if child_direction == 'left':
                if delete_node.value < delete_node.parent.value:
                    delete_node.parent.left = delete_node.left
                    delete_node.left.parent = delete_node.parent
                else:
                    delete_node.parent.right = delete_node.left
                    delete_node.left.parent = delete_node.parent
            else:
                if delete_node.value > delete_node.parent.value:
                    delete_node.parent.right = delete_node.right
                    delete_node.right.parent = delete_node.parent
                else:
                    delete_node.parent.left = delete_node.right
                    delete_node.right.parent = delete_node.parent
        else:
            if child_direction == 'left':
                    delete_node.left.parent = None
                    self.top = delete_node.left
            else:
                    delete_node.right.parent = None
                    self.top = delete_node.right

    def _two_children(self, del_node):
        """Delete a node with two children."""
        cursor = del_node.right
        while cursor.left is not None:
            cursor = cursor.left
        del_node.value, cursor.value = cursor.value, cursor.value + del_node.value
        cursor = del_node.right
        while cursor.left is not None:
            cursor = cursor.left
        if cursor.right:
            self._one_child(cursor, 'right')
        else:
            self._no_children(cursor)

    def delete(self, val):
        """Remove the value of choice from the BST."""
        if self.top:
            cursor = self.top
            while cursor is not None:
                if val == cursor.value:
                    self.length -= 1
                    if cursor.left and cursor.right:
                        self._two_children(cursor)
                        if cursor.parent is None:
                            cursor.balance_tree()
                    elif cursor.left:
                        self._one_child(cursor, 'left')
                    elif cursor.right:
                        self._one_child(cursor, 'right')
                    else:
                        self._no_children(cursor)
                    if cursor.parent is not None:
                        self.top = cursor.parent.balance_tree()
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
    list_ = [991, 482, 206, 326, 66, 859, 193, 10, 323]
    b = BST()
    for value in list_:
        b.insert(value)
    b.delete(713)
    b.write_graph()
