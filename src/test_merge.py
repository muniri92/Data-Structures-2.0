# _*_ coding: utf-8 _*_
"""Test the merge sort algorithm."""
import random


RANDOM_LIST = [random.sample(range(1000),
               random.randrange(2, 100)) for i in range(500)]


def test_random_lst():
    """A."""
    from merge_sort import merge_sort
    for lst in RANDOM_LIST:
        lst_sort = sorted(lst)
        assert merge_sort(lst) == lst_sort


def test_random_sames():
    """A."""
    from merge_sort import merge_sort
    assert merge_sort([2, 2, 2, 1]) == [1, 2, 2, 2]


def test_stability():
    """A."""
    from merge_sort import merge_sort
    lst = [(2, 'ab'), (1, 'ba'), (3, 'ab'), (2, 'ba'), (5, 'ab')]
    one = lst[0]
    two = lst[3]
    sort_lst = merge_sort(lst)
    assert sort_lst == [(1, 'ba'), (2, 'ab'), (2, 'ba'), (3, 'ab'), (5, 'ab')]
    assert sort_lst[1] is one
    assert sort_lst[2] is two


def test_merge_sort_empty():
    """Test that was can pass an empty list."""
    from merge_sort import merge_sort
    assert merge_sort([]) == []
