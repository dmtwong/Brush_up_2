//============================================================================
// Name        : sq_MAXSPPROD.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================
/*
 * Problem Description
 You are given an array A containing N integers. The special product of each ith integer in this array is defined as the product of the following:
LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] and (i>j). If multiple A[j]'s are present in multiple positions, the LeftSpecialValue is the maximum value of j. Here LeftSpecialValue is the index j and not A[j].
RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] and (j>i). If multiple A[j]'s are present in multiple positions, the RightSpecialValue is the minimum value of j. Here RightSpecialValue is the index j and not A[j].
Write a program to find the maximum special product of any integer in the array. In other words you have to find the maximum for all i (0<i<n-1) of product of l and r such that l is the LeftSpecialValue and r is the RightSpecialValue of an index i.
Note that the array A is zero indexed.
NOTE:  As the answer can be large, output your answer modulo 109 + 7.
Problem Constraints
1 <= N <= 105
1 <= A[i] <= 109
Input Format
First and only argument is an integer array A.
Output Format
Return an integer denoting the maximum special product of any integer.
Example Input
Input 1:
 A = [1, 4, 3, 4]
Input 2:
 A = [10, 7, 100]
Example Output
Output 1:
 3
Output 2:
 0
Example Explanation
Explanation 1:
 For A[2] = 3, LeftSpecialValue is 1 and RightSpecialValue is 3.
 So, the ans is 1*3 = 3.
 Explanation 2:
 There is not any integer having maximum special product > 0. So, the ans is 0.
 */

#include <iostream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	// int Solution::maxSpecialProduct(vector<int> &A) {
	int maxSpecialProduct(vector<int> &A) {
	    int n_A = A.size();
	    stack<pair<int,int>> stack_pair;
	    long int lf[n_A];
	    long int rt[n_A];
	    long int result = 0;

	    for (int i = 0; i < n_A; i++){
	        while(!stack_pair.empty() && stack_pair.top().first <= A[i])
	            stack_pair.pop();
	        if (stack_pair.empty()){
	            lf[i] = 0;
	        } else {
	            lf[i] = stack_pair.top().second;
	        }
	        stack_pair.push({A[i],i});
	    }

	    while(!stack_pair.empty()){
	        stack_pair.pop();
	    }

	    for(int j = n_A - 1; j >= 0; j--){
	        while(!stack_pair.empty() && stack_pair.top().first <= A[j]){
	            stack_pair.pop();
	        }
	        if(stack_pair.empty())
	            rt[j] = 0;
	        else
	            rt[j] = stack_pair.top().second;
	        stack_pair.push({A[j],j});
	    }


	    for (int k = 0; k < n_A; k++){
	        result = max(result, lf[k] * rt[k]);
	    }

	    return result%1000000007;

	}
	return 0;
}

/* special value as index not value;
 *
 * 		int n_A = A.size();
		// stack<pair<int, int>> stack_pair;
        // long int cur_pair[2];
        // stack<long int [2]> stack_pair;
        stack<long int> stack_left;
        stack<long int> stack_right;
        stack<long int> stack_ix_ft;
        stack<long int> stack_ix_rt;
		// pair cur_pair;
		long int cur_left;
		long int cur_run;
		long int cur_right;
		long int result;
		long int cur_prod;
        long int ix_lf;
        long int ix_rt;
		int ix_left = 0;
		int ix_right;
		long int cur_i = 0;
        long int lf;
        long int rt;
		bool left_found = false;
		bool right_found = false;
		for (int i = 1; i < n_A; i++){
			cur_i = A[i];
			while (ix_left < i){
				cur_run = A[ix_left];
				if (cur_i < cur_run){
					if (left_found == false){
						cur_left = cur_run;
                        // return cur_left;
						left_found = true;
					} else if (cur_left < cur_run){
						cur_left = cur_run;
					}
					ix_left += 1;
                    continue;
				}
                ix_left += 1;
			}
			ix_left = 0; //reset



			if (left_found == false){
				continue;
			}

			ix_right = i + 1;
			while (ix_right < n_A){
				cur_run = A[ix_right];
				if (cur_i < cur_run){
					if (right_found == false){
						cur_right = cur_run;
						right_found = true;
					} else if (cur_right < cur_run){
						cur_right = cur_run;
					}
					ix_right += 1;
					continue;
				}
                ix_right += 1;
			}
			if (right_found == true){
                stack_left.push(cur_left);
                stack_right.push(cur_right);
                // return 123;
                // stack_pair.push(cur_pair);
				// stack_pair.push(cur_left, cur_right);
			}
		}

        //return int(stack_left.top());

		if (stack_left.empty() == true){
			return 0;
		}
		result = 0;
		while (stack_left.empty() != true){
			//cur_pair = stack_pair.top();
			//cur_prod = cur_pair[0] * cur_pair[1];
            lf = stack_left.top();
			rt = stack_right.top();
            stack_left.pop();
            stack_right.pop();
            cur_prod = lf * rt;
			if (cur_prod > result){
				result = cur_prod;
			}
		}
		return result%1000000007;
 */


/* Editorial
 * int Solution::maxSpecialProduct(vector<int> &A) {
	int n = A.size();
	vector<int> LeftSpecialValue(n,0),RightSpecialValue(n,0);
	stack<int> leftCalc;
	leftCalc.push(0);
	LeftSpecialValue[0]=0;
	for(int i=1;i<n;i++){
		while(!leftCalc.empty()){
			if(A[leftCalc.top()]>A[i]) break;
			leftCalc.pop();
		}
		LeftSpecialValue[i] = (leftCalc.empty())?0:leftCalc.top();
		leftCalc.push(i);
	}
	stack<int> rightCalc;
	rightCalc.push(n-1);
	RightSpecialValue[n-1]=0;
	for(int i=n-2;i>=0;i--){
		while(!rightCalc.empty()){
			if(A[rightCalc.top()]>A[i]) break;
			rightCalc.pop();
		}
		RightSpecialValue[i] = (rightCalc.empty())?0:rightCalc.top();
		rightCalc.push(i);
	}
	long long mx = -1;
	for(int i=0;i<n;i++){
		mx=max(mx,LeftSpecialValue[i]*1LL*RightSpecialValue[i]);
	}
	return mx%1000000007;
}

import scala.collection.mutable.{ArrayBuffer, ListBuffer}

class Solution {
  def maxSpecialProduct(as: Array[Int]): Int  = {
    val mod = 1000000007
    val n = as.length

    def cleanStack(v: Int, s: List[Long]): List[Long] =
      if (s.isEmpty || v < as(s.head.toInt)) s
      else cleanStack(v, s.tail)

    val left = as.foldLeft((0, List[Long](), new ArrayBuffer[Long]())){ case ((i, stack, result), a) =>
      val currStack = cleanStack(a, stack)
      (i + 1, i :: currStack, result += (if (currStack.nonEmpty) currStack.head else 0))
      }._3.toArray
    //println(left.mkString(" "))

    val right = as.foldRight((n - 1, List[Long](), new ListBuffer[Long]())){ case (a, (i, stack, result)) =>
      val currStack = cleanStack(a, stack)
      (i - 1, i :: currStack, result.+=:(if (currStack.nonEmpty) currStack.head else 0))
    }._3.toArray
    //println(right.mkString(" "))

    (left.zip(right).foldLeft(Integer.MIN_VALUE.toLong){
      case (max, (a, b)) => math.max(max, a * b)
    } % mod).toInt
  }
}

GO:
func maxSpecialProduct(A []int )  (int) {
    if len(A) <= 2 {
        return 0
    }
    st := make([]int, 0, 1000)
    left := make([]int, len(A))
    st = append(st, 0)
    for i := 1; i < len(A); i++ {
        for len(st) > 0 && A[st[len(st) - 1]] <= A[i] {
            st = st[:len(st) - 1]
        }
        st = append(st, i)
        if len(st) == 1 {
            continue
        }
        left[i] = st[len(st) - 2]
    }
    st = st[:0]
    right := make([]int, len(A))
    st = append(st, len(A) - 1)
    for i := len(A) - 1; i >= 0; i-- {
        for len(st) > 0 && A[st[len(st) - 1]] <= A[i] {
            st = st[:len(st) - 1]
        }
        st = append(st, i)
        if len(st) == 1 {
            continue
        }
        right[i] = st[len(st) - 2]
    }
    var max int64
    for i := 0; i < len(A); i++ {
        if int64(left[i]) * int64(right[i]) > max {
            max = int64(left[i]) * int64(right[i])
        }
    }
    return int(max % 1000000007)

}

Python:
    def maxSpecialProduct(self, A):
        n = len(A)
        if n<3:
            return 0
        rightspval = [0]*n
        leftspval = [0]*n
        stack = []

        stack.append(0)
        for i in range(1,n):
            while stack and A[stack[-1]] < A[i]:
                rightspval[stack.pop()] = i
            stack.append(i)
        stack.clear()

        stack.append(n-1)
        for i in range(n-1,-1,-1):
            while stack and A[stack[-1]] < A[i]:
                leftspval[stack.pop()] = i
            stack.append(i)
        del(stack)

        maxi = -1
        for i in range(n):
            maxi = max(maxi, leftspval[i]*rightspval[i])
        return maxi%1000000007

 *
 */
