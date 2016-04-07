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
