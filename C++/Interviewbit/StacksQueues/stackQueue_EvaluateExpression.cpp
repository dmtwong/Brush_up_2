//============================================================================
// Name        : stackQueue_EvaluateExpression.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	// int Solution::evalRPN(vector<string> &A) {
	int evalRPN(vector<string> &A) {
	    stack<int> st_num;
	    int n_A = A.size();
	    string cur_i;
	    int int_cur_i;
	    int num_1;
	    int num_2;
	    for (int i = 0; i < n_A; i++) {
	    	cur_i = A[i];
	        if (cur_i != "+" && cur_i != "-" && cur_i != "/" && cur_i != "*") {
	        	int_cur_i = stoi(cur_i);
	        	st_num.push(int_cur_i);
	            continue;
	        }
	        else {
	            num_1 = st_num.top();
	            st_num.pop();
	            num_2 = st_num.top();
	            st_num.pop();
	            if (cur_i == "+")
	            	st_num.push(num_2 + num_1);
	            else if (cur_i == "-")
	            	st_num.push(num_2 - num_1);
	            else if (cur_i == "*")
	            	st_num.push(num_2 * num_1);
	            else
	            	st_num.push(num_2 / num_1);
	        }
	    }
	    return st_num.top();
	}

	return 0;
}

/*
 * Problem Description
An arithmetic expression is given by a string array A of size N. Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each string may be an integer or an operator.

Problem Constraints
1 <= N <= 105

Input Format
The only argument given is string array A.

Output Format
Return the value of arithmetic expression formed using reverse Polish Notation.

Example Input
Input 1:
    A =   ["2", "1", "+", "3", "*"]
Input 2:
    A = ["4", "13", "5", "/", "+"]

Example Output
Output 1:
    9
Output 2:
    6

Example Explanation
Explaination 1:
    starting from backside:
    * : () * ()
    3 : () * (3)
    + : (() + ()) * (3)
    1 : (() + (1)) * (3)
    2 : ((2) + (1)) * (3)
    ((2) + (1)) * (3) = 9
Explaination 2:
    + : () + ()
    / : () + (() / ())
    5 : () + (() / (5))
    13 : () + ((13) / (5))
    4 : (4) + ((13) / (5))
    (4) + ((13) / (5)) = 6
 */

/*
 * int Solution::evalRPN(vector<string> &tokens) {
    stack<int> st;
            for(int i = 0; i < tokens.size(); ++i) {
                if(tokens[i] == "+" || tokens[i] == "-" || tokens[i] == "*" || tokens[i] == "/") {
                    int v1=st.top();
                    st.pop();
                    int v2=st.top();
                    st.pop();
                    switch(tokens[i][0]) {
                        case '+':
                            st.push(v2 + v1);
                            break;
                        case '-':
                            st.push(v2 - v1);
                            break;
                        case '*':
                            st.push(v2 * v1);
                            break;
                        case '/':
                            st.push(v2 / v1);
                            break;
                    }
                } else {
                    st.push(atoi(tokens[i].c_str()));
                }
            }
            return st.top();
}

class Solution {
    def evalRPN(A: Array[String]): Int  = {
      import scala.collection.mutable
      val stack = mutable.Stack[Int]()
      for (ai <- A) {
        ai match {
          case "+" => stack.push(stack.pop() + stack.pop())
          case "*" => stack.push(stack.pop() * stack.pop())
          case "-" => {
            val a1 = stack.pop()
            val a2 = stack.pop()
            stack.push(a2 - a1)
          }
          case "/" => {
            val a1 = stack.pop()
            val a2 = stack.pop()
            stack.push(a2 / a1)
          }
          case ch => stack.push(ch.toInt)
        }
      }
      stack.top
    }
}

from operator import *
from itertools import starmap
class Solution:

    def evalRPN(self, A):
        D = dict(zip("+-* /", [add, sub, mul, floordiv]))
        S = []
        for a in A:
            if a in D:
                x, y = S.pop(), S.pop()
                S.append(D[a](y, x))
            else:
                S.append(int(a))
        return S[0]

 */
