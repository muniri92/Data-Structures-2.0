# _*_ coding: utf-8 _*_
"""Merge Sort Algorithm."""
import time
import random


def merge_sort(lst):
    """An algorithm that sorts a list."""
    try:
        if len(lst) > 1:
            left, right = lst[:len(lst) // 2], lst[len(lst) // 2:]
            merge_sort(left)
            merge_sort(right)
            i, j, k = 0, 0, 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    i, lst[k] = i + 1, left[i]
                else:
                    j, lst[k] = j + 1, right[j]
                k = k + 1
            while i < len(left):
                lst[k] = left[i]
                k, i = k + 1, i + 1
            while j < len(right):
                lst[k] = right[j]
                j = j + 1
                k = k + 1
        return (lst)
    except TypeError:
        print("Only integers and/or floats.")

if __name__ == '__main__':
    """
    Best case scenerio for the merge sort is if the list is very short.

    Worst case scenerio is that the list is extremely large.
    """
    start_time = time.time()
    merge_sort([10, 2, 493, 23, 5, 3343, 23, .4])
    print("TEST LIST: " + str([10, 2, 493, 23, 5, 3343, 23, .4]))
    print("-- Best Case: {} seconds --".format((time.time() - start_time)))
    print("***************************************************")
    start_time = time.time()
    merge_sort([random.sample(range(100000), random.randrange(2, 1000)) for i in range(5000)])
    print("TEST LIST: [*random list of 5000 integers*]")
    print("-- Worst Case: {} seconds --".format((time.time() - start_time)))
