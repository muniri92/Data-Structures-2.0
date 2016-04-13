# -*- coding: utf-8 -*-
"""Test Binary Search Tree Module."""
import pytest


@pytest.fixture(scope='function')
def big_left():
    """Fixture for testing."""
    from bst import BST
    b = BST([20])
    b.insert(16)
    b.insert(14)
    b.insert(17)
    b.insert(14)
    b.insert(23)
    return b


@pytest.fixture(scope='function')
def traversals():
    """Fixture for testing."""
    from bst import BST
    b = BST([20])
    b.insert(16)
    b.insert(25)
    b.insert(14)
    b.insert(17)
    b.insert(14)
    b.insert(22)
    b.insert(15)
    b.insert(4)
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
    assert big_left.top.left.value == 16


def test_insert_right(big_left):
    """Test that insert right works correctly."""
    assert big_left.top.left.right.value == 17


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


def test_depth_many():
    """Test that a node with one extra on the left has a depth of 2."""
    from bst import Node
    a = Node(20)
    a.left = Node(16)
    assert a.depth() == 2


def test_depth_tree(big_left):
    """Assert that a tree dpeth is three."""
    assert big_left.depth() == 3

# IN-ORDER TESTS


def test_in_order_empty():
    """Test an empty Node returns empty list."""
    from bst import BST
    b = BST()
    in_ord = b.in_order()
    in_ord_list = []
    for ii in in_ord:
        in_ord_list.append(ii)
    assert in_ord_list == []


def test_in_order_solo():
    """Test an empty Node returns empty list."""
    from bst import BST
    b = BST([20])
    in_ord = b.in_order()
    in_ord_list = []
    for ii in in_ord:
        in_ord_list.append(ii)
    assert in_ord_list == [20]


def test_in_order_filled(traversals):
    """Test an empty Node returns empty list."""
    b = traversals
    in_ord = b.in_order()
    in_ord_list = []
    for ii in in_ord:
        in_ord_list.append(ii)
    assert in_ord_list == [16, 14, 4, 15, 17, 20, 25, 22]


# PRE-ORDER TESTS

def test_pre_order_empty():
    """Test an empty Node returns empty list."""
    from bst import BST
    b = BST()
    pre_ord = b.pre_order()
    pre_ord_list = []
    for ii in pre_ord:
        pre_ord_list.append(ii)
    assert pre_ord_list == []


def test_pre_order_solo():
    """Test an empty Node returns empty list."""
    from bst import BST
    b = BST([132])
    pre_ord = b.pre_order()
    pre_ord_list = []
    for ii in pre_ord:
        pre_ord_list.append(ii)
    assert pre_ord_list == [132]


def test_pre_order_filled(traversals):
    """Test an empty Node returns empty list."""
    b = traversals
    pre_ord = b.pre_order()
    pre_ord_list = []
    for ii in pre_ord:
        pre_ord_list.append(ii)
    assert pre_ord_list == [20, 16, 14, 4, 15, 17, 25, 22]


# POST-ORDER TESTS

def test_post_order_empty():
    """Test an empty Node returns empty list."""
    from bst import BST
    b = BST()
    post_ord = b.post_order()
    post_ord_list = []
    for ii in post_ord:
        post_ord_list.append(ii)
    assert post_ord_list == []


def test_post_order_solo():
    """Test an empty Node returns empty list."""
    from bst import BST
    b = BST([35])
    post_ord = b.post_order()
    post_ord_list = []
    for ii in post_ord:
        post_ord_list.append(ii)
    assert post_ord_list == [35]


def test_post_order_filled(traversals):
    """Test an empty Node returns empty list."""
    b = traversals
    post_ord = b.post_order()
    post_ord_list = []
    for ii in post_ord:
        post_ord_list.append(ii)
    assert post_ord_list == [16, 14, 4, 15, 17, 25, 22, 20]


# BREATH-FIRST TEST

def test_breath_first_empty():
    """Test an empty Node returns empty list."""
    from bst import BST
    b = BST()
    breath = b.breath_first()
    breath_first_list = []
    for ii in breath:
        breath_first_list.append(ii)
    assert breath_first_list == []


def test_breath_first_solo():
    """Test an empty Node returns empty list."""
    from bst import BST
    b = BST([25])
    breath = b.breath_first()
    breath_first_list = []
    for ii in breath:
        breath_first_list.append(ii)
    assert breath_first_list == [25]


def test_breath_first_filled(traversals):
    """Test an empty Node returns empty list."""
    b = traversals
    breath = b.breath_first()
    breath_list = []
    for ii in breath:
        breath_list.append(ii)
    assert breath_list == [20, 16, 25, 14, 17, 22, 4, 15]


# delete tests

def test_delete_not_there(traversals):
    """Test the deletion of a node that not exist returns None."""
    outcome = traversals.delete(5)
    assert outcome is None


def test_delete_no_kids_there(traversals):
    """Test the deletion of a node that not exist returns None."""
    outcome = traversals.delete(4)
    assert outcome is None


def test_delete_no_kids_removed(traversals):
    """Test the deletion of a node that not exist returns None."""
    assert traversals.contains(4)
    traversals.delete(4)
    assert traversals.contains(4) is False


def test_delete_one_kids_there(traversals):
    """Test the deletion of a node that not exist returns None."""
    outcome = traversals.delete(14)
    assert outcome is None


def test_delete_one_kid_removed(traversals):
    """Test the deletion of a node that not exist returns None."""
    assert traversals.contains(14)
    traversals.delete(14)
    assert traversals.contains(14) is False


def test_delete_two_kids_there(traversals):
    """Test the deletion of a node that not exist returns None."""
    traversals.insert(16.5)
    outcome = traversals.delete(16)
    assert outcome is None


def test_delete_size_works(traversals):
    """Test the deletion of a node that not exist returns None."""
    traversals.insert(16.5)
    outcome = traversals.delete(16)
    assert outcome is None


def test_delete_two_kid_removed(traversals):
    """Test the deletion of a node that not exist returns None."""
    assert traversals.contains(16)
    traversals.insert(16.5)
    pre_delete = traversals.size()
    traversals.delete(16)
    assert pre_delete == (traversals.size() + 1)
