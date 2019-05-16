# This file contains the explantion of the method used for the problems

## Leetcode 207
In the answer, we used the depth first search to see if there are cycles in a digraph, in each depth search, we keep an stack, which
contains the node visited on this specfic depth first search. If when visiting the edge v->w, we find that w already on the stack, then 
there must be a cycle. Because if w is on the stack, this means there must be a path from w to v, and the edge v->w will form a cycle.

## Leetcode 444
This explantion comes from user **dettier** on leetcode
For **org** to be uniquely reconstructible from **seqs** we need to satisfy 2 conditions:
1. Every sequence in **seqs** should be a subsequence in **org**. This part is obvious.
1. Every 2 consecutive elements in **org** should be consecutive elements in some sequence from **seqs**. Why is that? Well, suppose condition 1 is satisfied. Then for 2 any consecutive elements x and y in **org** we have 2 options. We have both x and y in some sequence from **seqs**. Then (as condition 1 is satisfied) they must be consequtive elements in this sequence. There is no sequence in **seqs** that contains both x and y. In this case we cannot uniquely reconstruct **org** from **seqs** as sequence with x and y switched would also be a valid original sequence for **seqs**.
