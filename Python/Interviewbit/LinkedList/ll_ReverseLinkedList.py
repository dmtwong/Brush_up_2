# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:05:04 2024

@author: USER
"""

# Reverse a linked list. Do it in-place and in one-pass.

# For example:

# Given 1->2->3->4->5->NULL,

# return 5->4->3->2->1->NULL.

# PROBLEM APPROACH :

# Complete solution code in the hints

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

# class Solution:
# 	# @param A : head node of linked list
# 	# @return the head node in the linked list
# 	def reverseList(self, A):
    
# 5, 4, 3, 2, 1
def reverseList(A):
    curr = A
    prev = None
    while curr: # curr.next point to 4 not none
        next_1 = curr.next # temp save curr.next to next_1
        curr.next = prev # replacing curr.next to None from Node 4
        prev = curr # replacing prev to pointer to Node 4 from None
        curr = next_1 # changing the curr to 4 
    return prev


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.following = None

# def solve(A):
#     if not A:
#         return A
#     curr = A
#     prev = temp = tail = result = join = None
    
#     while (curr != None) :    
#         print(result, prev, temp, tail, join)
#         join = curr
#         temp = curr.next
#         curr.next = prev
#         prev = curr
#         curr = temp        
#         if (result == None):
#             result = prev    
#         if (tail != None):
#             tail.next = prev    
#         tail = join
#         tail.next = curr
#         tail = prev
#     # return result
#     A = result
#     return A

# A = [ 97 -> 63 -> 89 -> 34 -> 82 -> 95 -> 4 -> 70 -> 14 -> 41 -> 38 -> 83 -> 49 -> 32 -> 68 -> 56 -> 99 -> 52 -> 33 -> 54 ]

    # temp = A
    # temp = ListNode(None)
    # temp.next = A
    # curr = temp 
    # following = temp 
    # last = temp
    # count_len, block_size = 0, 0
 
    # while curr != None:
    #     curr = curr.next
    #     count_len += 1
    
    # isRev = True
    # while following:
    #     # print('here', following.val)
    #     block_size = (count_len > B and B) or (count_len - 1) 
    #     if (isRev):
    #         curr = last.next
    #         following = curr.next
    #         for i in range(1, block_size):
    #             # print('there', i, curr.next, following.next, last.next)
    #             curr.next = following.next
    #             following.next = last.next
    #             last.next = following
    #             following = curr.next
    #             # print('there', i, curr.next, following.next, last.next)
    #         last = curr
    #         count_len -= B
    #     else:
    #         for i in range(1, block_size):
    #             # print('there', i, curr.next, following.next, last.next)

    #     isRev = not(isRev)
    
    # return temp.next
        

# Node1 = ListNode(5) 
# Node2 = ListNode(4) 
# Node3 = ListNode(3)
# Node4 = ListNode(2)
# Node5 = ListNode(1)
# # Node6 = ListNode(4)
# Node1.next = Node2
# Node2.next = Node3
# Node3.next = Node4
# Node4.next = Node5
# Node5.next = None # Node6
# now = solve(Node1)
# now.val
# now.next.val

# temp.val
# temp.next.val
# temp.next.next.val
# temp.next.next.next.next.val

# c++
# /**
#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     ListNode *next;
#  *     ListNode(int x) : val(x), next(NULL) {}
#  * };
#  */
# ListNode* Solution::reverseList(ListNode* A) {
#     ListNode *revA = NULL, *nextA;
#     while (A) {
#         nextA = A->next;
#         A->next = revA;
#         revA = A;
#         A = nextA;
#     }
#     return revA;
# }

# Scala:
# /*
#  * Definition for singly-linked list
#  * class ListNode(val xc: Int){
#  *     var value: Int = xc
#  *     var next: ListNode = null
#  * }
# */
# class Solution {
#     def reverseList(A: ListNode): ListNode  = {
#         def reverseList(curr: ListNode, prev: ListNode): ListNode = {
#             if (curr.next == null) {
#                 curr.next = prev
#                 return curr
#             }
 
#             val next: ListNode = curr.next
     
#             curr.next = prev
     
#             return reverseList(next, curr)
            
#         }
#         reverseList(A, null)
#     }
# }

# GO: 
    

# Editorial

# 0

# 0
# /**
#  * Definition for singly-linked list.
#  * type listNode struct {
#  *     value int
#  *     next *listNode
#  * }
#  * 
#  * func listNode_new(val int) *listNode{
#  *     var node *listNode = new(listNode)
#  *     node.value = val
#  *     node.next = nil
#  *     return node
#  * }
#  */
# /**
#  * @input A : Head pointer of linked list 
#  * 
#  * @Output head pointer of list.
#  */
# func reverseList(root *listNode )  (*listNode) {
#     if root == nil || root.next == nil {
#         return root
#     }
#     rest := reverseList(root.next)
#     root.next.next = root
#     root.next = nil
#     return rest
# }
