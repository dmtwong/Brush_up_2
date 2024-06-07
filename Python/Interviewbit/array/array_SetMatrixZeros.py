# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 10:08:24 2024

@author: USER
"""
# # Problem Description
 
# # Given a matrix, A of size M x N of 0s and 1s. If an element is 0, set its entire row and column to 0.
# # Note: This will be evaluated on the extra memory used. Try to minimize the space and time complexity.

# # Problem Constraints
# # 1 <= N, M <= 1000
# # 0 <= A[i][j] <= 1

# # Input Format
# # The first and the only argument of input contains a 2-d integer matrix, A, of size M x N.

# # Output Format
# # Return a 2-d matrix that satisfies the given conditions.

# # Example Input
# # Input 1:
A = [   [1, 0, 1],
    [1, 1, 1], 
    [1, 1, 1]   ]
setZeroes(A)
# Input 2:
A = [   [1, 0, 1],
    [1, 1, 1],
    [1, 0, 1]   ]
A  = [
  [1, 1],
  [0, 0]
]

# Example Output
# Output 1:
# [   [0, 0, 0],
#     [1, 0, 1],
#     [1, 0, 1]   ]
# Output 2:
# [   [0, 0, 0],
#     [1, 0, 1],
#     [0, 0, 0]   ]

# class Solution:
    # @param A : list of list of integers
    # @return the same list modified
def setZeroes(A):
    n_row, n_col = len(A), len(A[0])
    zero_rows, zero_cols = set(), set()
    for i in range(n_row):
        for j in range(n_col):
            if A[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)
    # print(zero_rows, zero_cols)
    for row in zero_rows:
        for j in range(n_col):
            A[row][j] = 0
            # A[n_row-1][j] = 0

    for col in zero_cols:
        for i in range(n_row):
            A[i][col] = 0
            # A[i][n_col-1] = 0
    return A

# C++
# void Solution::setZeroes(vector<vector<int> > &matrix) {
#     int rownum = matrix.size();
#     if (rownum == 0)  return;
#     int colnum = matrix[0].size();
#     if (colnum == 0)  return;

#     bool hasZeroFirstRow = false, hasZeroFirstColumn = false;

#     // Does first row have zero?
#     for (int j = 0; j < colnum; ++j) {
#         if (matrix[0][j] == 0) {
#             hasZeroFirstRow = true;
#             break;
#         }
#     }

#     // Does first column have zero?
#     for (int i = 0; i < rownum; ++i) {
#         if (matrix[i][0] == 0) {
#             hasZeroFirstColumn = true;
#             break;
#         }
#     }

#     // find zeroes and store the info in first row and column
#     for (int i = 1; i < rownum; ++i) {
#         for (int j = 1; j < colnum; ++j) {
#             if (matrix[i][j] == 0) {
#                 matrix[i][0] = 0;
#                 matrix[0][j] = 0;
#             }
#         }
#     }

#     // set zeroes except the first row and column
#     for (int i = 1; i < rownum; ++i) {
#         for (int j = 1; j < colnum; ++j) {
#             if (matrix[i][0] == 0 || matrix[0][j] == 0)  matrix[i][j] = 0;
#         }
#     }

#     // set zeroes for first row and column if needed
#     if (hasZeroFirstRow) {
#         for (int j = 0; j < colnum; ++j) {
#             matrix[0][j] = 0;
#         }
#     }
#     if (hasZeroFirstColumn) {
#         for (int i = 0; i < rownum; ++i) {
#             matrix[i][0] = 0;
#         }
#     }
# }