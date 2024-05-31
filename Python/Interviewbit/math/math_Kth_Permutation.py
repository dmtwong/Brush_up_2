# -*- coding: utf-8 -*-
"""
Created on Fri May 31 11:14:31 2024

@author: USER
"""

# Problem Description

# You are given an integer A which represents the length of a permutation.
#  A permutation is an array of length A where all the elements occur exactly once and in any order.
#  For example, [3, 4, 1, 2], [1, 2, 3] are examples of valid permutations while [1, 2, 2], [2] are not.

# You are also given an integer B.
#  If all the permutation of length A are sorted lexicographically, return the Bth permutation.

# Problem Constraints

# 1 <= A <= 105
# 1 <= B <= min(1018, A!), where A! denotes the factorial of A.


# Input Format

# The first argument is the integer A.
# The second argument is the long integer B.


# Output Format

# Return an array denoting the Bth permutation of length A.


# Example Input
# Input 1:
# A = 3
# B = 3
# Input 2:
# A = 1
# B = 1

# Example Output
# Output 1:
# [2, 1, 3]
# Output 2:
# [1]
#  Example Explanation

# Explanation 1:
 
# All the permutations of length 3 sorted in lexicographical order are:
# [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
# Therefore, the third permutation is [2, 1, 3].
# Explanation 2:
# There is only one possible permutation -> [1].


# class Solution:
#     # @param A : integer
#     # @param B : long
#     # @return a list of integers
#     def findPerm(self, A, B):
def findPerm(A, B):         
    # from itertools import permutations  
    # result = list(permutations(range(1, A+1)))
    # # result.sort()
    # # if B < 1018
    # # print(result) 
    # return list(result[B-1])
    from itertools import islice, permutations, combinations
    from itertools import count
    def gen_permutations(source, A):
        n_A = A
        isource = iter(source)
        base = tuple(islice(isource, n_A -1))

        for x in isource:
            for subset in combinations(base, n_A - 1):
                for perm in permutations(subset + (x,), n_A):
                    yield perm
            base += (x,)
    ix = 0
    for p in gen_permutations(count(1), A):
        if ix == B - 1:            
            break
        ix += 1
    return list(p)
        
findPerm(3, 3)
findPerm(1, 1)
findPerm(11, 28) #solved: Memory Limit Exceeded. Expected: 1 2 3 4 5 6 8 7 10 11 9  [1, 2, 3, 4, 5, 6, 8, 7, 11, 9, 10]
findPerm(10**5, 1038) 
findPerm(11, 107145)# Time Limit Exceeded. # 1 2 5 9 4 10 11 6 7 3 8 

# j = n-1; loop = 1, loop_left = loop, i = j + loop
# 1,2,3,4,5 <- Defualt
# 1,2,3, 5, 4 <- A[i], A[i + loop_left] = A[i + loop_left], A[i], loop_left -= 1 
# check loop_left, if loop_left == 0, reset following: 
    # j = n-1, loop += 1, loop_left = loop_left, and default [1,2,3,4,5]
# 


##############################
# Fastest:
    # class Solution:
    # # @param A : integer
    # # @param B : long
    # # @return a list of integers
    # def findPerm(self, A, B):
    #     B -= 1
    #     fact = [1]*21
    #     for i in range(1,21):
    #         fact[i] = fact[i-1]*i
    #     ans = []        
    #     arr = [i+1 for i in range(min(A,20))]
    #     for i in range(min(19,A-1),-1,-1):
    #         x = B // fact[i]
    #         # print (B,i,x,arr)
    #         B = B - x*fact[i]
    #         ans.append(arr[x])
    #         del arr[x]
    #     if A > 20:
    #         return [i+1 for i in range(A-20)] + [x+(A-20) for x in ans]
    #     return ans
# Editoral:
    # Python
# class Solution:
    # # @param A : integer
    # # @param B : long
    # # @return a list of integers
    # def findPerm(self, A, B):
    #     fact = [0]*21
    #     fact[0] = 1
    #     for i in range(1, 21):
    #         fact[i] = i * fact[i - 1]
        
    #     ans = [0]*A
    #     curr = 0
    #     for i in range(A-20):
    #         ans[i] = i + 1
    #         curr = i
        
    #     l1 = []
    #     for i in range(max(A - 20, 1), A+1):
    #         l1.append(i)
    #     B-=1
        
    #     for i in range(min(20, A - 1), -1, -1): 
    #         idx = (B // fact[i])
    #         B -= idx * fact[i]
    #         ans[curr] = l1[idx]
    #         curr+=1
    #         l1.pop(idx)
        
    #     return ans
    
    # C++
# vector<int> Solution::findPerm(int A, long B) {
#     vector<long> fac(20,1);B--;
#     for(int i=2;i<20;i++) fac[i]=fac[i-1]*i;
#     int p=0;while(p<20 && fac[p]<=B) p++;
#     p--;
#     // cout<<p<<endl;
#     vector<int> ans;
#     for(int i=1;i<A-p;i++) ans.push_back(i);
#     vector<int> rem;
#     for(int i=A-p;i<=A;i++) rem.push_back(i);
#     while(p>=0){
#         int it = B/fac[p];
#         ans.push_back(rem[it]);
#         rem.erase(rem.begin()+it);
#         B=B%fac[p];p--;
#     }
#     return ans;
# }

    # GO:
#     /**
#  * @input A : Integer
#  * @input B : Long
#  * 
#  * @Output Integer array.
#  */
# func findPerm(A int , B int64 )  ([]int) {
#     // 4
#     // 1234 1243 1324 1342 1423 1432 
#     // 2134 2143 2314 2341 2413 2431 
#     // 3124 3142 3214 3241 3412 3421
#     // 4123 4132 4213 4231 4312 4321
    
#     // 16 -> ceil(B/(A-1)!) = 3 -> 3 124
#     // 4 -> ceil(B'/(A-2)!) = 2 -> 
#     // 2 -> ceil(B''/(A-3)!) = 2
#     // 
#     // if A > 20 -> iterate until last 20 places
#     output := make([]int, A)
#     for i := 1; i <= A; i++ {
#         output[i-1] = i
#     }
#     fact := make([]int64, 21)
#     fact[0] = 1
#     for i := 1; i < 21; i++{
#         fact[i] = int64(i) * fact[i-1]
#     }
    
#     var idx int
#     if A > 20 {
#         idx = A - 20 - 1
#     }
#     var totalIterationsLeft int64 = B
#     var currentElementPosition int = 0
#     for idx < A {
#         // fmt.Println("starting iterations", idx, totalIterationsLeft)
#         currentElementPosition, totalIterationsLeft = divideSpecial(totalIterationsLeft, fact[A - idx - 1])
#         if(currentElementPosition == 0) {
#             idx++
#             continue
#         }
#         val := output[idx+currentElementPosition-1]
#         // fmt.Println("divide special", currentElementPosition, totalIterationsLeft, val)
#         for j := idx + currentElementPosition-1; j > idx  ; j-- {
#             output[j] = output[j-1]
#         }
#         output[idx] = val
#         // fmt.Println(output)
#         idx++
#     }
#     return output
    
# }

# func divideSpecial(dividend, divisor int64)(int, int64){
#     if dividend < divisor {
#         return 0, dividend
#     }
#     if dividend % divisor == 0 {
#         return int(dividend/divisor), divisor
#     }
#     return int(dividend/divisor)+1, dividend%divisor
# }