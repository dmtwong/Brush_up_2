//============================================================================
// Name        : math_VerifyPrime.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	// int Solution::isPrime(int A) {

	int Solution::isPrime(int A) {
	    int end_ix = int(A / 2);
	    if (A == 0 || A == 1){
	        return 0;
	    }
	    if (A < 0){
	        A = -1 * A;
	    }
	    for (int i = 2; i <= end_ix; i++){
	        if (A % i == 0){
	            return 0;
	        }
	    }
	    return 1;
	}


	return 0;
}

/*
 * int Solution::isPrime(int A) {
    if(A==1) return 0;
    for(int i=2 ; i*i<=A ; i++)
        if(A%i==0) return 0;
    return 1;
}

Scala:
0

0
class Solution {
    def isPrime(A: Int): Int  = {
        if (A<2)
            return 0
        val sqrtA = math.sqrt(A).toInt
        for (i <- 2 to sqrtA) {
            if (A%i==0) {
                return 0
            }
        }
        1
    }
}
GO:
import "math"

func isPrime(a int) int {
	if a <= 1 {
		return 0
	}

	for i := 2; i <= int(math.Sqrt(float64(a))); i++ {
		if a % i == 0 && a != i {
			return 0
		}
	}
	return 1
}

Python
import math

class Solution:
	# @param A : integer
	# @return an integer
	def isPrime(self, A):

	    A = abs(A)

	    # Special cases
	    if A == 1:
	        return 0
	    if A == 2:
	        return 1

	    # If even (expect 2 itself), not prime.
	    if A % 2 == 0:
	        return 0

	    # Try odd divisors.
	    # NB: we could optimize by trying prime divisors only.
	    for x in range(3, int(math.sqrt(A)) + 1, 2):
	        if A % x == 0:
	            return 0
	    return 1
 */
