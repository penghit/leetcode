# This file contains the explantion of the method used for the problems

## Leetcode 444
For **org** to be uniquely reconstructible from **seqs** we need to satisfy 2 conditions:
1. Every sequence in **seqs** should be a subsequence in **org**. This part is obvious.
1. Every 2 consecutive elements in **org** should be consecutive elements in some sequence from **seqs**. Why is that? Well, suppose condition 1 is satisfied. Then for 2 any consecutive elements x and y in **org** we have 2 options. We have both x and y in some sequence from **seqs**. Then (as condition 1 is satisfied) they must be consequtive elements in this sequence. There is no sequence in **seqs** that contains both x and y. In this case we cannot uniquely reconstruct **org** from **seqs** as sequence with x and y switched would also be a valid original sequence for **seqs**.
