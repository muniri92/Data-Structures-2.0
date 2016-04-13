# -*- coding: utf-8 -*-
"""Test Binary Search Tree Module."""
import pytest


@pytest.fixture(scope='function')
def big_left():
    """Fixture for testing."""
    from bst import BST
    b = BST([20])
    b.insert(16.5)
    b.insert(14)
    b.insert(17.4)
    b.insert(14)
    b.insert(23)
    return b


def test_no_string():
    """Test that error is raise when anything other then an int is inserted."""
    from bst import BST
    b = BST([20])
    with pytest.raises(TypeError):
        b.insert("value")


def test_insert_top(big_left):
    """Test that insert works."""
    assert big_left.top.value == 20


def test_insert_left(big_left):
    """Test that insert smaller value goes left."""
    assert big_left.top.left.value == 16.5


def test_insert_right(big_left):
    """Test that insert right works correctly."""
    assert big_left.top.left.right.value == 17.4


def test_contains(big_left):
    """Test contains function."""
    assert big_left.contains(20) is True


def test_not_contained(big_left):
    """Test contains returns False when item not in list."""
    assert big_left.contains(89) is False


def test_size_empty():
    """Test size function works on an empty tree."""
    from bst import BST
    c = BST()
    assert c.size() == 0


def test_size_one():
    """Test size function works on a single Node Tree."""
    from bst import BST
    d = BST()
    d.insert(20)
    assert d.size() == 1


def test_size_many(big_left):
    """Test many and similar insert size."""
    assert big_left.size() == 5


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


def test_balance_left(big_left):
    """Test that a left side is larger and returns a positive int."""
    assert big_left.balance() > 0


def test_balance_right():
    """Test that a right side is larger and returns a negative int."""
    from bst import BST
    b = BST([20])
    b.insert(23)
    b.insert(22)
    assert b.balance() < 0
