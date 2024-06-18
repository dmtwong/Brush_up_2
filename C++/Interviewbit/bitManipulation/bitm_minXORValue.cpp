//============================================================================
// Name        : bitm_minXORValue.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	//int Solution::findMinXor(vector<int> &A) {
	int findMinXor(vector<int> &A) {
		sort(A.begin(), A.end());
		int n_A = A.size();
		int result= 2147483647;
		int cur_xor;
		for (int i = 0; i < n_A; i++){
			cur_xor = A[i] ^ A[i+1];
			cur_xor = abs(cur_xor);
			if (result > cur_xor){
				result = cur_xor;
			}
		}
		return result;
	}

	return 0;
}

/*
 * Given an integer array A of N integers, find the pair of integers in the array which have minimum XOR value. Report the minimum XOR value.
Input Format:

    First and only argument of input contains an integer array A
Output Format:

    return a single integer denoting minimum xor value
Constraints:

2 <= N <= 100 000
0 <= A[i] <= 1 000 000 000
For Examples :

Example Input 1:
    A = [0, 2, 5, 7]
Example Output 1:
    2
Explanation:
    0 xor 2 = 2
Example Input 2:
    A = [0, 4, 7, 9]
Example Output 2:
    3
 */

/* Editorial
 *
 * int Solution::findMinXor(vector<int> &numbers) {
    sort(numbers.begin(), numbers.end());
    int smallestXor = numbers[0] ^ numbers[1];
    for (int i = 2; i < numbers.size(); i ++) {
        smallestXor = min(smallestXor, numbers[i - 1] ^ numbers[i]);
    }
    return smallestXor;
}
Scala:
class Solution {
    def findMinXor(A: Array[Int]): Int  = {
        A.sorted.sliding(2).map(arr => arr(1) ^ arr(0)).min
    }
}

Python:
    def findMinXor(self, A):
        s = sorted(A)
        minn = s[0]^s[1]
        for i in range(1,len(A)):
            if(s[i]^s[i-1]<minn):
                minn = s[i]^s[i-1]
        return minn

GO:
import(
    "math"
    "sort"
)

func findMinXor(numbers []int ) (int) {
	sort.Ints(numbers)
	minXor := math.MaxInt32
	for i := 0; i < len(numbers) -1; i++ {
		nextXor := numbers[i] ^ numbers[i + 1]
		if nextXor < minXor {
			minXor = nextXor
		}
	}

	return minXor
}

 */
