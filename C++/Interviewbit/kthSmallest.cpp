//============================================================================
// Name        : kthSmallest.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

// Note to self: below code exceed time limit as ttrying to using constant space; another approach using min heap works if extra spaces are used:
/*  priority_queue<int,  vector<int>, greater<int>> pq;
    for (auto it: A){
        pq.push(it);
    }

    while(--B){
        pq.pop();
    }
    return pq.top();
 *
 *
 */

/*
 * Find the Bth smallest element in an unsorted array of non-negative integers A.
Definition of kth smallest element: The kth smallest element is the minimum possible n such that there are at least k elements in the array <= n.
In other words, if the array A was sorted, then Ak - 1
NOTE: You are not allowed to modify the array (The array is read-only). Try to do it using constant extra space.
Problem Constraints
1 <= |A| <= 106
1 <= B <= |A|
1 <= A[i] <= 109
Input Format
The first argument is an integer array A.
The second argument is integer B.

Output Format
Return the Bth smallest element in given array.

Example Input
Input 1:
A = [2, 1, 4, 3, 2]
B = 3
Input 2:
A = [1, 2]
B = 2
Example Output
Output 1:
 2
Output 2:
 2
 *
 */
#include <iostream>
#include <vector>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	//int Solution::kthsmallest(const vector<int> &A, int B) {
	int kthsmallest(const vector<int> &A, int B) {
		int n_A = A.size();
		    if (B > n_A){
		        return NULL;
		    }
		    int up = *max_element(A.begin(), A.end());
		    int bm = *min_element(A.begin(), A.end());
		    int mid;
		    int count_sm = 0;
		    int count_eq = 0;
		    int ix;
		    int count = 0;
		    while (bm <= up){
		        count += 1;
		        mid = bm + (up-bm)/2;
		        // return mid;
		        //if (count ==25){
		          //  return mid;
		        //}
		        for (int i = 0; i < n_A; i++){
		            if (A[i] < mid){
		                count_sm += 1;
		            } else if  (A[i] == mid){
		                count_eq += 1;
		            }
		        }
		        //if (count == 3){
		        //    return count_sm;
		        //}
		        //return count_sm;
		        if (count_sm > B){
		            up = mid - 1;
		        } else if (count_sm < B){
		            if (count_sm + count_eq >= B){
		                //return count_eq;
		                mid;
		            } else {
		                bm = mid + 1;
		            }
		        }
		        count_sm = 0;
		        count_eq = 0;
		        //else {
		            //return 123;
		            //break;
		        //}
		    }
		    //return count; # 6 times
		    return mid;
		    //if (count_sm == B){
		      //      return mid;
		    //}
		    /*
		    return count_sm;
		    auto it = find(A.begin(), A.end(), mid);
		    ix = it - A.begin();
		    return A[ix];
		            if (ix >= 0){
		                //return A[ix];
		            } else {
		                it = find_if(A.begin(), A.end(), [mid] (int ele) {return (mid < ele);});
		                ix = it - A.begin();
		               // return A[ix];
		            }

		    }
		    */

		}
	return 0;
}
