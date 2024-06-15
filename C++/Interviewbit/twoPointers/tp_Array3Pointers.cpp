//============================================================================
// Name        : tp_Array3Pointers.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

int main() {
	//int Solution::minimize(const vector<int> &A, const vector<int> &B, const vector<int> &C) {
	int minimize(const vector<int> &A, const vector<int> &B, const vector<int> &C) {
	    int ix_i = 0;
	    int ix_j = 0;
	    int ix_k = 0;
	    int res_i = 0;
	    int res_j = 0;
	    int res_k = 0;
	    int n_I = A.size();
	    int n_J = B.size();
	    int n_K = C.size();
	    int temp_diff = 2147483647;
	    int cur_min, cur_max;
	    while (ix_i < n_I && ix_j < n_J && ix_k < n_K){
	        cur_min = min(A[ix_i], min(B[ix_j], C[ix_k]));
	        cur_max = max(A[ix_i], max(B[ix_j], C[ix_k]));
	        if (cur_max - cur_min < temp_diff){
	                res_i = ix_i, res_j = ix_j, res_k = ix_k;
	                temp_diff = cur_max - cur_min;
	        }
	        if (temp_diff == 0) break;
	        if (A[ix_i] == cur_min){
	            ix_i++;
	        } else if (B[ix_j] == cur_min){
	            ix_j++;
	        }
	        else{
	            ix_k++;
	        }
	    }
	    return temp_diff;
	}
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	return 0;
}

/*
 * You are given 3 arrays A, B and C. All 3 of the arrays are sorted.
Find i, j, k such that :
max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i])) is minimized.
Return the minimum max(abs(A[i] - B[j]), abs(B[j] - C[k]), abs(C[k] - A[i]))
**abs(x) is absolute value of x and is implemented in the following manner : **
      if (x < 0) return -x;
      else return x;
Example :
Input :
        A : [1, 4, 10]
        B : [2, 15, 20]
        C : [10, 12]
Output : 5
         With 10 from A, 15 from B and 10 from C.
 */

/* Editoral
 * int Solution::minimize(const vector<int> &A, const vector<int> &B, const vector<int> &C) {
    int ans = INT_MAX;
    int i = 0, j = 0, k = 0;
    while(i<A.size() && j<B.size() && k<C.size()) {
        int high_no = max(A[i], max(B[j], C[k]));
        int low_no = min(A[i], min(B[j], C[k]));
        (A[i] == low_no)?i++:(B[j] == low_no)?j++:k++;
        ans = min(ans, high_no-low_no);
    }
    return ans;
}

Scala
class Solution {
    def minimize(A: Array[Int], B: Array[Int], C: Array[Int]): Int  = {
      def abs(x: Int) = if (x < 0) -x else x

      def calcMin(a: Int, b: Int, c: Int): Int = {
        val x = abs(a - b)
        val y = abs(b - c)
        val z = abs(c - a)
        math.max(x, math.max(y, z))
      }

      var res = Int.MaxValue
      var ai, bi, ci = 0
      while (ai < A.length && bi < B.length && ci < C.length) {
        val aa = A(ai)
        val bb = B(bi)
        val cc = C(ci)
        res = math.min(res, calcMin(aa, bb, cc))

        val ii = Array(
          (0, aa, ai < A.length),
          (1, bb, bi < B.length),
          (2, cc, ci < C.length)
        ).filter(_._3).minBy(_._2)._1
        if (ii == 0) ai = ai + 1
        else if (ii == 1) bi = bi + 1
        else if (ii == 2) ci = ci + 1
      }
      res
    }
}
GO:
import "math"

func minimize(A []int , B []int , C []int) (int) {
    ret := math.MaxInt32
    i, j, k := 0, 0, 0
    for i < len(A) && j < len(B) && k < len(C) {
        ab := abs(A[i] - B[j])
        bc := abs(B[j] - C[k])
        ca := abs(C[k] - A[i])
        x := max(max(ab, bc), ca)
        if x < ret {
            ret = x
        }
        if x == ab && A[i] < B[j] {
            i++
        } else if x == ab || (x == bc && B[j] < C[k]) {
            j++
        } else if x == bc || (x == ca && C[k] < A[i]) {
            k++
        } else {
            i++
        }
    }
    return ret
}

func abs(x int) int {
    if x < 0 {
        return -x
    }
    return x
}

func max(x, y int) int {
    if x > y {
        return x
    }
    return y
}

Python:
    def minimize(self, A, B, C):
        pA = 0
        pB = 0
        pC = 0
        minmax = float("inf")
        while pA < len(A) and pB < len(B) and pC < len(C):
            minmax = min(minmax, max(abs(A[pA] - B[pB]), abs(B[pB] - C[pC]), abs(C[pC] - A[pA])))
            if A[pA] == min(A[pA], B[pB], C[pC]):
                pA += 1
            elif B[pB] == min(A[pA], B[pB], C[pC]):
                pB += 1
            else:
                pC += 1

        return minmax
 *
 *
 */
