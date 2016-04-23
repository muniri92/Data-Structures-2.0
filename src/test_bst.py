# -*- coding: utf-8 -*-
"""Test Binary Search Tree Module."""
import pytest
import random
import math


RANDOM_LIST = [random.sample(range(1000), random.randrange(2, 100)) for i in range(500)]

EDGE_CASES = [
    [20],
    [9, 20],
    [20, 9],
    [0, 1, 2],
    [2, 1, 0],
    [2, 0, 1],
    [0, 2, 1],
    [1, 2, 0],
    [1, 0, 2]
]


@pytest.fixture(scope='function', params=EDGE_CASES + RANDOM_LIST)
def trees(request):
    """Test edge cases for balancing. Returns random lists of varies sizes."""
    from bst import BST
    b = BST(request.param)
    return (b, request.param[0])


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
    """Fixture for testing the traversals."""
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


def test_level_given_length(trees):
    """
    Test that determines the depth of a tree given the number of nodes.

    We know: depth = ∑ 2^(i), from i=0 to n=(number of nodes)
    Equation: k = log(n + 1) , where k=depth and n=(number of nodes)

    It's important to remember that this equation is for perfectly balanced
    trees, so we are confirming that the level falls in between -2 and +2
    from the aprroximated level.
    """
    level = trees[0].depth()
    length = trees[0].size()
    equation = math.log(((int(length) + 1)), 2)
    assert (level - 2) <= math.ceil(equation) <= (level + 2)


def test_tree_one_balance_tree(trees):
    """Test tree balance is properly operating over many insertions."""
    assert -2 < trees[0].balance() < 2


def test_tree_one_balance_tree_deletion(trees):
    """Test tree balance is properly operating over many insertions."""
    trees[0].delete(trees[1])
    assert -2 < trees[0].balance() < 2


def test_no_string():
    """Test that error is raise when anything other then an int is inserted."""
    from bst import BST
    b = BST([20])
    with pytest.raises(TypeError):
        b.insert("value")


def test_insert(trees):
    """Test the insert function."""
    breath_ord = trees[0].breath_first()
    ord_list = []
    for val in breath_ord:
        ord_list.append(val)
    try:
        assert trees[0].top.value == ord_list[0]
        assert trees[0].size() == len(ord_list)
    except AttributeError:
        pass


def test_contains(trees):
    """Test the contains function."""
    breath_ord = trees[0].breath_first()
    ord_list = []
    for val in breath_ord:
        ord_list.append(val)
    try:
        assert trees[0].contains(random.choice(ord_list)) is True
    except IndexError:
        pass


def test_not_contained(trees):
    """Test contains returns False when item not in list."""
    assert trees[0].contains(-89) is False


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


def test_size_many(trees):
    """Test many and similar insert size."""
    breath_ord = trees[0].breath_first()
    ord_list = []
    for val in breath_ord:
        ord_list.append(val)
    try:
        assert trees[0].size() == len(ord_list)
    except IndexError:
        pass


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
    from bst import Node
    a = Node(20)
    a.left = Node(18)
    assert a.balance() == 1


def test_balance_right():
    """Test that a right side is larger and returns a negative int."""
    from bst import Node
    a = Node(20)
    a.right = Node(23)
    assert a.balance() == -1


def test_depth_many():
    """Test that a node with one extra on the left has a depth of 2."""
    from bst import Node
    a = Node(20)
    a.left = Node(16)
    assert a.depth() == 2


def test_size_empty_tree():
    """Assert an empty tree has a size of zero."""
    from bst import BST
    b = BST([])
    assert b.size() == 0


def test_size_empty_depth():
    """Assert an empty tree has a depth of zero."""
    from bst import BST
    b = BST([])
    assert b.depth() == 0


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
    """Test running in-order on a tree with one Node."""
    from bst import BST
    b = BST([20])
    in_ord = b.in_order()
    in_ord_list = []
    for ii in in_ord:
        in_ord_list.append(ii)
    assert in_ord_list == [20]


def test_in_order_filled(traversals):
    """Test that in-order returns the correct list."""
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
    """Test running pre-order on a tree with one Node."""
    from bst import BST
    b = BST([132])
    pre_ord = b.pre_order()
    pre_ord_list = []
    for ii in pre_ord:
        pre_ord_list.append(ii)
    assert pre_ord_list == [132]


def test_pre_order_filled(traversals):
    """Test that pre-order returns the correct list."""
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
    """Test running post-order on a tree with one Node."""
    from bst import BST
    b = BST([35])
    post_ord = b.post_order()
    post_ord_list = []
    for ii in post_ord:
        post_ord_list.append(ii)
    assert post_ord_list == [35]


def test_post_order_filled(traversals):
    """Test that post-order returns the correct list."""
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
    """Test running breath on a tree with one Node."""
    from bst import BST
    b = BST([25])
    breath = b.breath_first()
    breath_first_list = []
    for ii in breath:
        breath_first_list.append(ii)
    assert breath_first_list == [25]


def test_breath_first_filled(traversals):
    """Test that breath returns the correct list."""
    b = traversals
    breath = b.breath_first()
    breath_list = []
    for ii in breath:
        breath_list.append(ii)
    assert breath_list == [20, 16, 25, 14, 17, 22, 4, 15]


# DELETE TEST

def test_delete_no_kids(traversals):
    """Test the deletion of a node with no children are no longer contained."""
    assert traversals.contains(4) is True
    traversals.delete(4)
    assert traversals.contains(4) is False


def test_delete_no_kid_size(traversals):
    """Test deleting a node with no childern will return the correct size."""
    assert traversals.contains(4) is True
    pre_delete = traversals.size()
    traversals.delete(4)
    post_delete = traversals.size()
    assert post_delete == (pre_delete - 1)


def test_delete_one_kid(traversals):
    """Test the deletion of a node with 1 children are no longer contained."""
    assert traversals.contains(16) is True
    traversals.delete(16)
    assert traversals.contains(16) is False


def test_delete_one_kid_size(traversals):
    """Test deleting a node with 1 child will return the correct size."""
    assert traversals.contains(16) is True
    pre_delete = traversals.size()
    traversals.delete(16)
    post_delete = traversals.size()
    assert post_delete == (pre_delete - 1)


def test_delete_two_kids(traversals):
    """Test the deletion of a node with 2 children are no longer contained."""
    assert traversals.contains(14) is True
    traversals.delete(14)
    assert traversals.contains(14) is False


def test_delete_two_kid_size(traversals):
    """Test deleting a node with 2 child will return the correct size."""
    assert traversals.contains(14) is True
    pre_delete = traversals.size()
    traversals.delete(14)
    post_delete = traversals.size()
    assert post_delete == (pre_delete - 1)

def test_delete_head_only():
    """Test deleteing a one node head."""
    from bst import BST
    b = BST([20])
    assert b.contains(20) is True
    b.delete(20)
    assert b.contains(20) is False


def test_delete_head_one_left_child():
    """Test deleting a head with one left child."""
    from bst import BST
    b = BST([20])
    b.insert(18)
    assert b.contains(20) is True
    b.delete(20)
    assert b.contains(20) is False
    assert b.top.value == 18


def test_delete_head_one_right_child():
    """Test deleting a head with one right child."""
    from bst import BST
    b = BST([20])
    b.insert(22)
    assert b.contains(20) is True
    b.delete(20)
    assert b.contains(20) is False
    assert b.top.value == 22


def test_delete_head_two_children():
    """Test deleting a head with two children."""
    from bst import BST
    b = BST([20])
    b.insert(18)
    b.insert(22)
    assert b.contains(20) is True
    b.delete(20)
    assert b.contains(20) is False
    assert b.top.value == 22
    assert b.top.left.value == 18
    assert b.top.right is None
