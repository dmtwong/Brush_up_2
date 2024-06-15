//============================================================================
// Name        : PrettyPrint.cpp
// Author      : David W.
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

int main() {
	cout << "!!!Hello World!!!" << endl; // prints !!!Hello World!!!
	//vector<vector<int> > Solution::prettyPrint(int A) {
	vector<vector<int> > prettyPrint(int A) {
	    int arraySize = A * 2 - 1;
	    int result[arraySize][arraySize];
	    vector<int> vec_line;
	    vector<vector<int> > Result;
	    for(int i = 0; i < arraySize; i++){
	        for(int j = 0; j < arraySize; j++){
	            if(abs(i - arraySize / 2) > abs(j - arraySize / 2))
	                result[i][j] = abs(i - arraySize / 2) + 1;
	            else
	                result[i][j] = (abs(j-arraySize / 2) + 1);
	        }
	    }
	    for (int i =0 ; i < arraySize; i++){
	        for(int j = 0; j < arraySize; j++)
	            vec_line.push_back(result[i][j]);
	        Result.push_back(vec_line);
	        vec_line.clear();
	    }
	    return Result;
	}
	/*
		int n = A * 2 - 1;
		int m = n;
	    //vector<vector<int, m>, n> Result;
		int arr_line[m];
		vector<int> vec_line;
		vector<vector<int> > Result;
	    int line_min = A;
	    int cur_val;
		for (int i = 0; i < n; i++){
			line_min = A - i;
			cur_val = A;
			for (int j = 0; j < m; j++){
				arr_line[j] = cur_val;
				if (cur_val > line_min && j < A - 1){
					cur_val -= 1;
				} else if (j >= A && cur_val < A){
					cur_val += 1;
				}
			}
			for (int k = 0; k < m; k++){
				vec_line.push_back(arr_line[k]);
			}
			//vec_line.emplace_back(arr_line.begin(), arr_line.end())
			Result.push_back(vec_line);
			vec_line.clear();
		}
		return Result;
	}
	*/
	return 0;
}
