# _*_ coding: utf-8 _*_
"""
Test the quick sort algorithm.

This algorithm is not stable, thus there are no stability tests.
"""

RAND_LST = [25, 90, 53, 64, 68, 79, 45, 44, 66, 51, 73, 41, 21, 78,
            57, 22, 87, 26, 5, 69, 99, 56, 48, 7, 13, 47, 49, 75,
            43, 52, 6, 55, 9, 2, 23, 16, 85, 19, 62, 63, 3, 42, 70,
            30, 46, 72, 71, 20, 11, 81]

RAND_LETTER = ['f', 'a', 'w', 't', 'p', 'b', 'e', 'c']

RAND_STR = ['hey', 'str', 'apple', 'sorted', 'words']

RAND_TUPLES = [(1,), (4,), (6,), (11,), (86,), (983,), (0,)]


def test_empty_lst():
    """Test that an empty lst returns an empty lst when sorted."""
    from quick_sort import quick_sort
    assert quick_sort([]) == []


def test_random_lst():
    """Test that a random list is sorted."""
    from quick_sort import quick_sort
    lst_sort = sorted(RAND_LST)
    assert quick_sort(RAND_LST) == lst_sort


def test_letters():
    """Test that a random list of letters can be sorted."""
    from quick_sort import quick_sort
    sorted_letters = sorted(RAND_LETTER)
    assert quick_sort(RAND_LETTER) == sorted_letters


def test_str():
    """Test that a random strings are sorted."""
    from quick_sort import quick_sort
    sorted_str = sorted(RAND_STR)
    assert quick_sort(RAND_STR) == sorted_str


def test_tuples():
    """Test that tuples are sorted."""
    from quick_sort import quick_sort
    sorted_tup = sorted(RAND_TUPLES)
    assert quick_sort(RAND_TUPLES) == sorted_tup
