#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DoublingArray 
September 20, 2020
CS 5012 Group Project, Module 2

by Rowan Rice, Amanda West, Hannah Fredrick, Nikki Aaron, Bev Dobrenz

This file illustrates the doubling-array algorithm.  The algorithm can be summed
up as such: enter items into a list until the list has no more room, at which 
point double the size of the list to continue adding items.

This file was developed as a demonstration of an algorithm that can be 
explained by amortized analysis as per the assignment.

"""


import numpy as np

## this function is the driver of the program
## it asks the user for input to build a list
def run_program():
    
    x = 0 ## variable that holds the user's input
    listA = np.empty(shape = 1, dtype = int) ## start with an empty array, size 1
    i = 0 ## keeps track of the index of the list in which x is being entered
    
    ## this is the loop that asks the user continuously for a value to add
    ## to the list.  when the user enters -1, the loop will stop and the 
    ## user will be shown the final list
    while (x != -1):
        ## ask for input
        x = int(input("Give me a non-zero positive integer to add to your list" +
                  " (enter -1 to exit): "))
        
        ## if the user stops the program before anything is added to the list,
        ## end the program and tell the user the list is empty
        if(x == -1) and (i == 0):
            print("Thanks for playing! Your list is empty.")
            break
        
        ## if at any point the user stops the program after items are already
        ## added to the list, end the program and print the final list
        elif (x == -1):
            print("Thanks for playing! Here is your final list: ", listA[0:i])
            break
        
        ## if the user enters a negative number, catch the error and correct
        ## the user to enter positive integers only
        elif(x <= 0):
            print("Try again! Non-negative numbers only.")
        
        ## when the user enters a positive integer to add to the list, call
        ## the helper function resize_list to make sure the integer is being
        ## added to the list correctly 
        else:
            listA = resize_list(i, x, listA)
            i += 1 ## increase the index counter by one for the next round


## this is a helper function that puts the user's item into the list correctly
## by following the below steps:
## if this is the very first item being added to the list, put it in index 0
## if the list is full, double the size of the array and add the user's item
## at the correct index
## if the list is not full, add the user's item at the correct index
## this function RETURNS a list
def resize_list(i, x, listA):
    
    length = len(listA)  
    
    ## enter first element into the list
    if (i == 0):
        listA[0] = x
        print("\nGreat! Here is your list: ", listA)
        print("Number of elements in list = " + (str(i+1)))
        print("Length of list = " + str(len(listA)))
        return listA
    
    ## if the array is too small and there is no more room to add another item, 
    ## then create a new array with double the size and copy over the original
    ## array's items. then add the user's item x
    elif (i > (length - 1)):
        
        ## new array with double the size
        listB = np.empty(shape = (length * 2), dtype = int)
        
        ## copy over old array
        j = 0
        while (j < i):
            listB[j] = listA[j]
            j += 1
            
        ## add in user's item    
        listB[i] = x
        
        print("\nGreat! Here is your list: ", listB[0:i+1])
        print("Number of elements in list = " + (str(i+1)))
        print("Length of list = " + str(len(listB)))
        return listB
    
    ## if there is enough room in the array for another item, add it
    elif (i < length):
        ## add in user's item
        listA[i] = x
        
        print("\nGreat! Here is your list: ", listA[0:i+1])
        print("Number of elements in list = " + (str(i+1)))
        print("Length of list = " + str(len(listA)))
        return listA
        
############# 

## main intro to the user:
            
print("\nThis program will ask you for a non-zero positive integer to add" + 
      " to your list until you exit the program.")

run_program() ## runs the program until the user stops it