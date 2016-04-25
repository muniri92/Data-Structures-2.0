# _*_ coding: utf-8 _*_
"""Test the quick sort algorithm."""

rand_lst = [25, 90, 53, 64, 68, 79, 45, 44, 66, 51, 73, 41, 21, 78,
            57, 22, 87, 26, 5, 69, 99, 56, 48, 7, 13, 47, 49, 75,
            43, 52, 6, 55, 9, 2, 23, 16, 85, 19, 62, 63, 3, 42, 70,
            30, 46, 72, 71, 20, 11, 81]


def test_random_lst():
    """Test that a random list is sorted."""
    from quick_sort import quick_sort
    lst_sort = sorted(rand_lst)
    assert quick_sort(rand_lst) == lst_sort


def test_stability():
    """Test the statbility of the quick sort."""
    from quick_sort import quick_sort
    lst = [(2, 'ab'), (1, 'ba'), (3, 'ab'), (2, 'ba'), (5, 'ab')]
    one = lst[0]
    two = lst[3]
    sort_lst = quick_sort(lst)
    assert sort_lst == [(1, 'ba'), (2, 'ab'), (2, 'ba'), (3, 'ab'), (5, 'ab')]
    assert sort_lst[1] is one
    assert sort_lst[2] is two


def test_quick_sort_empty():
    """Test that was can pass an empty list."""
    from quick_sort import quick_sort
    assert quick_sort([]) == []
