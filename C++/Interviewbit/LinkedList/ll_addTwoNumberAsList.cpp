//============================================================================
// Name        : ll_addTwoNumberAsList.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

/*
 * You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
    342 + 465 = 807
Make sure there are no trailing zeros in the output list

So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
 */
#include <iostream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	/**
	 * Definition for singly-linked list.
	 * struct ListNode {
	 *     int val;
	 *     ListNode *next;
	 *     ListNode(int x) : val(x), next(NULL) {}
	 * };
	 */
	// ListNode* Solution::addTwoNumbers(ListNode* A, ListNode* B) {
	ListNode* addTwoNumbers(ListNode* A, ListNode* B) {
        if (!A){
			return B;
		}
		if (!B){
			return A;
		}
		//deque <int> dq_int_1;
		//deque <int> dq_int_2;
		// int n_A = 0;
		// int n_B = 0;
		int cur_A;
		int cur_B;
		int sum;
		int carry = 0;
		int remain;

		//ListNode *curr = NULL;
		ListNode *prev = NULL;
		ListNode * result = NULL;

		ListNode *curr = A;
		curr = curr->next;
		while(curr!= NULL){
			if (curr->next == NULL){
				assert(curr->val != 0);
			}
			curr = curr->next;
		 }

		curr = B;
		while(curr!= NULL){
			if (curr->next == NULL){
				assert(curr->val != 0);
			}
			curr = curr->next;
		 }

		//temp_1 = A.next;
		while (A || B){
			// n_A += 1;
			// dq_int_1.push_front(temp->val);
			// if (A){
			//	cur_A = A.val;
			//} else {
			//	cur_A = 0;
			//}
			sum = (A ? A->val: 0) + (B ? B->val: 0) + carry;
			carry = sum/10;
			remain = sum % 10;
			curr = new ListNode(remain);
			if (result) {
				prev->next = curr;
			} else {
				result = curr;
			}
            prev = curr;
			if (A){
                A = A->next;
            }
            if (B){
                B = B->next;
            }
		}
		if (carry >= 1){
			curr->next = new ListNode(carry);
            // prev->next = curr;
            //result = curr;
            //curr->val = 1;
		}
		return result;
	}

	return 0;
}


/*
 * # Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def addTwoNumbers(self, A, B):
        dummy = ListNode(0)
        a, b, c = A, B, dummy
        carry = False
        while a or b or carry:
            total = int(carry)
            if a:
                total += a.val
                a = a.next
            if b:
                total += b.val
                b = b.next

            if total >= 10:
                carry = True
                total %= 10
            else:
                carry = False
            new = ListNode(total)
            c.next = new
            c = new

        return dummy.next

Scala:
class Solution {
    def addTwoNumbers(A: ListNode, B: ListNode): ListNode  = {
      var res = new ListNode(0)
      val ret = res
      var node1 = A
      var node2 = B
      var rem = 0
      while (node1 != null || node2 != null) {
        val aa = if (node1 == null) 0 else node1.value
        val bb = if (node2 == null) 0 else node2.value
        var sum = aa + bb + rem
        if (sum >= 10) {
          sum = sum - 10
          rem = 1
        } else {
          rem = 0
        }

        if (node1 != null) node1 = node1.next
        if (node2 != null) node2 = node2.next

        val over = node1 == null && node2 == null
        if (over) {
          res.value = sum
          if(rem > 0) {
            res.next = new ListNode(rem)
          }
        } else {
          res.value = sum
          res.next = new ListNode(0)
          res = res.next
        }
      }
      ret
    }
}
 GO:
 func addTwoNumbers(a, b *listNode) *listNode {
	if a == nil || b == nil {
		return nil
	}
	current := &listNode{}
	head := current
	rem := 0
	for a != nil || b != nil {
		data := rem
		if a != nil {
			data += a.value
			a = a.next
		}
		if b != nil {
			data += b.value
			b = b.next
		}
		if data > 9 {
			rem = 1
			data %= 10
		} else {
			rem = 0
		}
		current.next = &listNode{
			value: data,
		}
		current = current.next
	}

	if rem > 0 {
		current.next = &listNode{
			value: rem,
		}
	}

	return head.next
}

 */
