# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:35:54 2022

@author: hp
"""

list = [8, 2, 3, 0, 7]
sum = 0
for i in list:
    sum = i+sum
print(sum)

# 1)write a python function to sum all the numbers in a list
def sum(list):
    total = 0
    for i in list:
        total = i+total
    return total
print(sum([8, 2, 3, 0, 7]))


# 2) Write a function for below scenario.
# Param has 1000 rupess, ramu contains 5 chocolates, param give 500 rupees to ramu,
# ramu contains 10 chocolates, param give 700 rupees to ramu,
# ramu contains no chocolates param give 1000 rupees to ramu.
def param_gave(no_of_chocolates):
    if no_of_chocolates == 5:
        param_gave = 500
    elif no_of_chocolates == 10:
        param_gave  = 700
    elif no_of_chocolates ==0:
        param_gave = 1000
    return param_gave
print("Param gave to ramu Rs.",param_gave(5))
#param_gave(5)


# 3)Write a function for below scenario
# Big billon festival in amazon, bill amount on cloths more than 1000 rupess i will get 25% discount on bill.
# bill amount on cloths less than 500 rupess i will get 5% discount on bill.
# bill amount on cloths between 500  to 1000 rupess i will get 20% discount on bill.

def final_amount(bill_amount):
    if bill_amount >= 1000:
        discount = bill_amount*.25
        final_amount = (bill_amount-discount)
    elif bill_amount <= 500:
        discount = bill_amount*.05
        final_amount = (bill_amount-discount)
    elif bill_amount > 500 and bill_amount < 1000:
        discount = bill_amount*.20
        final_amount = (bill_amount-discount)
    return final_amount
final_amount(600)

# 4)Write a function for below scenario
# Big billon festival in amazon, the single formal shirt value is 1500,
# two shirts together buy(1+1 offer) shirts value is 1200
# bulk shirts together buy(1+2 offer) shirts vlaue is 1000


def final_amount(no_of_shirts):
    if no_of_shirts == 1:
        final_amount = 1500
    elif no_of_shirts == 2:
        final_amount = 1200
    elif no_of_shirts > 2:
        final_amount = 1000
    return final_amount
final_amount(3)


# 5).Write a function for below scenario
# Write a Python program to reverse a string.
def reverse(s):
    str = ""
    for i in s:
        str = i+str
    return str
s = "ramu"
print(reverse(s))


# 6)Write a Python function that takes a list and returns a new list with unique elements of the first list.
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

def unique_list(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x


print(unique_list([1, 2, 3, 3, 3, 3, 4, 5]))
