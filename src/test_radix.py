# _*_ coding: utf-8 _*_
"""Test the radix sort algorithm."""
import random
import pytest

RANDOM_LIST = [random.sample(range(1000),
               random.randrange(2, 100)) for i in range(500)]


@pytest.fixture(scope='function', params=RANDOM_LIST)
def lists(request):
    """Fixture of many random lists of varies sizes."""
    # import pdb; pdb.set_trace()
    b = []
    b.append(request.param)
    return b


def test_random_lst(lists):
    """Asser the radix sort works on multiple lists of various sizes."""
    from radix import radix_sort
    for lst in lists:
        lst_sort = sorted(lst)
        assert radix_sort(lst) == lst_sort


def test_random_sames():
    """Assert same numbers can sort."""
    from radix import radix_sort
    assert radix_sort([2, 2, 2, 1]) == [1, 2, 2, 2]


def test_floats():
    """Error raised with floats."""
    from radix import radix_sort
    with pytest.raises(TypeError):
        radix_sort([2.3, 2.8, 2.3, 1])


def test_string():
    """Error raised with strings."""
    from radix import radix_sort
    with pytest.raises(TypeError):
        radix_sort(["hello", 2, 3, 1])


def test_tuple():
    """Error raised with tuples."""
    from radix import radix_sort
    with pytest.raises(TypeError):
        radix_sort([(4, 7), 2, 3, 1])


def test_radix_sort_empty():
    """Test that was can pass an empty list."""
    from radix import radix_sort
    assert radix_sort([]) == []
