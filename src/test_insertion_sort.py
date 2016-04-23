# _*_ coding: utf-8 _*_
"""Test the insertion sort algorithm."""
import random

RANDOM_LIST = [random.sample(range(1000),
               random.randrange(2, 100)) for i in range(500)]


def test_random_lst():
    """A."""
    from insertion_sort import insertion
    for lst in RANDOM_LIST:
        lst_sort = sorted(lst)
        assert insertion(lst) == lst_sort


def test_random_sames():
    """A."""
    from insertion_sort import insertion
    assert insertion([2, 2, 2, 1]) == [1, 2, 2, 2]


def test_stability():
    """A."""
    from insertion_sort import insertion
    lst = [(2, 'ab'), (1, 'ba'), (3, 'ab'), (2, 'ba'), (5, 'ab')]
    one = lst[0]
    two = lst[3]
    sort_lst = insertion(lst)
    assert sort_lst == [(1, 'ba'), (2, 'ab'), (2, 'ba'), (3, 'ab'), (5, 'ab')]
    assert sort_lst[1] is one
    assert sort_lst[2] is two


def test_insertion_empty():
    """Test that was can pass an empty list."""
    from insertion_sort import insertion
    assert insertion([]) == []
