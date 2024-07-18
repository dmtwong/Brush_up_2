//============================================================================
// Name        : math_findDigitsInBinary.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

/*
 * Given a number N >= 0, find its representation in binary.
Example:
if N = 6,
binary form = 110
Problem Approach:
Complete code in the hint.
 */
int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	//string Solution::findDigitsInBinary(int A) {
	string findDigitsInBinary(int A) {
		string result = "";
		if (A == 0){
			return "0";
		}
		while (A!=0){
			result = to_string(A%2) + result;
			A = A/2;
		}
		return result;

	}

	return 0;
}

/*
 * string Solution::findDigitsInBinary(int A) {
    if(A == 0) return "0";
    string sol = "";
    while(A > 0) sol = (char)((A&1)+'0') + sol, A >>= 1;
    return sol;
}

    def findDigitsInBinary(self, a: int) -> str:
        if a == 0:
            return '0'

        res = ''

        while a > 0:
            res += '1' if ((a & 1) == 1) else '0'
            a >>= 1

        return res[::-1]

    def findDigitsInBinary(A: Int): String  = {
        if (A == 0) "0"
        else {
            var list = Seq[Int]()
            var num = A
            while (num > 0) {
                val reminder = num % 2
                list = list :+ reminder
                num = num / 2
            }
            list.reverse.mkString("")
        }
    }

func findDigitsInBinary(A int )  (string) {
	if A == 0 {
		return "0"
	}
	res := ""
	for A / 2 != 0 {
		rem := A % 2
		if rem == 1 {
			res += "1"
		} else {
			res += "0"
		}
		A /= 2
	}
	if A == 1 {
		res += "1"
	}
	str := []rune(res)
	for i := 0; i < len(res) / 2; i++ {
		str[i], str[len(res) - i - 1] = str[len(res) - i - 1], str[i]
	}

	return string(str)
}
 */
