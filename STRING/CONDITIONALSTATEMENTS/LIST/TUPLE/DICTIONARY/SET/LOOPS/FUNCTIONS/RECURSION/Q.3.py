#Write a recursive function to print all elements in a list
def print_list(list, idx=0):

    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["mango","litchi","apple","bannana"]
print_list(fruits)

