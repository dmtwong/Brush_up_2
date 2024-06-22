# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:30:32 2024

@author: USER
"""

# Problem Description
# Given a linked list A of length N and an integer B.
# You need to find the value of the Bth node from the middle towards the beginning of the Linked List A.
# If no such element exists, then return -1.
# NOTE:
# Position of middle node is: (N/2)+1, where N is the total number of nodes in the list.

# Problem Constraints
# 1 <= N <= 105
# 1<= Value in Each Link List Node <= 103
# 1 <= B <= 105

# Input Format
# First argument is the head pointer of the linkedlist A.
# Second argument is an integer B.

# Output Format
# Return an integer denoting the value of the Bth from the middle towards the head of the linked list A. If no such element exists, then return -1.

# Example Input
# Input 1:
#  A = 3 -> 4 -> 7 -> 5 -> 6 -> 1 6 -> 15 -> 61 -> 16
#  B = 3
#  Input 2:

#  A = 1 -> 14 -> 6 -> 16 -> 4 -> 10
#  B = 2
#  Input 3:

#  A = 1 -> 14 -> 6 -> 16 -> 4 -> 10
#  B = 10


# Example Output
# Output 1:

#  4
#  Output 2:

#  14
#  Output 3:

#  -1


# Example Explanation
# Explanation 1:

#  The Middle of the linked list is the node with value 6.
#  The 1st node from the middle of the linked list is the node with value 5.
#  The 2nd node from the middle of the linked list is the node with value 7.
#  The 3rd node from the middle of the linked list is the node with value 4.
#  So we will output 4.
# Explanation 2:

#  The Middle of the linked list is the node with value 16.
#  The 1st node from the middle of the linked list is the node with value 6.
#  The 2nd node from the middle of the linked list is the node with value 14.
#  So we will output 14.
# Explanation 3:

#  The Middle of the linked list is the node with value 16.
#  There are only 3 nodes to the left of the middle node and we need to find the 10th node which doesn't exist so we will return -1.

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

# class Solution:
#     # @param A : head node of linked list
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
def solve(A, B):
    val_list = []
    while A:
        val_list.append(A.val)
        A = A.next
    n_A = len(val_list)
    
    mid = n_A // 2
    if n_A % 2 == 0:
        mid += 1
        if mid < B + 1:
            return -1
        else:
            return val_list[mid - B - 1]
    else:
        if mid < B:
            return -1
        else:
            return val_list[mid - B]
    # return val_list[mid - B - 1]
    
# 47 806 891 730 371 351 7 102 394 549 630 624 85 955 757 841 967 377 932 309 945 440 627 324 538 539 119 83 930 542 834 116 640 659 705 931 978 307 674 387 22 746 925 73 271 830 778 574 
# 22

# 3 196 486 94 
# # 1


# # Definition for singly-linked list.
# # class ListNode:
# #    def __init__(self, x):
# #        self.val = x
# #        self.next = None
# # Function to count number of nodes 
# def getCount(head): 
      
#     count = 0 # Initialize count 
#     current = head # Initialize current 
#     while (current ):  
#         count = count + 1
#         current = current.next
      
#     return count 
  
# # Function to get the kth node from the mid 
# # towards begin of the linked list 
# def printKthfrommid(head_ref, k): 
  
#     # Get the count of total number of 
#     # nodes in the linked list 
#     n = getCount(head_ref) 
  
#     reqNode = int((n / 2 + 1) - k) 
  
#     # If no such node exists, return -1 
#     if (reqNode <= 0) : 
#         return -1
      
#     # Find node at position reqNode 
#     else : 
#         current = head_ref 
  
#         # the index of the 
#         # node we're currently 
#         # looking at 
#         count = 1
#         while (current) : 
#             if (count == reqNode): 
#                 return (current.val) 
#             count = count + 1
#             current = current.next
      
# class Solution:
#     # @param A : head node of linked list
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         return printKthfrommid(A,B);

# int Solution::solve(ListNode* A, int B) {

#     ListNode*p=A;
#     int s=0;
#     while(p)
#     {
#         s++;p=p->next;
#     }

#     B=B+((s+1)/2);

#     B=s-B;

#     if(B<0) return -1;

#     p=A;

#     while(B--)
#     {
#         p=p->next;
#     }

#     return p->val;
# }
# class Solution {
#     def solve(A: ListNode, B: Int): Int  = {
        
#         val head1 = A
#         val K = B
        
#         var slow = head1
#         var fast = head1
#         var midPosition = 0
        
#         while(fast != null && fast.next != null) {
#             slow = slow.next
#             fast = fast.next.next
#             midPosition = midPosition + 1
#         }
        
#         var reqPosition = midPosition - K
        
#         if(reqPosition < 0) return -1
        
#         var result = -1
#         var currPosition = 0
#         var currNode = head1
#         while(currNode != null && currPosition < reqPosition) {
#             currPosition = currPosition + 1
#             currNode = currNode.next
#         }
        
#         if(currNode != null) result = currNode.value
        
#         result
#     }
# }
