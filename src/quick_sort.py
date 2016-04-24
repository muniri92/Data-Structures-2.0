# _*_ coding: utf-8 _*_
"""Quick Sort Algorithm."""
import time


def quick_sort(lst):
    """Return the a sorted list using the Quick Sort Algorithm."""
    return _quick(lst, 0, len(lst) - 1)


def _quick(lst, begin, end):
    """Create the initial split and return the completed list."""
    if begin < end:
        split_point = _split(lst, begin, end)
        _quick(lst, begin, split_point - 1)
        _quick(lst, split_point + 1, end)
    return lst


def _split(lst, begin, end):
    """Use the pivot to start the paritioning."""
    right, left, pivot = end, begin + 1, lst[begin]
    while True:
        while lst[left] <= pivot and left <= right:
            left = left + 1
        while lst[right] >= pivot and right >= left:
            right = right - 1
        if left > right:
            break
        else:
            new_right = lst[left]
            lst[right], lst[left] = new_right, lst[right]
    new_right = lst[begin]
    lst[right], lst[begin] = new_right, lst[right]
    return right

if __name__ == '__main__':
    """
    This sort randomly shuffles the items in a list until the list is sorted.

    Best case scenerio for the merge sort is for very short lists.

    Worst case scenerio is that the list is extremely large.
    """
    start_time = time.time()
    print("TEST LIST: " + str([10, 2, 493, 23, 5, 3343, 23, .4]))
    print("-- Best Case: {} seconds --".format((time.time() - start_time)))
    print("***************************************************")
    start_time = time.time()
    rand_lst = [25, 90, 53, 64, 68, 79, 45, 44, 66, 51, 73, 41, 21, 78,
                57, 22, 87, 26, 5, 69, 99, 56, 48, 7, 13, 47, 49, 75,
                43, 52, 6, 55, 9, 2, 23, 16, 85, 19, 62, 63, 3, 42, 70,
                30, 46, 72, 71, 20, 11, 81]
    quick_sort(rand_lst)
    print("TEST LIST: [*random list of 5000 integers*]")
    print("-- Worst Case: {} seconds --".format((time.time() - start_time)))
