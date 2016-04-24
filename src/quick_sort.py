# _*_ coding: utf-8 _*_
"""Quick Sort Algorithm."""
import time
import random


def quick_sort(lst):
    """Split the lists."""
    if len(lst) < 1:
        split_point = _split(lst, 0, len(lst) - 1)
        quick_sort(lst, 0, split_point - 1)
        quick_sort(lst, split_point + 1, len(lst) - 1)


def _split(lst, begin, end):
    """Use the pivot to start the paritioning."""
    right, left, pivot = end, begin + 1, lst[begin]
    while True:
        while lst[left] < pivot and left < right:
            left = left + 1
        while lst[right] > pivot and right > left:
            right = right - 1
        if left > right:
            break
        else:
            lst[right], lst[left], new_right = new_right, lst[right], lst[left]
    lst[right], lst[begin], new_right = new_right, lst[right], lst[begin]
    return right


if __name__ == '__main__':
    """
    The bogosort randomly shuffles the items in a list until the list is sorted.

    Best case scenerio for the merge sort is for very short lists.

    Worst case scenerio is that the list is extremely large.
    """
    start_time = time.time()
    quick_sort([30, 25, 42, 0, 3])
    print("TEST LIST: " + str([10, 2, 493, 23, 5, 3343, 23, .4]))
    print("-- Best Case: {} seconds --".format((time.time() - start_time)))
    print("***************************************************")
    start_time = time.time()
    quick_sort([random.sample(range(100000), random.randrange(2, 1000)) for i in range(5000)])
    print("TEST LIST: [*random list of 5000 integers*]")
    print("-- Worst Case: {} seconds --".format((time.time() - start_time)))

