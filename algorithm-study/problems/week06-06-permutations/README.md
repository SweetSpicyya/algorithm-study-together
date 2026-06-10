# {46}. {Permutations}

**Link:** https://leetcode.com/problems/permutations
**Difficulty:** Medium
**Topic:** Array, Backtracking

## Problem Summary
return all the possible permutations in given array.

## Approaches & Discussion
### Yourim
This solution uses backtracking with a recursive helper function to generate all possible permutations. 
We maintain a visited boolean array to keep track of which numbers are already used in the current path. 
The recursive function acts as a decision tree, iterating through every number and building up a curr_permutation list. 
Once the list reaches the same length as the input array, a copy of it is added to our final result list. 
After each deep dive, the code performs backtracking by popping the last element and resetting its visited status back to False to explore the next alternative path.