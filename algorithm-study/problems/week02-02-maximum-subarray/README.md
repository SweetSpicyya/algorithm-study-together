# {53}. {Maximum Subarray}

**Link:** https://leetcode.com/problems/maximum-subarray/  
**Difficulty:** Medium
**Topic:** Array, Divide and Conquer, Dynamic Programming

## Problem Summary
Find the subarray with the largest sum in given array, and return its sum.

## Approaches & Discussion
### Yourim
- **Coding interview**:
So, my first approach is just brute-force it.
Simply try every possible subarray using nested loop.
But using nested loop takes nxn time complexity, so it's not efficient.
So how do we optimize it?
I think we need global max sum variable to keep maximum sum.
And compare current item and sum that summed so far and then, get max result between those.
if current item is greater than sum, the result will be current item.
Now compare global max sum variable and previous result, that will be the largest sum.
Time complexity is O(n) because it iterates the given array once.
