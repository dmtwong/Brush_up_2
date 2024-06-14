//============================================================================
// Name        : string_ReverseTheString.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

/*
 * Problem Description

You are given a string A of size N.

Return the string A after reversing the string word by word.

NOTE:

A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.
 Problem Constraints
1 <= N <= 3 * 105

Input Format
The only argument given is string A.

Output Format
Return the string A after reversing the string word by word.

Example Input
Input 1:
    A = "the sky is blue"
Input 2:
    A = "this is ib"

Example Output
Output 1:
    "blue is sky the"
Output 2:
    "ib is this"

Example Explanation
Explanation 1:
    We reverse the string word by word so the string becomes "the sky is blue".
Explanation 2:
    We reverse the string word by word so the string becomes "this is ib".
 *
 */
#include <iostream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	//string Solution::solve(string A) {
	string solve(string A) {
		int n_A = A.size();
		int i; string result; string wrd;
		int ix_w = 0;
		while (ix_w < n_A){
			// skip white space
			while (A[ix_w] == ' ' && ix_w < n_A){
				ix_w++;
			}
			i = ix_w + 1;
			while (A[i] != ' ' && i < n_A){
				i++;
			}
			wrd = A.substr(ix_w, i-1);
			if (result.size() == 0){
				result = wrd;
			} else {
				result = wrd + ' ' + result;
			}
			ix_w = i + 1;
		}
		return result;
	}

	return 0;
}

/* Above can't pass some cases, below are editor solution:
 * string Solution::solve(string s) {
    string ans = "";
    string cur = "";
    for (int i = s.length() - 1; i >= 0; i--) {
        if (s[i] == ' ') {
            if (cur.length() == 0) {
                continue;
            }
            // found a word
            reverse(cur.begin(), cur.end());
            if (ans.length() > 0) {
                ans.push_back(' ');
            }
            ans += cur;
            cur = "";
            continue;
        }
        cur.push_back(s[i]);
    }
    if (cur.length() > 0) {
        reverse(cur.begin(), cur.end());
        if (ans.length() > 0) {
            ans.push_back(' ');
        }
        ans += cur;
    }
    s = ans;
    return s ;
}


scala:
class Solution {
    def solve(str: String): String  = {
        str.split(" ").reverse.mkString(" ").trim
    }
}

python:
    def solve(self, A):
        return ' '.join(A.strip().split()[::-1])

GO:
type stackString struct {
    s []string
}

func NewStackString() *stackString {
    return &stackString {make([]string,0), }
}

func (s *stackString) Push(v string) {
    s.s = append(s.s, v)
}

func (s *stackString) Pop() (string) {
    l := len(s.s)
    if l == 0 {
        panic("empty stackString access")
    }

    res := s.s[l-1]
    s.s = s.s[:l-1]
    return res
}

func (s *stackString) First() string {
    l := len(s.s)
    return s.s[l-1]
}

func (s *stackString) IsEmpty() bool {
    return len(s.s) == 0
}

func (s *stackString) Size() int {
    return len(s.s)
}

func solve(str string )  (string) {
    stack := NewStackString()
    s := ""

    for i := 0; i < len(str); i++ {
        if str[i] == ' ' {
            stack.Push(s)
            s = ""
        } else {
            s = s + string(str[i])
        }
    }
    stack.Push(s)
    result := ""
    for !stack.IsEmpty() {
        next := stack.Pop()
        result = result + next
        if stack.Size() > 0 {
            result = result + " "
        }
    }
    return result
}

 *
 *
 *
 */
