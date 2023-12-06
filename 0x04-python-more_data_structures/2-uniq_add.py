#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_set = set()
    sum = 0
    for element in my_list:
        if isinstance(element, int):
            if element not in uniq_set:
                uniq_set.add(element)
                sum += element
    return sum
