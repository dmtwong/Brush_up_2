//============================================================================
// Name        : sq_FirstnonRepeatingChar.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

// Note: failed to encounter possible cancellation when the current top is removed; see the python solution for review

#include <iostream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	//string Solution::solve(string A) {
	string solve(string A) {


		// queue<char> q_char;
		deque<char> dq_char;
		string result;
		char cur_i;
		char first_non;
		int n_A = A.length();
		// int n_dq;
		deque<int>::iterator itr;

		for (int i = 0; i < n_A; i++){
			cur_i = A[i];
			if (dq_char.front() == cur_i){
				dq_char.pop_front();
	//			while (dq_char.size() > 1 && find(dq_char.begin(), dq_char.end(), dq_char.front()) != dq_char.end()){
			//		dq_char.pop_front();
		//			dq_char.pop_back();
				}
			} else {
				dq_char.push_back(cur_i);
			}
			// dq_char.empty()
			//n_dq = dq_char.size();
			//while (dq_char.size() > 1 && find(dq_char.begin(), dq_char.end(), dq_char.front()) != dq_char.end()){
				//dq_char.pop_front();
				//dq_char.pop_back();
			//}

			if (dq_char.size() == 0){
				result += '#';

			//} else if (n_dq > 1) {
			//	while (dq_char.front() == dq_char.back()){
				//	dq_char.pop_front();
					//dq_char.pop_back();
				//}
			//	if (dq_char.size() == 0){
			//		result += '#';
			//	} else {
			//		result += dq_char.front();
		//		}
			} else {
				result += dq_char.front();
			}

		}
		return result;
	}

	return 0;
}

/*
jyhrcwuengcbnuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl
jjjjjjjjjjjjjjjjjjjjjyyyyyyyyyyyyyyyyyyyyyyyyyyyhhhhh
jjjjjjjjjjjjjjjjjjjjjyyyyyyyyyyyyyyyyyyyyyyyyyyyqqqqq

jyhrcwuengcbnuchctlux
jgtxqtfvrebveewgasluuwooupc
yxwgl

jyhrcwuengcb
nuchctluxjgtxqtfvrebveewgasluuwooupcyxwgl
*/
/*
 * Problem Description
Given a string A denoting a stream of lowercase alphabets. You have to make new string B.
B is formed such that we have to find first non-repeating character each time a character is inserted to the stream and append it at the end to B. If no non-repeating character is found then append '#' at the end of B.

Problem Constraints
1 <= length of the string <= 100000

Input Format
The only argument given is string A.

Output Format
Return a string B after processing the stream of lowercase alphabets A.

Example Input
Input 1:
 A = "abadbc"
Input 2:
 A = "abcabc"
Example Output
Output 1:
 "aabbdd"
Output 2:
 "aaabc#"
Example Explanation
Explanation 1:
    "a"      -   first non repeating character 'a'
    "ab"     -   first non repeating character 'a'
    "aba"    -   first non repeating character 'b'
    "abad"   -   first non repeating character 'b'
    "abadb"  -   first non repeating character 'd'
    "abadbc" -   first non repeating character 'd'
Explanation 2:
    "a"      -   first non repeating character 'a'
    "ab"     -   first non repeating character 'a'
    "abc"    -   first non repeating character 'a'
    "abca"   -   first non repeating character 'b'
    "abcab"  -   first non repeating character 'c'
    "abcabc" -   no non repeating character so '#'
 */


/* :
 string Solution::solve(string s) {
    vector<int> v(26, 0);
    queue<char> q;
    int n =s.length();
    string ans="";
    for(int i=0; i<n; i++){
        if(v[s[i]-'a']==0)q.push(s[i]);
        v[s[i]-'a']++;
        while(!q.empty() && v[q.front()-'a']>1 )q.pop();
        if(!q.empty())ans+=q.front();
        else ans+='#';
    }
    return ans;

}

from collections import defaultdict, deque
class Solution:
    # @ returns 0
    def default(x): return 0
    # @param A : string
    # @return a strings
    def solve(self, A):
        chars = defaultdict(self.default)
        ans = ''
        q = deque()

        for char in A:
            q.append(char)
            chars[char] += 1
            while len(q) and chars[q[0]] != 1:
                q.popleft()
            ans += ('#' if not len(q) else q[0])

        return ans

 import scala.collection.mutable._

class Solution {
  def solve(str: String): String  = {
    if (str.isEmpty) {
      return ""
    }

    val q = Queue[Char]()
    val charsFoundSoFar = Map[Char, Int]()

    val result = for (ch <- str) yield {
      if (charsFoundSoFar.contains(ch)) {
        // more than one occurence of char 'ch'
        charsFoundSoFar(ch) = 2

        // find next non-repeating char
        while (q.nonEmpty && charsFoundSoFar(q.front) > 1) {
          q.dequeue
        }
      } else {
        // first occurence of char 'ch'
        charsFoundSoFar(ch) = 1
        q.enqueue(ch)
      }

      if (q.isEmpty) '#' else q.front
    }

    result.mkString
  }
}
 *
 *
 */
