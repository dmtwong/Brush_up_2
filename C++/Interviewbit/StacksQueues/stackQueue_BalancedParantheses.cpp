//============================================================================
// Name        : stackQueue_BalancedParantheses.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	//int Solution::solve(string A) {
	int solve(string A) {
    	deque <char> dq_char;
		int n_A = A.length();
		int cur_dq_len;
        char cur_i;
        int count = 0;
		for (int i = 0; i < n_A; i++){
			cur_i = A[i];
			if (cur_i == '('){
				dq_char.push_back(cur_i);
                count += 1;
			} else {
                count -= 1;

				cur_dq_len = dq_char.size();
				if (cur_dq_len > 0){
					dq_char.pop_back();
					continue;
				} else {
					return 0;
				}

			}
		}
        //return count;

		if (count == 0){
			return 1;
		} else {
			return 0;
		}

	return 0;
}

/*
 * Problem Description
Given a string A consisting only of '(' and ')'.
You need to find whether parantheses in A is balanced or not ,if it is balanced then return 1 else return 0.
Problem Constraints
1 <= |A| <= 105
Input Format
First argument is an string A.
Output Format
Return 1 if parantheses in string are balanced else return 0.

Example Input
Input 1:
 A = "(()())"
Input 2:
 A = "(()"
Example Output
Output 1:
 1
Output 2:
 0
Example Explanation
Explanation 1:
 Given string is balanced so we return 1
Explanation 2:
 Given string is not balanced so we return 0
 */


	/*
	 *
	 * int Solution::solve(string A)
{
    stack<int> s;
    for(int i=0;i<A.size();i++)
    {
        if(A[i]=='(')
        {
            s.push(i);
        }
        else
        {
            if(s.empty())
            {
                return 0;
            }
            s.pop();
        }
    }
    return s.empty();

}

Scala:
class Solution {
    def solve(A: String): Int  = {
        var openBrackets = 0

        for (c <- A) {
            c match{
                case '(' => openBrackets += 1
                case ')' => if (openBrackets == 0) return 0 else openBrackets -= 1
            }
        }
        return if (openBrackets > 0)  0 else 1
    }
}

func solve(A string )  (int) {
    stack := []byte{}

    for _, val := range A {
        if val == '(' {
            stack = append(stack, '(')
        } else {
            if len(stack) == 0 {
                return 0
            }

            stack = stack[0:len(stack)-1]
        }
    }

    if len(stack) > 0 {
        return 0
    }

    return 1
}

def solveQ(A):
    stk=[]
    for a in A:
        if(a=='('):
            stk.append(a)
            continue
        if(len(stk)==0):
            return False
        if(a==')'):
            x=stk[-1]
            stk.pop(-1)
            if(x!='('):
                return False
    if(len(stk)==0):
        return True
    return False

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        if(solveQ(A)==False):
            return 0
        return 1
	 */
