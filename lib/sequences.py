#!/usr/bin/env python3

def print_fibonacci(length):
    my_list = [0, 1]

    if(length == 0):
        my_list = []

    elif(length == 1):
        my_list = [0]

    elif(length > 2):
        while len(my_list) < length:
            my_list.append(my_list[-1] + my_list[-2])
    
    print(my_list)