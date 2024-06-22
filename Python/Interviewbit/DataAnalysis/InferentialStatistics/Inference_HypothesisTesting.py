# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 13:31:29 2024

@author: USER
"""

# Problem Description

# A candidate sat in recruitment tests for the job of data scientists by one of the top leading firms of US. He was confused whether the salary in the company is good or not. So, what he did was that he took a survey of 14 employees working there. Their salaries would be given as input and candidates would like to test the hypothesis whether there is no significant mean difference in salary of data scientists given input mean. We have to return True if we can decline the hypothesis else False (Take threshold of 0.05)

# Sample Input: (Salary in thousands $)
# [183, 152, 178, 157, 194, 163, 144, 114, 178, 152, 118, 158, 172, 138]

# 165

# Sample Output:
# False

# import numpy as np
def solve(salary_lst, mu):
    import numpy as np
    from scipy.stats import t
    n_lst = len(salary_lst)    
    var = np.var(salary_lst) 
    var_p = var * (n_lst) / (n_lst - 1)
    # return var_p
    sd = var_p**0.5
    mu_lst = np.mean(salary_lst)
    # t_stat = np.random.standard_t(n_lst - 1) # stats.pdf(0.05, n_lst - 1)
    # return abs(mu_lst - mu) / (sd / (n_lst)**0.5)
    #return abs(mu_lst - mu) / (sd / (n_lst)**0.5) >= abs(t_stat)
    t_stat = (mu_lst - mu) / (sd / (n_lst)**0.5)
    return 2*(1- t.cdf(abs(t_stat), n_lst-1)) < 0.05