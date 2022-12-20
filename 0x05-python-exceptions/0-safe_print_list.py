#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    total = 0
    for i in range(x):
        try:
            print(my_list[x])
            total += 1
            return total
        except IndexError:
            print("Index is out of bounds")

