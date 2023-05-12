#!/usr/bin/python3

def element_at(my_list, idx):
    for i in my_list:
        if idx < 0 or idx > len(my_list):
            return None
        else:
            i = idx
    print(my_list[i])
