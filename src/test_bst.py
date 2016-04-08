# -*- coding: utf-8 -*-
"""Test Binary Search Tree Module."""
import pytest


def test_insert_left():
    """Test that insert works."""
    from bst import BST
    b = BST([20])
    b.insert(16)
    b.insert(14)
    b.insert(17)
    b.insert(23)
    assert b.top.value == 20
    assert b.top.left.value == 16
    assert b.top.left.right.value == 17
    assert b.top.left.left.value == 14
    assert b.top.right.value == 23


def test_contains():
    """Test contains function."""
    from bst import BST
    b = BST([20])
    b.insert(16)
    b.insert(14)
    b.insert(17)
    b.insert(23)
    assert b.contains(20) is True
    assert b.contains(89) is False


def test_size_empty():
    """Test size function works."""
    from bst import BST
    c = BST()
    assert c.size() == 0


def test_size_one():
    """Test size function works."""
    from bst import BST
    d = BST()
    d.insert(20)
    assert d.size() == 1


def test_size_many():
    """Test many and similar insert size."""
    from bst import BST
    b = BST([20])
    b.insert(16)
    b.insert(14)
    b.insert(17)
    b.insert(14)
    b.insert(23)
    assert b.size() == 5


def test_depth_none():
    """Test that a node of nothing returns a value of nothing."""
    from bst import Node
    a = Node()
    assert a.depth() == 0


def test_depth_one():
    """Test that a node of one returns a depth of one."""
    from bst import Node
    a = Node(1)
    assert a.depth() == 1


def test_balance_none():
    """Test that a node of nothing returns a value of nothing."""
    from bst import Node
    a = Node()
    assert a.balance() == 0


def test_balance_one():
    """Test that a node of one returns a depth of one."""
    from bst import Node
    a = Node(1)
    assert a.balance() == 0


def test_balance_left():
    """Test that a left side is larger and returns a positive int."""
    from bst import BST
    b = BST([20])
    b.insert(16)
    b.insert(14)
    b.insert(17)
    b.insert(14)
    b.insert(23)
    assert b.balance() > 0


def test_balance_right():
    """Test that a right side is larger and returns a negative int."""
    from bst import BST
    b = BST([20])
    b.insert(23)
    b.insert(22)
    assert b.balance() < 0


def test_depth_many():
    """Test that a node with one extra on the left has a depth of 2."""
    from bst import Node
    a = Node(20)
    a.left = Node(16)
    assert a.depth() == 2

def test_depth_tree():
    from bst import BST
    b = BST([20])
    b.insert(16)
    b.insert(14)
    b.insert(17)
    b.insert(14)
    b.insert(23)
    assert b.depth() == 3