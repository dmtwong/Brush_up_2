# -*- coding: utf-8 -*-
"""
Created on Fri May 31 13:46:29 2024

@author: USER
"""

# Problem Description

# Given the position of a Bishop (A, B) on an 8 * 8 chessboard.

# Your task is to count the total number of squares that can be visited by the Bishop in one move.

# The position of the Bishop is denoted using row and column number of the chessboard.



# Problem Constraints
# 1 <= A, B <= 8



# Input Format
# First argument is an integer A denoting the row number of the bishop.

# Second argument is an integer B denoting the column number of the bishop.



# Output Format
# Return an integer denoting the total number of squares that can be visited by the Bishop in one move.

temp = []
temp.append([0] * 5)
temp
# Example Input
# Input 1:

  A = 4
  B = 4
solve(A, B)

# Example Output
# Output 1:

#  13

# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
    
    # Consider:
        # 1   2
        # 3   4
def solve(A, B):
    row_lf = B - 1
    row_rt = 8 - B
    col_up = 8 - A
    col_down = A - 1
    return min(row_lf, col_down) + min(row_rt, col_down) + min(row_rt, col_up) + min(row_lf, col_up);

A = 1; B = 8
solve(A, B)
A = 8; B = 1
solve(A, B)
A = 8; B = 8
solve(A, B)
A = 1; B = 1
solve(A, B)
A = 2; B = 2
solve(A, B)


    # Editoral:
        # Python
# Function to return the count of  
# total positions the Bishop  
# can visit in a single move 
# def countSquares(row, column): 
      
#     # Count top left squares 
#     topLeft = min(row, column) - 1
      
#     # Count bottom right squares 
#     bottomRight = 8 - max(row, column) 
      
#     # Count top right squares 
#     topRight = min(row, 9-column) -1
      
#     # Count bottom left squares 
#     bottomLeft = 8 - max(row, 9-column)  
  
      
#     # Return total count 
#     return (topLeft + topRight + bottomRight + bottomLeft) 
# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         return countSquares(A,B)
    
#     # C++
# int Solution::solve(int A, int B) {

    
#     return min(B-1,A-1) + min(8-B,A-1) + min(8-B,8-A) + min(B-1,8-A);
    
    
# }

# GO:
#     /**
#  * @input A : Integer
#  * @input B : Integer
#  * 
#  * @Output Integer
#  */
# // 4 + 4 + 

# func min(A ,B int) (int){
#     if A > B {
#         return B
#     }
#     return A
# }



# func solve(A int , B int )  (int) {
#     Ad := 8-A
#     Bd := 8-B  
#     A = A-1 // Row
#     B = B-1 // Col
#     return min(Ad,B) + min(B,A) + min(A,Bd) + min(Bd,Ad)
# }

# Scala
# class Solution {
    
#   def solve(A: Int, B: Int): Int  = {
#     upLeft(A, B) +
#     upRight(A, B) +
#     bottomLeft(A, B) +
#     bottomRight(A, B)
#   }

#   private def upLeft(A: Int, B: Int): Int = {
#     var count = -1
#     var a = A
#     var b = B
#     while (a >= 1 && a <= 8 && b >= 1 && b <= 8) {
#       count = count + 1
#       a = a - 1
#       b = b - 1
#     }
#     count
#   }

#   private def upRight(A: Int, B: Int): Int = {
#     var count = -1
#     var a = A
#     var b = B
#     while (a >= 1 && a <= 8 && b >= 1 && b <= 8) {
#       count = count + 1
#       a = a - 1
#       b = b + 1
#     }
#     count
#   }

#   private def bottomLeft(A: Int, B: Int): Int = {
#     var count = -1
#     var a = A
#     var b = B
#     while (a >= 1 && a <= 8 && b >= 1 && b <= 8) {
#       count = count + 1
#       a = a + 1
#       b = b - 1
#     }
#     count
#   }

#   private def bottomRight(A: Int, B: Int): Int = {
#     var count = -1
#     var a = A
#     var b = B
#     while (a >= 1 && a <= 8 && b >= 1 && b <= 8) {
#       count = count + 1
#       a = a + 1
#       b = b + 1
#     }
#     count
#   }
# }
