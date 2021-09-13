#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)

    legnth = len(my_list) - 1
    if idx > legnth:
        return (None)

    return (my_list[idx])
