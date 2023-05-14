#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list

    tmp = []
    tmp.extend(my_list)

    for i in tmp:
        i = idx
        tmp[i] = element
    return tmp
