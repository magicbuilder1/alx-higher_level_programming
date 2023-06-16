#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    return (max(a_dictionary, key=a_dictionary.get))

=================================
11-mutiply_list_map.py

#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return (list(map((lambda i: i * number), my_list)))
