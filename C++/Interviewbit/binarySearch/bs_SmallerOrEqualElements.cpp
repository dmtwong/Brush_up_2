//============================================================================
// Name        : bs_SmallerOrEqualElements.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	//int Solution::solve(vector<int> &A, int B) {
	int solve(vector<int> &A, int B) {
		int n_A = A.size();
		int lo = 0;
		int hi = n_A - 1;
		int mid;
		int mid_val;
		int result;
        bool findB = false;
        if (A[0] > B){
			return 0;
		}
		if (A[n_A - 1] <= B){
			return n_A;
		}

		while (lo <= hi){
			mid = lo + int((hi - lo)/2);
			if (A[mid] == B){
                findB = true;
				break;
			} else if (A[mid] < B){
				lo = mid + 1;
			} else if (A[mid] > B){
				hi = mid - 1;
			} else {
				break;
			}
		}
        // return mid;
		mid_val = A[mid];
		result = mid + 1;

        while (A[result] == B && result <= n_A){
			result += 1;
		}
        while (findB == true){
            return result;
        }

		if (mid_val != B){
			if (mid_val > B){
                while (mid_val > B){
                    mid -= 1;
                    mid_val = A[mid];
                }
				return mid + 1;
			} else {
                while (mid_val < B){
                    mid += 1;
                    mid_val = A[mid];
                }
				return mid;
			}
		}
	}

	return 0;
}

/*
 * Problem Description
Given an sorted array A of size N. Find number of elements which are less than or equal to B.
NOTE: Expected Time Complexity O(log N)
Problem Constraints
1 <= N <= 106
1 <= A[i], B <= 109
Input Format
First agument is an integer array A of size N.
Second argument is an integer B.
Output Format
Return an integer denoting the number of elements which are less than or equal to B.
Example Input
Input 1:
 A = [1, 3, 4, 4, 6]
 B = 4
Input 2:
 A = [1, 2, 5, 5]
 B = 3
Example Output
Output 1:
 4
Output 2:
 2
Example Explanation
Explanation 1:
 Elements (1, 3, 4, 4) are less than or equal to 4.
Explanation 2:
 Elements (1, 2) are less than or equal to 3.
 */


/* Editorial
 * int Solution::solve(vector<int> &A, int B) {
    int n = A.size();
    int left = 0;
    int right = n - 1;
    int count = 0;

    while (left <= right) {
        int mid = (right + left) / 2;

        // Check if middle element is less than or equal to B
        if (A[mid] <= B) {

            // At least (mid + 1) elements are there whose values are less than or equal to B
            count = mid + 1;
            left = mid + 1;
        }

        // If B is smaller, ignore right half
        else
            right = mid - 1;
    }
    return count;

}

Scala:
class Solution {
    def solve(A: Array[Int], B: Int): Int  = {
        import scala.collection.Searching._
        val ip=A.search(B)
        if(ip.isInstanceOf[InsertionPoint]){
            return ip.insertionPoint
        }else{
            var j=ip.insertionPoint+1
            while(j<A.length && A(j)==B) j+=1
            return j
        }
    }
}

GO:
// import "fmt"

func solve(A []int , B int )  (int) {
    l, r := 0, len(A)

    for l <= r {
        mid := (l+r)/2
        // fmt.Println(mid)

        if mid == 0 || (A[mid-1] <= B && (mid == len(A) || A[mid] > B)) {
            return mid
        } else if A[mid] <= B {
            l = mid+1
        } else {
            r = mid
        }
    }

    return -1
}

Python:
    def solve(self, A, B):
        n = len(A)
        left = 0
        right = n - 1

        count = 0

        while (left <= right):
            mid = int((right + left) / 2)

            # Check if middle element is less than or equal to B
            if (A[mid] <= B):

                # At least (mid + 1) elements are there whose values are less than or equal to key
                count = mid + 1
                left = mid + 1

            # If B is smaller, ignore right half
            else:
                right = mid - 1

        return count
 */
