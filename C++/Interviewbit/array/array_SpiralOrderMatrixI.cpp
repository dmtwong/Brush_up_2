//============================================================================
// Name        : array_SpiralOrderMatrixI.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

int main() {
	//cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	/*
	Problem Description
	Given a matrix of M * N elements (M rows, N columns), return all elements of the matrix in spiral order.
	Problem Constraints
	1 <= M, N <= 1000
	Input Format
	The first argument is a matrix A.
	Output Format
	Return an array of integers representing all elements of the matrix in spiral order.
	Example Input
	A =
	    [
	        [ 1, 2, 3 ],
	        [ 4, 5, 6 ],
	        [ 7, 8, 9 ]
	    ]
	Example Output
	[1, 2, 3, 6, 9, 8, 7, 4, 5]
	*/
	// vector<int> Solution::spiralOrder(const vector<vector<int> > &A) {
	vector<int> Solution::spiralOrder(const vector<vector<int> > &A) {
	    int n_N, n_M;
	    int ix = 0;
	    int ix_n = 0;
	    int ix_m = 0;
	    n_N = A.size();
	    n_M = A[0].size();
	    vector<int> V(n_N * n_M, 1);
	    int n_last = n_N - 1;
	    int m_last = n_M - 1;

	    while (ix_n <= n_last && ix_m <= m_last){
	        for (int i = ix_m; i <= m_last; i++){
	            V[ix] = A[ix_n][i];
	            ix += 1;
	        }
	        ix_n += 1;
	        //ix_n++;
	        for (int i = ix_n; i <= n_last; i++){
	            V[ix] = A[i][m_last];
	            ix += 1;
	        }
	        m_last -= 1;
	        //m_last--;
	        if (ix_n <= n_last){
	            for (int i = m_last; i >= ix_m; i--){
	                V[ix] = A[n_last][i];
	                ix+= 1;
	            }
	            n_last -= 1;
	            //n_last--;
	        }
	        if (ix_m <= m_last){
	            for (int i = n_last; i >= ix_n; i--){
	                V[ix] = A[i][ix_m];
	                ix += 1;
	            }
	            ix_m += 1;
	            //ix_m--;
	        }
	    }
	    return V;
	    }
	    /*for (int i = 0; i < n_N; i++){
	        for (int j = 0; j < n_M; j++){
	            V[ix] = A[i][j];
	            ix += 1;
	        }
	    }
	    */

	return 0;
}

/*
 *
 * vector<int> Solution::spiralOrder(const vector<vector<int> > &A) {
	vector<int> result;
	int r=A.size(), c=A[0].size();
	int r_beg=0,r_end=r,c_beg=0,c_end=c;
    while(r_beg<r_end && c_beg<c_end){
        for(int i=c_beg;i<c_end;i++)
            result.push_back(A[r_beg][i]);
        for(int i=r_beg+1;i<r_end;i++)
            result.push_back(A[i][c_end-1]);
        for(int i=c_end-2;i>=c_beg && (r_end-1-r_beg)>0;i--)
            result.push_back(A[r_end-1][i]);
        for(int i=r_end-2;i>r_beg && (c_end-1-c_beg)>0;i--)
            result.push_back(A[i][c_beg]);
        r_beg++;r_end--;
        c_beg++;c_end--;
    }
	return result;
}
 */
