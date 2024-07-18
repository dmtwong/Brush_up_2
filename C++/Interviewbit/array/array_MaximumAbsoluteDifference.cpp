//============================================================================
// Name        : array_MaximumAbsoluteDifference.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

/*Problem Description
You are given an array of N integers, A1, A2 ,..., AN. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N. f(i, j) is defined as |A[i] - A[j]| + |i - j|, where |x| denotes absolute value of x.
Problem Constraints
1 <= |A| <= 105
-109 <= Ai <= 109
Input Format
The first argument is an integer array A.
Output Format
Return an integer equal to the maximum value of f(i, j)
Example Input
A = [1, 3, -1]
Example Output
5
Example Explanation
Given A = [1, 3, -1],
f(1, 1) = f(2, 2) = f(3, 3) = 0
f(1, 2) = f(2, 1) = |1 - 3| + |1 - 2| = 3
f(1, 3) = f(3, 1) = |1 - (-1)| + |1 - 3| = 4
f(2, 3) = f(3, 2) = |3 - (-1)| + |2 - 3| = 5
The maximum value is 5, which is of f(2, 3)
 *
 */

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
	//int Solution::maxArr(vector<int> &A) {
	int maxArr(vector<int> &A) {
	    int max1 = INT_MIN, min1 = INT_MAX;
	    int max2 = INT_MIN, min2 = INT_MAX;
	    int n_A = A.size();
	    for (int i = 0; i < n_A; i++) {
	        max1 = max(max1, A[i] + i);
	        min1 = min(min1, A[i] + i);
	        max2 = max(max2, A[i] - i);
	        min2 = min(min2, A[i] - i);
	    }

	    return max(max1 - min1, max2 - min2);

		//int max_1 = A[0] + i;
		//int max_2 = A[0] - i;
		/*
		int max_1 = A[0];
		int max_2 = max_1;
		int min_1 = max_1;
		int min_2 = min_1;
		int n_A = A.size();
		int result;
		for (int i = 0; i < n_A; i++){
			max_1 = max(max_1, A[i] + i);
			max_2 = max(max_2, A[i] - i);
			min_1 = max(min_1, A[i] + i);
			min_2 = max(min_2, A[i] - i);
		}
		result = max(max_1 - min_1, max_2 - min_2);
		return result;
		*/
	}
}

/*int Solution::maxArr(vector<int> &A) {
    int ans = 0, n = A.size();

    int max1 = INT_MIN, max2 = INT_MIN;
    int min1 = INT_MAX, min2 = INT_MAX;

    for(int i = 0; i < n; i++){
        max1 = max(max1, A[i] + i);
        max2 = max(max2, A[i] - i);
        min1 = min(min1, A[i] + i);
        min2 = min(min2, A[i] - i);
    }
    ans = max(ans, max2 - min2);
    ans = max(ans, max1 - min1);
    return ans;
}


    def maxArr(self, a):
        n = len(a)
        ap = [a[i] + i for i in range(n)]
        am = [a[i] - i for i in range(n)]
        return max(max(ap) - min(ap), max(am) - min(am))

    def maxArr(A: Array[Int]): Int  = {
        var max1 = Int.MinValue
        var max2 = Int.MinValue
        var min1 = Int.MaxValue
        var min2 = Int.MaxValue
        for {
            i <- A.indices
            ai = A(i)
        } {
            max1 = math.max(max1, ai + i)
            max2 = math.max(max2, ai - i)
            min1 = math.min(min1, ai + i)
            min2 = math.min(min2, ai - i)
        }
        math.max(math.max(0, max2 - min2), max1 - min1)
    }

    func maxArr(A []int )  (int) {
    max_diff, mx1,mn1, mx2, mn2 := 0,0,0,0,0
    arr1, arr2:= make([]int,0), make([]int,0)

    if len(A) <2 {
        return 0
    }

    for i:= 0; i< len(A); i++ {
        arr1 = append(arr1, A[i]+i)
        arr2 = append(arr2, A[i]-i)
    }
    mn1, mx1 = arr1[0], arr1[0]
    mn2, mx2 = arr2[0], arr2[0]
    for i:= 1; i< len(A); i++ {
        if mx1<arr1[i] {
            mx1 = arr1[i]
        }
        if mx2<arr2[i] {
            mx2 = arr2[i]
        }
        if arr1[i]<mn1 {
            mn1 = arr1[i]
        }
        if arr2[i]<mn2 {
            mn2 = arr2[i]
        }
    }
    t1 := mx1-mn1
    t2 := mx2-mn2

    if t1 < 0 {
        t1*= -1
    }

    if t2 < 0 {
        t2*= -1
    }

    if t1 > t2 {
        max_diff = t1
    } else {
        max_diff = t2
    }
    return max_diff

}

 *
 */
