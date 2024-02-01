#!/usr/bin/python3
def best_score(a_dictionary):
    if key not in a_dictionary:
        return None
    best_key = None
    best_value = 0
    for key, value in a_dictionary.item():
        if value > best_value:
            best_value = value
            best_key = best_value
    return best_key
