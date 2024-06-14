//============================================================================
// Name        : array_AddOneToNumber_1.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
/*
 * Problem Description
Given a non-negative number represented as an array of digits, add 1 to the number ( increment the number represented by the digits ).
The digits are stored such that the most significant digit is at the head of the list.
NOTE: Certain things are intentionally left unclear in this question which you should practice asking the interviewer. For example:
for this problem, following are some good questions to ask :
Q : Can the input have 0's before the most significant digit. Or in other words, is 0 1 2 3 a valid input?
A : For the purpose of this question, YES
Q : Can the output have 0's before the most significant digit? Or in other words, is 0 1 2 4 a valid output?
A : For the purpose of this question, NO. Even if the input has zeroes before the most significant digit.
Problem Constraints
1 <= |A| <= 106
0 <= Ai <= 9
Input Format
First argument is an array of digits.

Output Format
Return the array of digits after adding one.

Example Input
Input 1:
[1, 2, 3]
Example Output
Output 1:
[1, 2, 4]
Example Explanation
Explanation 1:
Given vector is [1, 2, 3].
The returned vector should be [1, 2, 4] as 123 + 1 = 124.
 *
 */
#include <iostream>
#include <vector>

using namespace std;

int main() {
	// cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	//vector<int> Solution::plusOne(vector<int> &A) {
	vector<int> plusOne(vector<int> &A) {
	    int n_A = A.size();
	    int ix_cur = n_A - 1;
	    int cur = A[ix_cur] + 1;
	    if (cur != 10){
	        A[ix_cur] = cur;
	        return A;
	    }

	    cur = A[ix_cur] + 1;
	    A[ix_cur] = cur;
	    while (ix_cur >= 1){
	        if (A[ix_cur] <= 9){
	            return A;
	        } else {
	            A[ix_cur] = cur - 10;
	            A[ix_cur - 1] += 1;
	            ix_cur -= 1;
	        }
	    }
	    if (A[ix_cur] == 10){
	        A[ix_cur] = 0;
	        A.insert(A.begin(), 1);
	    }
	    // A.erase(A.begin()+1);
	    if (A[1] == 0){
	        A.erase(A.begin());
	        //return &(A+1);
	    }
	    return A;
	}
	return 0;
}

/* Cannot remove 0 at ix = 0 for non sense input ase:
 *
 * vector<int> Solution::plusOne(vector<int> &digits) {
    assert(digits.size() >= 1 && digits.size() <= 1e6);
    reverse(digits.begin(), digits.end());
    vector<int> ans;
    int carry = 1;
    for (int i = 0; i < digits.size(); i++) {
        assert(digits[i] >= 0 && digits[i] < 10);
        int sum = digits[i] + carry;
        ans.push_back(sum%10);
        carry = sum / 10;
    }
    while (carry) {
        ans.push_back(carry%10);
        carry /= 10;
    }
    while (ans[ans.size() - 1] == 0 && ans.size() > 1) {
        ans.pop_back();
    }
    reverse(ans.begin(), ans.end());
    reverse(digits.begin(), digits.end());
    return ans;
}
 *
 * Scala:
 * class Solution {
    def plusOne(A: Array[Int]): Array[Int]  = {
        var bb = 1
        for {
            i <- A.length - 1 to 0 by -1
            ai = A(i)
        } {
            val aa = ai + bb
            if (aa == 10) {
                A(i) = 0
                bb = 1
            } else {
                A(i) = A(i) + bb
                bb = 0
            }
        }
        val ret = if (bb == 0) A else bb +: A
        ret.dropWhile(_ == 0)
    }
}

GO:

func plusOne(A []int )  ([]int) {
    var result []int
    var carry int = 1

    // Remove leading 0s and spurious negative numbers
    for len(A) > 0 && A[0] <= 0 {
        A = A[1:]
    }
    for i := len(A) - 1; i >= 0; i-- {
        sum := A[i] + carry
        carry = sum / 10
        sum = sum % 10
        result = append(result, sum)
    }
    if carry > 0 {
        result = append(result, carry)
    }

    // Reverse result
    for i, j := 0, len(result)-1; i < j; i, j = i+1, j-1 {
        result[i], result[j] = result[j], result[i]
    }
    return result
}
Python:
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):

        for i in range(len(A)-1,-1,-1):
            if A[i] != 9:
                A[i] = A[i] + 1
                while A[0] == 0:
                    del A[0]
                break
            else:
                A[i] = 0
        else:
            A.insert(0,1)
        return A
 *
 */
