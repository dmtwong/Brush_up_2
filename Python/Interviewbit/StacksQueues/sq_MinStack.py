# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 10:50:29 2024

@author: USER
"""
 
# Problem Description

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# Note that all the operations have to be constant time operations.
# Questions to ask the interviewer :
# Q: What should getMin() do on empty stack? 
# A: In this case, return -1.

# Q: What should pop do on empty stack? 
# A: In this case, nothing. 

# Q: What should top() do on empty stack?
# A: In this case, return -1
# NOTE : If you are using your own declared global variables, make sure to clear them out in the constructor.
# dd_1 = defaultdict(lambda:0)
# for i in range(10):
#     if i == 5: 
#         continue
#     dd_1[i] = i
# dd_1[5]
# dd_1[2] = 0
# dd_1
# max([i for i in dd_1.keys()])
# ([i for i in dd_1.keys() if list(dd_1.values())[i] == 0 ])
# dd_1[9]

# dd_1[10]
# dd_1[11]
# dd_1.keys()
# defaultdict()
# dd_1.values()
class MinStack:
    # @param x, an integer
    # from collections import defaultdict # added as Time limit excceded 
    def __init__(self):
        # self.front = None
        self.topp = None
        self.cnt = 0
        self.min = None
        self.list = []
        # self.dd_1 = defaultdict(lambda: 0)
        # self.list_sort = []
        # self.dict = {}
        self.min_list = []
        
    def push(self, x):
        if self.topp == None:
            self.min = x
        # if self.dd_1[x] == 0: 
        #     self.dd_1[x] = 1
        # else:
        # self.list_sort.append(x)
        # self.list_sort.sort()
        # self.d[x] += 1
        self.topp = x
        self.list.append(x)
        self.cnt += 1
        if x <= self.min:
            self.min = x
            self.min_list.append(x)
    # @return nothing
    def pop(self):
        if self.topp == None:
            return None
        elif self.cnt == 1:
            self.topp = None
            self.min = None
            # print('here')
            self.list.pop()
            # print('there')
            self.cnt -= 1
            return None
        self.cnt -= 1
        # print(self.cnt)
        cur_last = self.list[-1]                
        self.list.pop()
        self.topp = self.list[-1]    
                # self.list = self.list[:-1]
        if self.min == cur_last:
            self.min_list.pop()
        #     self.list.index(cur_last)
        # except:           
        #     # print(self.list)
            self.min = self.min_list[-1]
                # self.dd_1[self.min] -= 1
                # if self.dd_1[self.min] == 0:
                    # []
            # temp = self.top
            # return temp
    # @return an integer
    def top(self):
        if self.topp == None:
            return -1
        return self.topp

    # @return an integer
    def getMin(self):
        if self.min == None:
            return -1
        else:
            return self.min
        
temp = MinStack()
temp.push(19)
temp.getMin()
temp.top()
temp.push(10)
temp.push(9)
temp.getMin()


# 19 P 10 P 9 g P 8 g P 7 g P 6 g p g p g p g p g p g

# There are 1 lines in the input

# Line 1 ( Corresponds to arg 1 ) : The line starts with a number numOperations, corresponding to the number of operations.
# Then "numOperation" operations follow. 
# Each operation is either : 
#  * P <number> : Corresponds to push(<number>) in stack
#  * p : Corresponds to pop()
#  * t : Corresponds to top()
#  * g : Corresponds to getMin() call.
# Note that the function calls are made in order.  

# The expected return value: 
# 9 8 7 6 7 8 9 10 -1 



# Your submission failed for the following input
# 913 p P 644643544 g t t t p P 723943208 p P 909204 g t g t P 481523691 p P 465865082 t P 243519307 p t p P 844871295 g P 573041392 P 468497349 p t g P 776647984 t p t P 884224920 t t p P 626132265 g t P 26748055 g g P 720873676 P 31868025 P 118819922 t g p P 12108907 g p p p t P 895351682 g t P 127364950 g t P 76234642 g t g P 940134342 g p t g P 209923674 g p p P 593912449 g t P 182168561 P 252333986 g P 120254050 g t t g P 281700253 t p p P 107300696 P 83179520 p t t p P 743998858 P 348668934 t t P 238471928 P 185805946 P 345076113 g p P 612934366 p P 646116941 g t P 488822038 g g g P 656668538 g p t g P 205786971 g p p g t g p g t t t P 250759605 g P 696981907 g p p p g g t t p P 660016257 P 254799527 p p g t g g t g p t p P 548011103 p g p t g p P 598697340 p g P 89970109 g t t P 528152523 t p P 750873206 t t P 125328730 g t p t P 860096457 t t p g g P 561229779 g t p t t t g p t t g t g t p P 243176345 P 488648003 g P 22516828 P 80428842 g p g t g p P 112478235 p p g g P 750671046 g g p t P 632746483 g g g g g p g P 168809210 p P 517352357 t p p P 901370929 p g P 69043217 p p p t g P 847833679 t p p t t t t p p g t P 349308524 P 652875950 t P 606686342 P 431329509 p t g t t P 917778387 g t P 588497480 p P 118202971 t P 809454497 t g g p t t P 983614607 p P 500383473 g P 724206024 g t t P 554200746 p t p p p t p p t t t t P 88588979 g p g P 926280810 g t g g P 7007596 p g g t t g p t P 299898202 p P 176651727 p P 625298442 g g P 964576672 g t p p t p g t P 824230322 g g t p p t g p g P 659267334 p P 686616200 p P 54394415 t P 12936572 g P 823626948 P 296766867 g P 335749563 P 904935349 g g p g p t P 754491210 t t g p p p p p p P 36886338 p p p g p P 780809279 t P 57337424 P 998849637 t p P 514381243 p t t t p P 814651044 g P 241546604 P 358242178 p p t t g g p t p P 89830827 t g P 240798522 P 247368207 P 730272441 P 662618586 t p t p t P 621571093 g g t p P 650001396 p t P 38553589 p g t t p g g g p t P 997480662 P 136877685 t p P 278152626 t g t t t P 157969343 g p p p p p g P 651164025 p P 229722550 g t g p P 351226886 p p P 121870305 g g t p p p p P 2843013 p P 618922784 t t g P 462348827 g p p P 604617481 t g g p g g p p P 541892421 P 9071319 t P 237859914 g P 51389970 P 585997077 p P 369222651 t p g g p g p P 670239380 g p P 106123423 P 327003375 t g g g P 525338387 P 972120060 P 78041206 g p t p g p t t t t t t g g g p p g t t p p P 895785982 g P 593298567 t P 152298972 g p p g t t t t P 402633899 P 86452767 g P 126101020 t p p p P 576987968 t p p g g t p t t t p p P 709040762 g g g g g P 135410678 P 468694199 p p t t g P 533112170 P 754858929 p g g p p g P 103302239 t g P 842320959 p t t P 731860400 g t p p g p g g g P 787907999 p t t p g P 373884541 g t P 98601703 p p t p p p g P 280232551 t P 121479941 t P 750771195 P 841602601 p p p p t P 792761407 p p p p t P 304880476 t g t t P 45007612 P 39553022 g g g t t p P 174625619 g t t p t g g p P 135094596 g P 2359009 t P 312614429 p g g g g p p g p t t p p t p t P 186258833 P 964834539 t P 934935549 t g g t p p P 353623991 t P 826395666 P 386343072 g p p P 349547603 P 179753601 P 492794836 P 580149290 P 165212936 g P 1670863 t P 784959420 g p g p p g t t P 21842309 P 337081522 P 777712799 t P 555402283 g t g P 75160257 g g g g g p p t g g p p p g g P 745438423 g P 691084246 p g t P 88773973 t p g P 372912557 p p p g t t P 911490527 t t P 978231016 g P 55522554 P 29843435 g t p p p t p t t p t g P 263283033 p P 372553608 g p p p P 871047378 p g t t t g p P 54582821 t P 103119643 P 619917644 t g p p P 534201865 g P 688295661 p p p p g p p p g p g P 366155438 g t g g p P 119307898 g g P 337604683 g P 585762794 t P 482263814 t p P 796273641 p t P 891773904 g t P 536501786 g P 136953609 t g P 793669592 p t p t p t p g g p t P 703312633 g p p p t p P 12446017 t t g p p P 660673550 P 970004511 P 859363430 t t p t p g t P 307165825 t t p P 27229714 g t t g g P 955115299 P 829997260 t g p P 464667952 g t g p t g p t g p t p
# temp2 = MinStack()
# temp2.pop()
# temp2.push(644643544)

# temp2.getMin()
# temp2.top()
# temp2.top()
# temp2.top()
# temp2.list
# temp2.pop()
# temp2.push(723943208)
# temp2.pop()
# temp2.push(909204)
# temp2.getMin()
# temp2.top()
# temp2.getMin()
# temp2.top()
# temp2.push(481523691)
# temp2.pop()
# temp2.push(465865082)
# temp2.top()
# temp2.push(243519307)
# temp2.top()


# There are 1 lines in the input

# Line 1 ( Corresponds to arg 1 ) : The line starts with a number numOperations, corresponding to the number of operations.
# Then "numOperation" operations follow. 
# Each operation is either : 
#  * P <number> : Corresponds to push(<number>) in stack
#  * p : Corresponds to pop()
#  * t : Corresponds to top()
#  * g : Corresponds to getMin() call.
# Note that the function calls are made in order.  

# The expected return value: 
# 644643544 644643544 644643544 644643544 909204 909204 909204 909204 465865082 465865082 909204 573041392 909204 776647984 573041392 884224920 884224920 909204 626132265 909204 909204 118819922 909204 909204 26748055 909204 895351682 909204 127364950 909204 76234642 909204 909204 76234642 909204 909204 909204 593912449 909204 909204 120254050 120254050 909204 281700253 107300696 107300696 348668934 348668934 909204 909204 646116941 909204 909204 909204 909204 488822038 909204 909204 909204 646116941 909204 909204 185805946 185805946 185805946 909204 909204 909204 909204 238471928 238471928 909204 348668934 909204 909204 348668934 909204 743998858 909204 182168561 909204 909204 909204 89970109 89970109 528152523 750873206 750873206 909204 125328730 750873206 860096457 860096457 909204 909204 909204 561229779 750873206 750873206 750873206 909204 89970109 89970109 909204 89970109 909204 89970109 909204 909204 909204 22516828 909204 909204 909204 909204 909204 243176345 909204 909204 909204 909204 909204 909204 517352357 909204 895351682 909204 847833679 26748055 26748055 26748055 26748055 909204 573041392 652875950 606686342 909204 606686342 606686342 909204 917778387 118202971 809454497 909204 909204 118202971 118202971 909204 909204 724206024 724206024 724206024 917778387 652875950 652875950 652875950 652875950 909204 909204 909204 926280810 909204 909204 909204 909204 926280810 926280810 909204 652875950 909204 909204 909204 964576672 652875950 909204 349308524 909204 909204 824230322 573041392 909204 909204 54394415 909204 909204 909204 909204 909204 296766867 754491210 754491210 909204 -1 780809279 998849637 57337424 57337424 57337424 780809279 814651044 814651044 780809279 780809279 780809279 89830827 89830827 662618586 730272441 247368207 89830827 89830827 621571093 247368207 89830827 247368207 247368207 89830827 89830827 89830827 89830827 136877685 278152626 89830827 278152626 278152626 278152626 89830827 -1 229722550 229722550 229722550 121870305 121870305 121870305 618922784 618922784 618922784 462348827 604617481 604617481 604617481 -1 -1 9071319 9071319 369222651 9071319 9071319 9071319 9071319 327003375 9071319 9071319 9071319 9071319 972120060 9071319 327003375 327003375 327003375 327003375 327003375 327003375 9071319 9071319 9071319 9071319 9071319 9071319 895785982 593298567 152298972 895785982 895785982 895785982 895785982 895785982 86452767 126101020 576987968 -1 -1 -1 -1 -1 -1 709040762 709040762 709040762 709040762 709040762 709040762 709040762 709040762 533112170 533112170 -1 103302239 103302239 103302239 103302239 103302239 731860400 -1 -1 -1 -1 -1 -1 -1 373884541 373884541 -1 -1 280232551 121479941 -1 -1 304880476 304880476 304880476 304880476 39553022 39553022 39553022 39553022 39553022 45007612 174625619 174625619 45007612 45007612 45007612 135094596 2359009 2359009 2359009 2359009 2359009 304880476 -1 -1 -1 -1 964834539 934935549 186258833 186258833 934935549 353623991 186258833 165212936 1670863 1670863 1670863 179753601 580149290 580149290 777712799 21842309 555402283 21842309 21842309 21842309 21842309 21842309 21842309 777712799 21842309 21842309 179753601 179753601 179753601 179753601 745438423 88773973 179753601 179753601 492794836 492794836 911490527 911490527 179753601 29843435 29843435 911490527 492794836 492794836 179753601 179753601 179753601 186258833 353623991 353623991 353623991 186258833 54582821 619917644 54582821 54582821 -1 -1 -1 366155438 366155438 366155438 366155438 119307898 119307898 119307898 585762794 482263814 585762794 119307898 891773904 119307898 136953609 119307898 136953609 536501786 891773904 119307898 119307898 337604683 119307898 -1 12446017 12446017 12446017 859363430 859363430 970004511 660673550 660673550 307165825 307165825 27229714 27229714 27229714 27229714 27229714 829997260 27229714 27229714 464667952 27229714 955115299 27229714 27229714 27229714 660673550 
# Your function returned the following: 
# 644643544 644643544 644643544 644643544 909204 909204 909204 909204 909204 465865082 909204 573041392 909204 573041392 573041392 573041392 573041392 909204 573041392 909204 909204 573041392 909204 909204 26748055 909204 26748055 909204 26748055 909204 26748055 909204 909204 76234642 909204 909204 909204 127364950 909204 909204 127364950 127364950 909204 127364950 107300696 107300696 252333986 252333986 909204 909204 185805946 909204 909204 909204 909204 488822038 909204 909204 909204 646116941 909204 909204 185805946 185805946 185805946 909204 909204 909204 909204 238471928 238471928 909204 348668934 909204 909204 348668934 909204 743998858 909204 182168561 909204 909204 909204 593912449 593912449 593912449 89970109 89970109 909204 89970109 750873206 750873206 750873206 909204 909204 909204 750873206 750873206 750873206 750873206 909204 89970109 89970109 909204 89970109 909204 89970109 909204 909204 909204 22516828 909204 909204 909204 909204 909204 243176345 909204 909204 909204 909204 909204 909204 243176345 909204 895351682 909204 895351682 26748055 26748055 26748055 26748055 909204 573041392 573041392 606686342 909204 606686342 606686342 909204 606686342 917778387 917778387 909204 909204 118202971 118202971 909204 909204 118202971 118202971 724206024 917778387 652875950 652875950 652875950 652875950 909204 909204 909204 652875950 909204 909204 909204 909204 926280810 926280810 909204 652875950 909204 909204 909204 652875950 652875950 909204 349308524 909204 909204 349308524 573041392 909204 909204 844871295 909204 909204 909204 909204 909204 296766867 296766867 296766867 909204 -1 780809279 780809279 57337424 57337424 57337424 780809279 814651044 814651044 780809279 780809279 780809279 89830827 89830827 89830827 730272441 247368207 89830827 89830827 247368207 247368207 89830827 247368207 247368207 89830827 89830827 89830827 89830827 89830827 997480662 89830827 997480662 997480662 997480662 89830827 -1 229722550 229722550 229722550 121870305 121870305 121870305 618922784 618922784 618922784 462348827 604617481 604617481 604617481 -1 -1 541892421 9071319 51389970 9071319 9071319 9071319 9071319 9071319 9071319 9071319 9071319 9071319 972120060 9071319 327003375 327003375 327003375 327003375 327003375 327003375 9071319 9071319 9071319 9071319 9071319 9071319 895785982 895785982 152298972 895785982 895785982 895785982 895785982 895785982 86452767 895785982 895785982 -1 -1 None None None None 709040762 709040762 709040762 709040762 709040762 709040762 709040762 709040762 533112170 533112170 -1 103302239 103302239 103302239 103302239 103302239 103302239 -1 -1 -1 -1 None None -1 373884541 373884541 None -1 280232551 280232551 None None 304880476 304880476 304880476 304880476 39553022 39553022 39553022 304880476 304880476 45007612 45007612 45007612 45007612 45007612 45007612 135094596 304880476 2359009 2359009 2359009 2359009 304880476 None None None None 186258833 186258833 186258833 186258833 186258833 186258833 186258833 165212936 353623991 1670863 1670863 179753601 580149290 580149290 580149290 21842309 580149290 21842309 21842309 21842309 21842309 21842309 21842309 777712799 21842309 21842309 179753601 179753601 179753601 179753601 745438423 745438423 179753601 179753601 492794836 492794836 492794836 492794836 179753601 29843435 492794836 911490527 492794836 492794836 179753601 179753601 179753601 186258833 353623991 353623991 353623991 186258833 186258833 186258833 54582821 54582821 -1 -1 -1 366155438 366155438 366155438 366155438 119307898 119307898 119307898 119307898 119307898 585762794 119307898 585762794 119307898 585762794 119307898 136953609 536501786 891773904 119307898 119307898 337604683 119307898 None 12446017 12446017 12446017 660673550 660673550 970004511 660673550 660673550 660673550 660673550 27229714 660673550 660673550 27229714 27229714 660673550 27229714 27229714 955115299 27229714 955115299 27229714 27229714 27229714 660673550 
# Test as custom input

# # Editorial:
# class MinStack:
#     stack = []
#     minimums = []
#     # @param x, an integer
#     # @return an integer
#     def push(self, x):
#         if len(self.stack) == 0:
#             self.stack.append(x)
#             self.minimums.append(x)
#         else:
#             self.stack.append(x)
#             if x < self.minimums[-1]:
#                 self.minimums.append(x)
#             else:
#                 self.minimums.append(self.minimums[-1])

#     # @return nothing
#     def pop(self):
#         if len(self.stack) != 0:
#             self.stack.pop()
#             self.minimums.pop()

#     # @return an integer
#     def top(self):
#         if len(self.stack) == 0:
#             return -1
#         else:
#             return self.stack[-1]

#     # @return an integer
#     def getMin(self):
#         if len(self.stack) == 0:
#             return -1
#         else:
#             return self.minimums[-1]
    
#     def __init__(self):
#         self.stack = []
#         self.minimums = []

# stack<int> st;
# int mn=INT_MAX;
# MinStack::MinStack() {
#      while(!st.empty()){st.pop();}
# }
# void MinStack::push(int x) {
#     if(st.empty()){mn = x;}
#     else if(mn>=x){
#         st.push(mn);
#         mn = x;
#     }st.push(x);
# }

# void MinStack::pop() {
#     if(!st.empty()){
#         if(st.top()==mn){
#             st.pop();
#             if(!st.empty()){mn = st.top();st.pop();}
#             return;
#         }
#         st.pop();
#     }
# }

# int MinStack::top() {
#     if(st.empty()){return -1;}
#     return st.top();
# }

# int MinStack::getMin() {
#     if(st.empty()){return -1;}
#     return mn;
# }