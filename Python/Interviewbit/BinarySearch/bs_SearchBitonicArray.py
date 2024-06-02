# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 18:22:02 2024

@author: USER
"""
# Problem Description
 
# Given a bitonic sequence A of N distinct elements, write a program to find a given element B in the bitonic sequence in O(logN) time.
# NOTE:
# A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.

# Problem Constraints
# 3 <= N <= 105
# 1 <= A[i], B <= 108
# Given array always contain a bitonic point.

# Array A always contain distinct elements.

# Input Format
# First argument is an integer array A denoting the bitonic sequence.
# Second argument is an integer B.

# Output Format
# Return a sing

# Example Input
# Input 1:
  A = [3, 9, 10, 20, 17, 5, 1]
  B = 20
solve(A, B)
# Input 2:
  A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
  B = 30
# Example Output
# Output 1:
#  3
#  Output 2:

#  -1


# Example Explanation
# Explanation 1:

#  B = 20 present in A at index 3
# Explanation 2:

#  B = 30 is not present in A


# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
        
def solve(self, A, B):
    
def solve(A, B):
    def find_bp(A, lf, rt):
        bp = 0
        mid = (lf + rt) // 2
        if A[mid] > A[mid - 1] and A[mid + 1] < A[mid]:
            return mid
        elif A[mid] > A[mid - 1] and A[mid + 1] > A[mid]:
            bp = find_bp(A, mid, rt)
        else:
            bp = find_bp(A, lf, mid)
        return bp
    def search_direction(A, lf, rt, key, isUp):
        while lf <= rt:
            mid = lf + (rt - lf) // 2
            if A[mid] == key:
                return mid
            if (A[mid] > key and isUp == True) or (A[mid] < key and isUp == False) :
                rt = mid - 1
            else:
                lf = mid + 1
        return -1   
    def search(A, ix, n, key):    
        if key > A[ix]:
            return -1
        elif key == A[ix]:
            return ix
        else:
            result = search_direction(A, 0, ix-1, key, True)
            if result != -1:
                return result                 
            return search_direction(A, ix+1, n-1, key, False)
    n_A = len(A)
    ix = find_bp(A, 0, n_A - 1)
    result = search(A, ix, n_A, B)
    if result == -1:
        return -1
    else:
        return result


    # Editoral:
        # Python 

# def ascendingBinarySearch(arr,low,high,key):
#     while(low<=high):
#         mid=low+(high-low)//2
#         if(arr[mid]==key):
#             return mid
#         if(arr[mid]>key):
#             high=mid-1
#         else:
#             low=mid+1
#     return -1
# def descendingBinarySearch(arr,low,high,key):
#     while(low<=high):
#         mid=low+(high-low)//2
#         if(arr[mid]==key):
#             return mid
#         if(arr[mid]<key):
#             high=mid-1
#         else:
#             low=mid+1
#     return -1
# def findBitonicPoint(arr,n,l,r):
#     mid=(l+r)//2
#     if(arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]):
#         return mid
#     elif(arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]):
#         return findBitonicPoint(arr,n,mid,r)
#     elif(arr[mid]<arr[mid-1] and arr[mid]>arr[mid+1]):
#         return findBitonicPoint(arr,n,l,mid)
# def searchBitonic(arr,n,key,index):
#     if(key>arr[index]):
#         return -1
#     elif(key==arr[index]):
#         return index
#     else:
#         temp=ascendingBinarySearch(arr,0,index-1,key)
#         if(temp!=-1):
#             return temp
#         return descendingBinarySearch(arr,index+1,n-1,key)
# def solveQ(arr,b):
#     index=findBitonicPoint(arr,len(arr),0,len(arr)-1)
#     x=searchBitonic(arr,len(arr),b,index)
#     return x 
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         return solveQ(A,B)
    
    # C++
#     // Function for binary search in ascending part
# int ascendingBinarySearch(vector < int > & arr, int low,
#   int high, int key) {
#   while (low <= high) {
#     int mid = low + (high - low) / 2;
#     if (arr[mid] == key)
#       return mid;
#     if (arr[mid] > key)
#       high = mid - 1;
#     else
#       low = mid + 1;
#   }
#   return -1;
# }

# // Function for binary search in descending part of array
# int descendingBinarySearch(vector < int > & arr, int low,
#   int high, int key) {
#   while (low <= high) {
#     int mid = low + (high - low) / 2;
#     if (arr[mid] == key)
#       return mid;
#     if (arr[mid] < key)
#       high = mid - 1;
#     else
#       low = mid + 1;
#   }
#   return -1;
# }

# // finding bitonic point
# int findBitonicPoint(vector < int > & arr, int n, int l, int r) {
#   int mid;
#   mid = (r + l) / 2;
#   if (arr[mid] > arr[mid - 1] && arr[mid] > arr[mid + 1]) {
#     return mid;
#   } else if (arr[mid] > arr[mid - 1] && arr[mid] < arr[mid + 1]) {
#     return findBitonicPoint(arr, n, mid, r);
#   } else if (arr[mid] < arr[mid - 1] && arr[mid] > arr[mid + 1]) {
#     return findBitonicPoint(arr, n, l, mid);
#   }
# }

# // Function to search key in bitonic array
# int searchBitonic(vector < int > & arr, int n, int key, int index) {
#   if (key > arr[index])
#     return -1;

#   else if (key == arr[index])
#     return index;

#   else {
#     int temp = ascendingBinarySearch(arr, 0, index - 1, key);
#     if (temp != -1) {
#       return temp;
#     }

#     // Search in right of k
#     return descendingBinarySearch(arr, index + 1, n - 1, key);
#   }
# }
# int solveQ(vector < int > & arr, int b) {
#   int index = findBitonicPoint(arr, arr.size(), 0, arr.size() - 1);
#   int x = searchBitonic(arr, arr.size(), b, index);
#   return x;
# }
# int Solution::solve(vector < int > & A, int B) {
#   return solveQ(A, B);
# }

    # Scala
# class Solution {
#   def solve(A: Array[Int], B: Int): Int  = {
#     var start = 0
#     var end = A.length-1

#     var bitonicPoint = -1
#     while (bitonicPoint == -1) {
#       if (end - start <= 1) {
#         bitonicPoint = if (A(start) > A(start+1)) start else end
#       } else if (A(start) < A(start + 1)) {
#         start = (end + start) / 2
#       } else {
#         end = start
#         start = start / 2
#       }
#     }
#     import scala.collection.Searching._
#     A.search(B, 0, bitonicPoint) match {
#       case Found(foundIndex) => foundIndex
#       case InsertionPoint(insertionPoint) =>
#         A.search(B, bitonicPoint, A.length)(Ordering.Int.reverse) match {
#           case Found(foundIndex) => foundIndex
#           case InsertionPoint(insertionPoint) => -1
#         }
#     }
#   }
# }

    # GO
# /**
#  * @input A : Integer array
#  * @input B : Integer
#  * 
#  * @Output Integer
#  */

# func isAscendingIndex(A []int, mid int) bool {
#     if mid == 0 || (mid != len(A) - 1 && A[mid] > A[mid - 1] && A[mid] < A[mid + 1]) {
#         return true
#     }
#     return false
# }

# func isBitonicIndex(A []int, mid int) bool {
#     if mid != 0 && mid != len(A) - 1 && A[mid] > A[mid - 1] && A[mid] > A[mid + 1] {
#         return true
#     }
#     return false
# }

# func findIncreasing(A []int, B int, high int) int {
#     low := 0
#     for low <= high {
#         mid := low + ((high - low) / 2)
#         if A[mid] == B {
#             return mid
#         } else if A[mid] < B {
#             low = mid + 1
#         } else {
#             high = mid - 1
#         }
#     }
#     return -1
# }

# func findDecreasing(A []int, B int, low int) int {
#     high := len(A) - 1
#     for low <= high {
#         mid := low + ((high - low) / 2)
#         if A[mid] == B {
#             return mid
#         } else if A[mid] < B {
#             high = mid - 1
#         } else {
#             low = mid + 1
#         }
#     }
#     return -1
# }

# func findBitonicIndex(A []int) int {
#     low := 0
#     high := len(A) - 1
#     mid := low + ((high - low) / 2)
#     for !isBitonicIndex(A, mid) {
#         if isAscendingIndex(A, mid) {
#             low = mid + 1
#         } else {
#             high = mid - 1
#         }
#         mid = low + ((high - low) / 2)
#     }
#     return mid
# }
 
# func solve(A []int , B int )  (int) {
#     bitonicIndex := findBitonicIndex(A)
#     result := findIncreasing(A, B, bitonicIndex)
#     if result == -1 {
#         return findDecreasing(A, B, bitonicIndex + 1)
#     }
#     return result
# }

