//============================================================================
// Name        : hash_PairsWithGivenXor.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
/*
 * Problem Description
Given an 1D integer array A containing N distinct integers.
Find the number of unique pairs of integers in the array whose XOR is equal to B.
NOTE:
Pair (a, b) and (b, a) is considered to be same and should be counted once.
Problem Constraints
1 <= N <= 105
1 <= A[i], B <= 107
Input Format
First argument is an 1D integer array A.
Second argument is an integer B.
Output Format
Return a single integer denoting the number of unique pairs of integers in the array A whose XOR is equal to B.

Example Input
Input 1:
 A = [5, 4, 10, 15, 7, 6]
 B = 5
Input 2:
 A = [3, 6, 8, 10, 15, 50]
 B = 5
Example Output
Output 1:
 1
Output 2:
 2
Example Explanation
Explanation 1:
 (10 ^ 15) = 5 1010 ^ 1111 XOR > 0101 == 5
Explanation 2:
 (3 ^ 6) = 5 and (10 ^ 15) = 5
 */

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	// int Solution::solve(vector<int> &A, int B) {
	int solve(vector<int> &A, int B) {
		int n_A = A.size();
		unordered_set<int> hash_int;
		int count = 0;
		for (int i = 0; i < n_A; i++){
			auto iter = hash_int.find(B ^ A[i]);
			if (iter != hash_int.end()){
				count++;
			}
			hash_int.insert(A[i]);
		}
		return count;
	}

	return 0;
}

/*
 * def xorPairCount(arr, n, x):
    result = 0 # Initialize result

    # create empty set that stores the
    # visiting element of array.
    s = set()
    for i in range(0, n):

        # If there exist an element in set s
        # with XOR equals to x^arr[i], that
        # means there exist an element such
        # that the XOR of element with arr[i]
        # is equal to x, then increment count.
        if(x ^ arr[i] in s):
            result = result + 1

        # Make element visited
        s.add(arr[i])
    return result

 * // Returns count of pairs in arr[0..n-1] with XOR
// value equals to x.
int xorPairCount(vector<int>&arr,int x)
{
    int n=arr.size();
    int result = 0; // Initialize result

    // create empty set that stores the visiting
    // element of array.
    // Refer below post for details of unordered_set
    // https://www.geeksforgeeks.org/unorderd_set-stl-uses/
    unordered_set<int> s;

    for (int i=0; i<n ; i++)
    {
        // If there exist an element in set s
        // with XOR equals to x^arr[i], that means
        // there exist an element such that the
        // XOR of element with arr[i] is equal to
        // x, then increment count.
        if (s.find(x^arr[i]) != s.end())
            result++;

        // Make element visited
        s.insert(arr[i]);
    }

    // return total count of pairs with XOR equal to x
    return result;
}
int Solution::solve(vector<int> &A, int B) {
    return xorPairCount(A,B);
}


class Solution {
  import scala.collection.mutable
  def solve(A: Array[Int], B: Int): Int  = {
    var ans = 0
    val hash = new mutable.HashSet[Int]()
    for(n <- A) {
      if(hash.contains(n ^ B)) ans += 1 else hash += n
    }
    ans
  }
}

func solve(A []int , B int )  (int) {
    m := make(map[int]bool)
    ans := 0
    for _, a := range A {
        if _, ok := m[B^a]; ok {
            ans ++
        }
        m[a] = true
    }
    return ans
}
 */
