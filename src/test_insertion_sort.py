# _*_ coding: utf-8 _*_
"""Test the insertion sort algorithm."""
import pytest
import random

RANDOM_LIST = [random.sample(range(1000),
               random.randrange(2, 100)) for i in range(500)]


def test_random_lst():
    """A."""
    from insertion_sort import InsertionSort
    i = InsertionSort()
    for lst in RANDOM_LIST:
        lst_sort = sorted(lst)
        assert i.insertion(lst) == lst_sort


def test_insertion_empty():
    """Test that was can pass an empty list."""
    from insertion_sort import InsertionSort
    i = InsertionSort()
    assert i.insertion([]) == []


def test_error_string():
    """Test to see that error is raised when string is passed."""
    from insertion_sort import InsertionSort
    i = InsertionSort()
    with pytest.raises(TypeError):
        i.insertion([10, 20, "hey", 20])


def test_error_list():
    """Test to see that error is raised when list is passed."""
    from insertion_sort import InsertionSort
    i = InsertionSort()
    with pytest.raises(TypeError):
        i.insertion([10, 20, [], 20])


def test_error_tuple():
    """Test to see that error is raised when tuple is passed."""
    from insertion_sort import InsertionSort
    i = InsertionSort()
    with pytest.raises(TypeError):
        i.insertion([10, 20, ("hey", "fail"), 20])


def test_error_dict():
    """Test to see that error is raised when dict is passed."""
    from insertion_sort import InsertionSort
    i = InsertionSort()
    with pytest.raises(TypeError):
        i.insertion([10, 20, {"hey": "fail"}, 20])
