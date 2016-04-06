# -*- coding: utf-8 -*-
"""Test Binary Search Tree Module."""
import pytest


HEAP_TEST = [3, 2, 4, 1, 5]

CONTAINS_TEST = [
    (1, True),
    (7, False),
    (3, True),
]


@pytest.mark.parametrize('value, result', CONTAINS_TEST)
def test_contains(value, result):
    """Test contain function in BST."""
    from bst import BST
    b = BST()
    b.heap = HEAP_TEST
    assert b.contains(value) == result
