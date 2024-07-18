//============================================================================
// Name        : bitM_TrailingZeroes.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

/*Problem Description
Given an integer A, count and return the number of trailing zeroes.
Problem Constraints
1 <= A <= 109
Input Format
First and only argument is an integer A.
Output Format
Return an integer denoting the count of trailing zeroes.
Example Input
Input 1:
 A = 18
Input 2:
 A = 8


Example Output
Output 1:

 1
Output 2:

 3


Example Explanation
Explanation 1:

 18 in binary is represented as: 10010, there is 1 trailing zero.
Explanation 2:

 8 in binary is represented as: 1000, there are 3 trailing zeroes.

 *
 *
 */

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	//int Solution::solve(int A) {
	int solve(int A) {
	    int result = 0;
	    while (A > 0 && (A & 1) == 0) {
	        result++;
	        A >>= 1;
	    }
	    return result;
	}
	return 0;
}

/*
 * int Solution::solve(int x) {
      int count = 0;
  while ((x & 1) == 0)
  {
      x = x >> 1;
      count++;
  }
  return count;

}

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        a=bin(A)
        a=str(a)
        a=a[2::]
        c=0
        for i in a:
            if i!='0':
                c=0
                continue
            else:
                c+=1
        return c

class Solution {
    def solve(A: Int): Int  = {
        A.toBinaryString.reverse.takeWhile(_ == '0').length
    }
}

func solve(A int )  (int) {
    var count int
    for A!=0{
        if A%2 != 0{
            return count
        } else {
            count++
        }
        A/=2
    }
    return count
}

 */
