# _*_ coding: utf-8 _*_
"""Insertion Sort Algorithm."""
import time


def insertion(lst):
    """Insertion Sort Function."""
    for idx in range(1, len(lst)):
        val = lst[idx]
        cur_spot = idx
        while val <= lst[cur_spot - 1] and cur_spot > 0:
            lst[cur_spot] = lst[cur_spot - 1]
            cur_spot = cur_spot - 1
        lst[cur_spot] = val
    return lst


if __name__ == '__main__':
    """
    Worst case scenerio is that the list is backwards from largest to smallest.

    Best case scenerio for this algorithm is if the list is already sorted.
    """
    start_time = time.time()
    insertion([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0])
    print("TEST LIST: " + str([100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]))
    print("-- Worst Case: {} seconds --".format((time.time() - start_time)))
    print("**********************************************************")
    start_time = time.time()
    insertion([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
    print("TEST LIST: " + str([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]))
    print("-- Best Case: {} seconds --".format((time.time() - start_time)))
