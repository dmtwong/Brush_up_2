# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 22:37:27 2024

@author: USER
"""

# Problem Description
# Given a list, rotate the list to the right by k places, where k is non-negative.

# Problem Constraints
# 1 <= B <= 109

# Input Format
# The first argument is ListNode A, pointing to the head of the list.
# The second argument is an integer B, representing the value of k.

# Output Format
# Return the rotated list.

# Example Input
# A = 1->2->3->4->5->NULL
# B = 2

# Example Output
# 4->5->1->2->3->NULL


# Example Explanation
# Given list: A = 1->2->3->4->5->NULL
# Given B = 2;
# After rotating A once, A = 5->1->2->3->4->NULL
# After rotating A again, A = 4->5->1->2->3->NULL
# Hence after rotating the given list A, for B = 2, return 4->5->1->2->3->NULL

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

# class Solution:
# 	# @param A : head node of linked list
# 	# @param B : integer
# 	# @return the head node in the linked list
# 	def rotateRight(self, A, B):

def rotateRight(A, B):
    # head = A
    # last = head 
    # temp = head 
    # if head == None or B == 0: 
    #     return head 
    # while last.next != None: 
    #     last = last.next          
    # while B: 
    #     head = head.next
    #     temp.next = None
    #     last.next = temp 
    #     last = temp 
    #     temp = head 
    #     B -= 1           
    # return head 
    # If the linked list is empty
    if (not A):
        return A
    tmp = A
    n_A = 1    
    while (tmp.next != None):
        tmp = tmp.next
        n_A += 1
    if (B > n_A):
        B = B % n_A
    B = n_A - B
    if (B == 0 or B == n_A):
        return A

    curr = A
    count = 1
    
    while (count < B and curr != None):
        curr = curr.next
        count += 1

    if (curr == None):
        return A

    node_K = curr
    tmp.next = A

    A = node_K.next
    node_K.next = None

    return A
    
        
    
# class Solution:
#     # @param A : head node of linked list
#     # @param B : integer
#     # @return the head node in the linked list
#     def rotateRight(self, A, B):
#         head = A
#         last = None
#         length = 0
        
#         # get length of list as well as the last node of the current list
#         while A:
#             last = A
#             A = A.next
#             length += 1
        
#         # because B can be greater than length of list...normalize B
#         B %= length
        
#         if B == 0:
#             return head
        
#         cur = head
        
#         # get to the point where you will detach the list and rotate it
#         for i in range(length - B - 1):
#             cur = cur.next
        
#         rotated_head = cur.next
#         cur.next = None
#         last.next = head
        
#         return rotated_head

# ListNode* Solution::rotateRight(ListNode* A, int B) {
#     ListNode* ret, *curr, *prev;
#     int temp, length = 0;
#     curr = A;
#     prev = A;
#     while(curr) {
#         ++length;
#         curr = curr->next;
#     }
#     if (length == 0 || B%length == 0) {
#         return A;
#     }
#     curr = A;
#     temp = B%length;
#     while(temp-- > 0 ) {
#         curr = curr->next;
#     }
#     while (curr->next) {
#         curr = curr->next;
#         prev = prev->next;
#     }
#     ret = prev->next;
#     prev->next = NULL;
#     curr->next = A;
#     return ret;
# }

# class Solution {
#     def rotateRight(A: ListNode, B: Int): ListNode  = {
#       var head = A
#       var cur = head
#       var len = 1
#       while (cur.next != null) {
#         cur = cur.next
#         len += 1
#       }
#       cur.next = head
#       var preLen = len - B % len - 1
#       var pre = head
#       while (preLen > 0) {
#         pre = pre.next
#         preLen -= 1
#       }
    
#       head = pre.next
#       pre.next = null
#       head
#     }
# }

