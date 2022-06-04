#!/usr/bin/pyhton3


def element_at(my_list, idx):
    """
    Gets an element in a list at a given index 
    And return it
    """
    if idx >= len(my_list) or idx < 0:
        return

    return (my_list[idx])
