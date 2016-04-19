# _*_ coding: utf-8 _*_
"""Insertion Sort Algorithm."""


class InsertionSort(object):
    """Insertion class."""

    def __init__(self, inital_list):
        """Initial."""
        self.inital_list = inital_list

    def insertion(self):
        """Insertion funtion."""
        try:
            lst = self.inital_list
            print(lst)
            for idx, val in enumerate(lst):
                future = lst[idx + 1]
                if future is not None:
                    # print('IDX: ' + str(idx))
                    # print('VAL: ' + str(val))
                    # print('FUTURE: ' + str(future))
                    # print(val)

                    while future <= val:
                        lst[idx], lst[idx + 1] = future, val
                        val = lst[idx]
                        future = lst[idx + 1]
                        break

        except IndexError:
            return lst

if __name__ == '__main__':
    i = InsertionSort([30, 20, 10, 0, 340, 320])
    print(i.insertion())
