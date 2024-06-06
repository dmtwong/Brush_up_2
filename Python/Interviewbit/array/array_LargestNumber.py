# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 10:27:45 2024

@author: USER
"""

# Problem Description

# Given a list of non-negative integers, arrange them such that they form the largest number.
# Note: The result may be very large, so you need to return a string instead of an integer.

# Problem Constraints
# 1 <= |A| <= 105
# 0 <= Ai <= 109

# Input Format
# The first argument is an integer array A.

# Output Format
# Return a string representing the largest number formed

# Example Input
A = [3, 30, 34, 5, 9]
A = [8, 89]
largestNumber(A)
A = [ 0, 0, 0, 0, 0 ]

# Example Output
# 9534330

# Example Explanation
# Largest possible number that can be formed is 9534330
# class Solution:
#     # @param A : tuple of integers
#     # @return a strings
#     def largestNumber(self, A):
    
def largestNumber(A):
    from functools import cmp_to_key
    def compare_gt(num_1, num_2):
        temp_1, temp_2 = num_1, num_2
        n_1, n_2 = len(str(num_1)), len(str(num_2))
        n_Test = min(n_1, n_2)
        cur_dict = {num_1 : [num_1], num_2 : [num_2]}#[num_1], num_2 = [num_2]}# , n_1], num_2 = [num_2, n_2]}
        while temp_1 > 0:
            cur_dict[num_1].insert(0, temp_1 % 10)
            temp_1 //= 10
        while temp_2 > 0:
            cur_dict[num_2].insert(0, temp_2 % 10)
            temp_2 //= 10
        ix = 0
        for i in range(n_Test):
            if cur_dict[num_1][i] > cur_dict[num_2][i]:
                return 1 
            elif cur_dict[num_1][i] < cur_dict[num_2][i]:
                return -1
            else:
                ix += 1
        j, k = 0, 0 
        if n_1 > n_2:
            while k < n_1:
                if  cur_dict[num_1][k] >  cur_dict[num_2][j]:
                    return 1
                elif  cur_dict[num_1][k] <  cur_dict[num_2][j]:
                    return -1
                else:
                    if j == n_2 - 1: 
                        j = 0
                        k += 1
                        continue
                j += 1
                k += 1
            while j != n_Test:
                if cur_dict[num_1][k-1] > cur_dict[num_2][j]:
                    return 1
                elif cur_dict[num_1][k-1] < cur_dict[num_2][j]:
                    return -1
                else:
                    j += 1
        elif n_1 < n_2:
            while k < n_2:
                if cur_dict[num_1][j] > cur_dict[num_2][k]:
                    return 1
                elif cur_dict[num_1][j] < cur_dict[num_2][k]:
                    return -1
                else:
                    if j == n_1 - 1: 
                        j = 0
                        k += 1
                        continue
                j += 1
                k += 1
            while j != n_Test:
                if cur_dict[num_1][j] > cur_dict[num_2][k-1]:
                    return 1
                elif cur_dict[num_1][j] < cur_dict[num_2][k-1]:
                    return -1
                else:
                    j += 1
        return 1 
    # print(A)
    # print(cmp_to_key(compare_gt))
    A.sort(key = cmp_to_key(compare_gt), reverse = True)
    # print(A)
    A = [str(x) for x in A]
    if A[0] == '0':
        return '0'
    return ''.join(A)

# # #     # Editoral:
# # # # Python:
               
# from functools import cmp_to_key

# class Solution:
# 	# @param A : tuple of integers
# 	# @return a strings
# 	def largestNumber(self, A):
# 	    ''' When comparing numbers we must pick the one leading
# 	        to the best concatenated result:
# 	        787978 > 787879  so 7879 is 'bigger' than 78
# 	                    but     7879 is 'less' than 788
# 	    '''
# 	    
# 	    # Convert to string once, for proper comparison a+b vs b+a
# 	    A = map(str, A)
# 	    key = cmp_to_key(lambda a,b: 1 if a+b >= b+a else -1)
# 	    res = ''.join(sorted(A, key= key, reverse=True))
# 	    # Must left trim 0, apparently
# 	    res = res.lstrip('0')
# 	    return res if res else '0'

# C++:
#     bool compareNum(string a, string b) {
#     return a + b > b + a;
# }
# string Solution::largestNumber(const vector < int > & A) {
#     string result;
#     vector < string > str;
#     assert(A.size() >= 1 && A.size() <= 1e5);
#     for (int i = 0; i < A.size(); i++) {
#         assert(A[i] >= 0 && A[i] <= 1e9);
#         str.push_back(to_string(A[i]));
#     }
#     sort(str.begin(), str.end(), compareNum);
#     for (int i = 0; i < str.size(); i++) {
#         result += str[i];
#     }

#     int pos = 0;
#     while (result[pos] == '0' && pos + 1 < result.size()) pos++;
#     return result.substr(pos);
# }

# Scala:
#     class Solution {
#     def largestNumber(A: Array[Int]): String  = {
#       if (A.forall(_ == 0)) "0"
#       else {
#         A.map(_.toString).sortWith {
#           case (l, r) => {
#             val ll = l + r
#             val rr = r + l
#             rr > ll
#           }
#         }.reverse.mkString("")
#       }
#     }
# }


# GO:
#     /**
#  * @input A : Read only ( DON'T MODIFY ) Integer array
#  * @input n1 : Integer array's ( A ) length
#  * 
#  * @Output string.
#  */
 
# import "sort"
# import "strconv"
# //import "fmt"

# type dictInt []int

# func (s dictInt) Less(i, j int) bool {
#     s1 := strconv.Itoa(s[i])
#     s2 := strconv.Itoa(s[j])
#     return s1 + s2 < s2 + s1
# }

# func (s dictInt) Len() int {
#     return len(s)
# }

# func (s dictInt) Swap(i, j int) {
#     s[i], s[j] = s[j], s[i]
# }

# func largestNumber(A []int )  (string) {
    
#     b := A

# //    fmt.Println("Unsorted: ", b)

#     sort.Sort(sort.Reverse(dictInt(b)))
# //    fmt.Println("Sorted: ", b)

#     lNum := ""

#     if (b[len(b) - 1] == 0) {
#         return "0";
#     }
    
#     for _, v := range b {
#         lNum += strconv.Itoa(v)
#     }
    
#     return lNum
# }
