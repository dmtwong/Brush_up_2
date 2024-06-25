# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 10:27:04 2024

@author: UsubErt
"""

# 1. https://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
# 2. https://python5566.wordpress.com/2020/01/09/interviewbit-simple-queries/ Review this again 


# Problem Description
#  You are given an array A having N integers.
# You have to perform the following steps in a given order.
# 1) generate all subarrays of A.
# 2) take the maximum element from each subarray of A and insert it into a new array G.
# 3) replace every element of G with the product of their divisors mod 1e9 + 7.
# 4) sort G in descending order

# You now need to perform Q queries

# In each query, you are given an integer K, where you have to find the Kth element in G.

# NOTE : Your solution will run on multiple test cases so do clear global variables after using them.



# Problem Constraints
# 1 <= N <= 1e5

# 1 <= A[i] <= 1e5

# 1 <= Q <= 1e5

# 1 <= k <= (N * (N + 1))/2 



# Input Format
# The first argument given is an Array A, having N integers.

# The second argument given is an Array B, where B[i] is the ith query.



# Output Format
# rteturn an Array X, where X[i] will have the answer for the ith query.



# Example Input
# Input 1:

  A = [1, 2, 4]
B = [1, 2, 3, 4, 5, 6]
solve(A, B)
# Input 2:

   A = [1, 3]
B = [1]


# Example Output
# Output 1:

#  [8, 8, 8, 2, 2, 1]
# Output 2:

#  [3]


# Example Explanation
# Explanation 1:

#  subarrays of A    maximum element
# [1] 1
# [1, 2] 2
# [1, 2, 4] 4
# [2] 2
# [2, 4] 4
# [4] 4
# original
# G = [1, 2, 4, 2, 4, 4]

# after changing every element of G with product of their divisors
# G = [1, 2, 8, 2, 8, 8]

# after sorting G in descending order
# G = [8, 8, 8, 2, 2, 1]



# Explanation 2:

#  Just perform given query.
# class subolution:
#     # @param A : list of integers
#     # @param B : list of integers
#     # @return a list of integers
#     def solve(self, A, B):
def solve(A, B):
    from bisect import bisect_left

    def getFreq(A):
        # n = len(A)
        lt, rt = [1] * n_A, [1] * n_A
        sub, up = [], -1
        for i in range(n_A):
            while(up >= 0 and A[sub[up]] <= A[i]):
                sub.pop()
                up -= 1
            if (up >= 0):
                lt[i] = i - sub[up]
            else:
                lt[i] = i + 1
            sub.append(i)
            up += 1
        # print(sub, up, lt, rt)
        sub = []
        up = -1
        for i in range(n_A - 1, -1, -1):
            while(up >= 0 and A[sub[up]] < A[i]):
                sub.pop()
                up -= 1
            if (up >= 0):
                rt[i] = sub[up] - i
            else:
                rt[i] = n_A - i
            sub.append(i)
            up += 1
        # print(sub, up, lt, rt)
        for i in range(n_A):
            lt[i] *= rt[i]
        return lt
        
    def divisorProduct(k):
        d = 2
        for i in range(2, int(k ** 0.5) + 1):
            if k % i == 0:
                if k//i != i:
                    d += 1
                d += 1
        result = 1
        for _ in range(d // 2): # for result in range(d // 2): # for _ in range(d // 2):
            result = (result * k) % (10**9 + 7)
            # print(result)
            # print(_) # 0 
        if d % 2 != 0:
            result = (result * (k**0.5)) % (10**9 + 7)
        return int(result)
    
    n_A, proA = len(A), []
    freq = getFreq(A)
    #query 3
    for i in range(n_A):
        proA.append(divisorProduct(A[i]))
    fA = list(zip(proA, freq))
    fA.sort(reverse = True)
    V, accumulated = [], 0
    for i in range(n_A):
        accumulated += fA[i][1]
        V.append(accumulated)
    result = []
    for i in B:
        result.append(fA[bisect_left(V, i)][0])
    #query 5
    return result

# # Editorial:

# from collections import defaultdict
# from math import sqrt
# import bisect

# def getDivsProd(n):
#     mod = 1000000007
#     p = 1
#     for i in range(1, int(n**0.5 + 1)):
#         if n%i==0:
#             if n/i==i: p = (p*i)%mod
#             else:
#                 p = (p*i)%mod
#                 p = (p*(n/i))%mod
#     return int(p%mod)

# def getFrequency(A):
#     N = len(A)
#     L = [1]*N
#     R = [1]*N
#     S = []
#     top = -1
#     for i in range(N):
#         while(top >= 0 and A[S[top]] <= A[i]):
#             S.pop()
#             top -= 1
#         if (top >= 0):
#             L[i] = i - S[top]
#         else:
#             L[i] = i + 1
#         S.append(i)
#         top += 1
#     S = []
#     top = -1
#     for i in range(N-1, -1, -1):
#         while(top >= 0 and A[S[top]] < A[i]):
#             S.pop()
#             top -= 1
#         if (top >= 0):
#             R[i] = S[top] - i
#         else:
#             R[i] = N - i
#         S.append(i)
#         top += 1
#     for i in range(N):
#         L[i] *= R[i]
#     return L
    

# class Solution:
#     def solve(self, A, B):
#         N = len(A)
#         freq = getFrequency(A)
#         for i in range(N):
#             A[i] = getDivsProd(A[i])
#         keys = []
#         values = []
#         prev = 0
#         for i in sorted(zip(A, freq), reverse = True):
#             keys.append(i[0])
#             prev += i[1]
#             values.append(prev)
#         res = []
#         for i in B:
#             res.append(keys[bisect.bisect_left(values,i)])
#         return res
    
# C++:
#     #define ll long long int
# const int mn = 1e5 + 5;
# const ll mod = 1e9 + 7;
# ll power(ll a, ll g) {ll ag = 1; while(g){if(g&1) ag = (ag%mod * a%mod)%mod; a = (a%mod * a%mod)%mod; g >>= 1;} return ag;}

# ll p[mn];

# void pre_compute_product_of_divisors() {
#     p[0] = 0; p[1] = 1;
#     if(p[2] != 0) return;
#     for(ll i = 2; i < mn; i += 1) {
#         if(p[i] == 0) {
#             p[i] = 2;
#             for(ll j = i+i; j < mn; j += i) {
#                 if(p[j] == 0) p[j] = 1;
#                 ll tmp = j;
#                 ll cnt = 0;
#                 while(tmp % i == 0) {
#                     cnt += 1;
#                     tmp /= i;
#                 }
#                 p[j] *= (cnt + 1);
#             }
#         }
#     }
#     for(int i = 2; i < mn; i += 1) {
#         p[i] = (power(i, p[i]/2)%mod * (p[i]&1 ? (ll)sqrt(i) : 1)%mod)%mod;
#     }
# }

# // comparator to sort in descending order
# bool compare(pair<int, long long int> a, pair<int, long long int> g) {
#     if(a.first == g.first)
#         return a.second < g.second;
#     else
#         return a.first > g.first;
# }

# vector<int> Solution::solve(vector<int> &A, vector<int> &B) {
    
#     pre_compute_product_of_divisors();
    
#     int n = (int)A.size();
#     // create arrays to store length of longest segment in which ith element is greater
#     long long int l[n], r[n], lr[n];
#     // initialize elements array equal to 1.
#     for(int i = 0; i < n; i += 1) {
#         l[i] = r[i] = 1;
#     }
#     // find next greater element to the left of the current element
#     for(int i = 1; i < n; i += 1) {
#         int last = i-1;
#         while(last >= 0 and A[i] > A[last]) {
#             l[i] += l[last];
#             last -= l[last];
#         }
#     }
#     // find next greater element to the right of the current element
#     for(int i = n-2; i >= 0; i -= 1) {
#         int last = i+1;
#         while(last < n and A[i] >= A[last]) {
#             r[i] += r[last];
#             last += r[last];
#         }
#     }
#     // The number of subarrays in which current element will be the greater
#     for(int i = 0; i < n; i += 1) {
#         lr[i] = l[i] * r[i];
#     }
#     // Sort elements in descending order according to there value
#     pair<int, long long int> ag[n];
#     for(int i = 0; i < n; i += 1) {
#         ag[i] = {p[A[i]], lr[i]};
#     }
#     sort(ag, ag + n, compare);

#     // Take Prefix Sum of frequencies of elements
#     long long pre[n];
#     pre[0] = ag[0].second;
#     for(int i = 1; i < n; i += 1) {
#         pre[i] = pre[i-1] + ag[i].second;
#     }
    
#     // do Binary search for each query
#     int q = (int)B.size();
#     vector<int> ans(q);
#     for(int i = 0; i < q; i += 1) {
#         auto id = lower_bound(pre, pre + n, B[i]) - pre;
#         ans[i] = ag[id].first;
#     }
#     // return the ans array
#     return ans;
# }

# GO:
# import ("sort"
#         "math")

# type FactorFreq struct{
#     product int
#     freq int
# }

# func solve(A []int , B []int )  ([]int) {
#     ans := make([]int, len(B))
#     if len(A) == 0{
#         return ans
#     }
    
#     lGreater := make([]int, len(A))
#     rGreater := make([]int, len(A))

#     items := make([]item, 1)
#     items[0] = item{A[0], 0}
#     lGreater[0] = -1
#     for i := 1; i < len(A); i++ {
#         items, lGreater[i] = processNextGreater(items, item{A[i], i}, true)
#     }
    
#     rightItems := make([]item, 1)
#     rightItems[0] = item{A[len(A)-1], len(A) - 1}
#     rGreater[len(A)-1] = -1
    
#     for i := len(A) - 2; i >= 0; i--{
#         rightItems, rGreater[i] = processNextGreater(rightItems, item{A[i], i}, false)
#     }
    
#     maxOccurenceSubarr := make([]int, len(A))
    
#     for i:=0; i < len(A); i++ {
#         var left int
#         if lGreater[i] < 0 {
#             left = i + 1
#         }else{
#             left = i - lGreater[i]
#         }
        
#         var right int
#         if rGreater[i] < 0{
#             right = len(A) - i
#         }else{
#             right = rGreater[i] - i
#         }
#         maxOccurenceSubarr[i] = left * right
#     }

#     subArrProdDivisors := make([]FactorFreq, len(A))
#     for i := 0; i < len(A); i++{
#         subArrProdDivisors[i] = FactorFreq{product:getProductOfFactor(A[i]), freq:maxOccurenceSubarr[i]}
#     }
#     sort.Slice(subArrProdDivisors, func(i, j int) bool{
#         return subArrProdDivisors[i].product > subArrProdDivisors[j].product
#     })
    
#     prefixSum := make([]int, len(subArrProdDivisors))
#     prefixSum[0] = subArrProdDivisors[0].freq
#     for i := 1; i < len(subArrProdDivisors); i++ {
#         prefixSum[i] = prefixSum[i-1] + subArrProdDivisors[i].freq
#     }

#     res := make([]int, len(B))
#     for i := 0; i < len(B); i++{
#         res[i] = subArrProdDivisors[binSearch(prefixSum, B[i])].product
#     }

#     return res
# }


# type item struct{
#     value int
#     index int
# }

# func processNextGreater(itemSlack []item, currItem item, considerEq bool) ([]item, int){
#     if len(itemSlack) == 0{
#         return itemSlack, -1
#     }
    
#     topIndex := len(itemSlack) - 1
#     topElem := itemSlack[topIndex]
    
#     for (topIndex >= 0 && ((considerEq && topElem.value <= currItem.value) || (!considerEq && topElem.value < currItem.value))){
#         itemSlack = itemSlack[:topIndex]
#         topIndex = len(itemSlack) - 1
#         if topIndex >= 0{
#             topElem = itemSlack[topIndex]
#         }
#     }
#     itemSlack = append(itemSlack, currItem)
#     if topIndex < 0 {
#         return itemSlack, -1
#     }
#     return itemSlack, topElem.index
# }

# func getProductOfFactor(num int) int {
#     prod := 1
    
#     var isSeenFactor = map[int]bool{}
#     for i := 1; i <= int(math.Sqrt(float64(num))); i++ {
#         if num % i == 0 {
#             if _, ok := isSeenFactor[i]; !ok {
#                 prod = (prod % 1000000007 * i % 1000000007) % 1000000007
#                 isSeenFactor[i] = true
#             }
#             if _, ok := isSeenFactor[num/i]; !ok{
#                 prod = (prod % 1000000007 * (num/i) % 1000000007) % 1000000007
#                 isSeenFactor[num/i] = true
#             }
#         }
#     }
#     return prod
# }


# func binSearch(nums []int, numToSearch int) int{
#     start, end, mid := 0, len(nums)-1, len(nums)/2

#     for (start >= 0 && end < len(nums) && start <= end){
#         if nums[mid] == numToSearch{
#             return mid
#         }

#         if nums[mid] > numToSearch{
#             if mid - 1 >= start && nums[mid - 1] < numToSearch{
#                 return mid
#             }
#             end = mid - 1
#         } else{
#             if mid + 1 <= end && nums[mid + 1] > numToSearch{
#                 return mid + 1
#             }
#             start = mid + 1
#         }
#         mid = (start + end) / 2
#     }

#     if start <= 0{
#         return 0
#     }
#     return len(nums) - 1
# }
            
