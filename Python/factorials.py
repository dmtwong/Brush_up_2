# -*- coding: utf-8 -*-
"""
Created on Mon May 27 12:40:40 2024

@author: USER
"""

# Practice various way to compute factorial

count_iter = 0
def fact_iter(i):
    global count_iter 
    # count_iter += 1
    # print('11')
    result = 1
    while i > 0:
        count_iter += 1
        # print('22')
        result *= i
        # print(i, result)
        i -= 1
    return result

count_rec = 0
count_rec_dict = 0
prev_dict = {}

def fact_recur(i):
    global count_rec
    count_rec += 1
    # print('111')
    if i == 0 or i == 1:
        return i
    while i > 1:
        # print('222')
        return i * fact_recur(i-1)

# def fact_recur_dict(i, prev_dict = {1 = 1}):
def fact_recur_dict(i):
    global count_rec_dict
    count_rec_dict += 1
    # print('1111')
    if i == 0 or i == 1:
        return i
    elif i in prev_dict:
        return prev_dict[i]
    else:
        # print('2222')
        return i * fact_recur_dict(i-1)


count_iter = 0
count_rec = 0
count_rec_dict = 0
prev_dict = {}
fact_iter(16)
fact_recur(16)
fact_recur_dict(16)
count_iter, count_rec, count_rec_dict

count_iter = 0
count_rec = 0
count_rec_dict = 0
prev_dict = {}
fact_iter(999)
fact_recur(999)
fact_recur_dict(999)

count_iter, count_rec, count_rec_dict