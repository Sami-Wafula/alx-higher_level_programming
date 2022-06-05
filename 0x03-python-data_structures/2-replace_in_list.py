#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = len(my_list)
    if 0 <= idx < i - 1:
        my_list[idx] = element
    return (my_list)
