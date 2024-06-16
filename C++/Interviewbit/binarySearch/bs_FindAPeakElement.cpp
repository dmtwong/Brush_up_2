//============================================================================
// Name        : bs_FindAPeakElement.cpp
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
	int Solution::solve(vector<int> &A) {
		int n_A = A.size();
		int ix = 0;
		int ix_rev = n_A - 1;
		int mid;
		int result = -1;

		while (ix <= ix_rev){
			mid = ix + (ix_rev - ix) / 2;
			if ((mid == 0 || A[mid] >= A[mid -1]) && (mid == n_A - 1 || A[mid] >= A[mid + 1])){
				return A[mid];
			}
			if (mid == 0 || (A[mid] >= A[mid - 1])){
				ix = mid + 1;
			} else {
				ix_rev = mid - 1;
			}
		}
		return result;
	}
	return 0;
}

/*
 * Given an array of integers A, find and return the peak element in it.
An array element is peak if it is NOT smaller than its neighbors.
For corner elements, we need to consider only one neighbor.
For example, for input array {5, 10, 20, 15}, 20 is the only peak element.
Following corner cases give better idea about the problem.
1) If input array is sorted in strictly increasing order, the last element is always a peak element.
For example, 5 is peak element in {1, 2, 3, 4, 5}.
2) If input array is sorted in strictly decreasing order, the first element is always a peak element.
10 is the peak element in {10, 9, 8, 7, 6}.
Note: It is guranteed that the answer is unique.

Input Format

The only argument given is the integer array A.
Output Format

Return the peak element.
Constraints

1 <= length of the array <= 100000
1 <= A[i] <= 10^9
For Example

Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    5

Input 2:
    A = [5, 17, 100, 11]
Output 2:
    100
 *
 */

/* Editorial
 *class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        nums = A
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l+r) // 2
            if nums[mid] > nums[mid + 1]:
                r = mid
            else:
                l = mid + 1

        return nums[l]


 GO:

func solve(A []int )  (int) {
    if len(A) == 1 {
        return A[0]
    }
    peak  := 0
    for i := 0;  i < len(A); i++ {
        if i == 0 {
            if  A[i] >= A[i+1] {
                peak = A[i]
            }

        } else if i == len(A) - 1 {
            if A[i] >= A[i-1] {
                peak = A[i]
            }
        } else if A[i] >= A[i-1] && A[i+1] <= A[i] {
            peak = A[i]
        }

    }
    return peak
}

 *
 */
