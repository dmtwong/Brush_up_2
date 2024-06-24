//============================================================================
// Name        : hash_SubarrayWithBoddNumbers.cpp
// Author      : NDavid W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	// int Solution::solve(vector<int> &A, int B) {
	int solve(vector<int> &A, int B) {
		int n_A = A.size();
		int odd = 0;
		int prefix[n_A + 1] = {0};
		// int cur = 0;
		int result = 0;

		for (int i = 0; i < n_A; i++){
			prefix[odd]++;
			// return prefix[odd];

			if (A[i]%2 == 1){
				odd++;
			}
			if (odd >= B){
				result += prefix[odd - B];
			}
		}
		return result;
	}

	return 0;
}}

/*
 * int Solution::solve(vector<int> &A, int B) {
    int n = A.size();
    int count = 0;
    int prefix[n+1];
    memset(prefix, 0, sizeof(prefix));
    int odd = 0;
    // traverse in the array
    for (int i = 0; i < n; i++)
    {

      prefix[odd]++;
      // if array element is odd
      if (A[i] & 1)
          odd++;

      // when number of odd elements>=M
      if (odd >= B)
          count += prefix[odd - B];
    }
    return count;

}

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        count = 0
        prefix = [0] * (n+1)
        odd = 0;
    # traverse in the array
        for i in range(n):
            prefix[odd] += 1
        # if array element is odd
            if (A[i] & 1):
                odd+=1

        # when number of odd elements>=M
            if (odd >= B):
                count += prefix[odd - B]
        return count
   func solve(A []int , B int )  (int) {
    if len(A) < B {
        return 0
    }
    odd := make([]int, 0, 10)

    for i, v := range A {
        if v%2 != 0 {
            odd = append(odd, i)
        }
    }

    fEven := 0
    lEven := -1
    i := 0
    sum := 0

    for i+B <= len(odd) {
        if B > 0 {
            if i == 0 {
                fEven = odd[i]
            } else {
                fEven = odd[i] - odd[i-1] - 1
            }

            if i+B == len(odd) {
                lEven = len(A) - odd[i+B-1] - 1
            } else {
                lEven = odd[i+B] - odd[i+B-1] - 1
            }
            sum += fEven + fEven*lEven + lEven + 1
        } else {
            if i == len(odd) {
                if len(odd) > 0 {
                    fEven = len(A) - 1 - odd[i-1]
                } else {
                    fEven = len(A)
                }
            } else if i == 0 {
                fEven = odd[i]
            } else {
                fEven = odd[i] - odd[i-1] - 1
            }
            sum += (fEven * (fEven + 1)) / 2
        }
        i++
    }
    return sum
}

 */
