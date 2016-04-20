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


def test_insertion_solo():
    """Test the you can insert a single item list."""
    from insertion_sort import InsertionSort
    i = InsertionSort()
    assert i.insertion([20]) == [20]


# I WANT 1,000,000 TESTS!
# @pytest.fixture(scope='function', params=RANDOM_LIST)
# def unord_lst(request):
#     """Test random list and confirm that we get them back sorted."""
#     lst = []
#     i = lst[(request.param)]
#     # i.insertion(request.param)
#     # import pdb; pdb.set_trace()
#     return i


# def test_rando(unord_lst):
#     from insertion_sort import InsertionSort
#     i = InsertionSort()
#     lst = unord_lst
#     print(lst)
#     i.insertion(unord_lst)
