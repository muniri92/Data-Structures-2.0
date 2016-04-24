# -*- coding:utf-8 -*-
"""Radix module sort."""
import time


def radix_sort(lst):
    """Sort via radix sorting."""
    try:
        maxlength = False
        tmp, place = 0, 1
        while not maxlength:
            maxlength = True
            buckets = [[] for x in range(10)]
            for i in lst:
                tmp = i // place
                buckets[tmp % 10].append(i)
                if maxlength and tmp > 0:
                    maxlength = False
            new_index = 0
            for index in range(10):
                bucket = buckets[index]
                for i in bucket:
                    lst[new_index] = i
                    new_index += 1
            place *= 10
        return lst
    except TypeError:
        raise TypeError("List must be composed of ints.")

if __name__ == '__main__':
    """
    Worst case scenerio is that the list is backwards from largest to smallest.

    Best case scenerio for this algorithm is if the list is already sorted.
    """
    start_time = time.time()
    radix_sort([29850283765, 13820, 4, 20982340986091283058, 72639287])
    print("TEST LIST: " + str([29850283765, 13820, 4, 20982340986091283058, 72639287]))
    print("-- Worst Case: {} seconds --".format((time.time() - start_time)))
    print("**********************************************************")
    start_time = time.time()
    radix_sort([2, 0, 8])
    print("TEST LIST: " + str([2, 0, 8]))
    print("-- Best Case: {} seconds --".format((time.time() - start_time)))