# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 13:49:33 2024

@author: USER
"""

# Merge two sorted linked lists and return it as a new list. 

# The new list should be made by splicing together the nodes of the first two lists, and should also be sorted.

# For example, given following linked lists :

#   5 -> 8 -> 20 
#   4 -> 11 -> 15
# The merged list should be :

# 4 -> 5 -> 8 -> 11 -> 15 -> 20

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

# class Solution:
# 	# @param A : head node of linked list
# 	# @param B : head node of linked list
# 	# @return the head node in the linked list
# 	def mergeTwoLists(self, A, B):
def mergeTwoLists(A, B):
    result_curr = ListNode(True)
    result_head = ListNode(True)
    result_head.next = result_curr
    curr_a = A
    curr_b = B
    while curr_a.next != None and curr_b.next != None:
        val_a, val_b = curr_a.val, curr_b.val
        if val_a <= val_b:
            result_curr.next = curr_a
            result_curr = curr_a
            curr_a = curr_a.next
        else:
            result_curr.next = curr_b
            result_curr = curr_b
            curr_b = curr_b.next
    while curr_a.next != None:
        result_curr = curr_a
        result_curr.next = curr_a
        curr_a = curr_a.next
    while curr_b.next != None:
        result_curr = curr_b
        result_curr.next = curr_b 
        curr_b = curr_b.next       
    result_curr.next = None
    return result_head.next.next



# # # #     # Editoral:
# # # #         # Python 
# class Solution:
#     # @param A : head node of linked list
#     # @param B : head node of linked list
#     # @return the head node in the linked list
#     def mergeTwoLists(self, A, B):
#         head = None
#         if A.val > B.val:
#             head = B
#             B = B.next
#             if B == None:
#                 head.next=A
#                 return head 
#         else:
#             head = A
#             A = A.next
#             if A==None:
#                 head.next=B
#                 return head

#         current = head
#         while True:
#             if A.val > B.val:
#                 current.next = B
#                 current = current.next
#                 B = B.next
#                 if B == None:
#                     current.next = A
#                     break
#             else:
#                 current.next = A
#                 current = current.next
#                 A = A.next
#                 if A == None:
#                     current.next = B
#                     break
#         return head

# Scala:
# // Definition for singly-linked list.
# //    function Node(data){
# //         this.data = data
# //         this.next = null
# //}

# module.exports = { 
#     //param a : head node of linked list
#     //param b : head node of linked list
#     //return the head node in the linked list
# 	mergeTwoLists : function(a, b){
# 	    var result = new Node(1);
#         var head = result;
#         while (a != null && b != null) {
#             if (a.data >= b.data) {
#                 var nextB = b.next;
#                 result.next = b;
#                 b.next = null;
#                 b = nextB;
#             } else {
#                 var nextA = a.next;
#                 result.next = a;
#                 a.next = null;
#                 a = nextA;
                
#             }
#             result = result.next;
#         }
#         if (a != null) result.next = a;
#         if (b != null) result.next = b;
#         return head.next;
# 	}
# };

# C++:                
# /**
#  * Definition for singly-linked list.
#  * struct ListNode {
#  *     int val;
#  *     ListNode *next;
#  *     ListNode(int x) : val(x), next(NULL) {}
#  * };
#  */
# ListNode* Solution::mergeTwoLists(ListNode* A, ListNode* B) {
#     ListNode *ret, *temp, *rettemp;
#     if (!A) {
#         return B;
#     }
#     if (!B) {
#         return A;
#     }
#     if (A->val <= B->val) {
#         ret = new ListNode(A->val);
#         A = A->next;
#     } else {
#         ret = new ListNode(B->val);
#         B = B->next;
#     }
    
#     temp = ret;
#     while (A&&B) {
#         if (A->val <= B->val) {
#             temp->next = new ListNode(A->val);
#             A = A->next;
#         } else {
#             temp->next = new ListNode(B->val);
#             B = B->next;
#         }
#         temp = temp->next;
#     }
#     while (A) {
#         temp->next = new ListNode(A->val);
#         A = A->next;
#         temp = temp->next;
#     }
#     while (B) {
#         temp->next = new ListNode(B->val);
#         B = B->next;
#         temp = temp->next;
#     }
    
#     return ret;
# }
            
# GO: 
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
#  * @input B : Head pointer of linked list 
#  * 
#  * @Output head pointer of list.
#  */
# func mergeTwoLists(A *listNode , B *listNode )  (*listNode) {
#     ha, hb := A, B
#     var h, curr *listNode
#     for ha!=nil && hb!=nil {
#         if ha.value<hb.value {
#             if h==nil {
#                 h=A
#                 curr=A
#             } else {
#                 curr.next=ha
#                 curr=curr.next
#             }
#             ha=ha.next
#         } else {
#             if h==nil {
#                 h=B
#                 curr=B
#             } else {
#                 curr.next=hb
#                 curr=curr.next
#             }
#             hb=hb.next
#         }
#     }
#     if ha!=nil {
#         if h==nil {
#             h=ha
#         } else {
#             curr.next=ha
#         }
#     }
#     if hb!=nil {
#         if h==nil {
#             h=hb
#         } else {
#             curr.next=hb
#         }
#     }
#     return h
# }
