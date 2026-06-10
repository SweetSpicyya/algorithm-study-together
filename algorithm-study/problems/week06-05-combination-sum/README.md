# {39}. {Combination Sum}

**Link:** https://leetcode.com/problems/combination-sum
**Difficulty:** Medium
**Topic:** Array, Backtracking

## Problem Summary
return a list of all unique combinations of candidates where the chosen numbers sum to target.

## Approaches & Discussion
### Yourim
The problem requires finding a target's index in a rotated sorted array in O(log n) time, which dictates using a modified Binary Search. 
No matter where you split a rotated sorted array in half, at least one of the halves is guaranteed to be perfectly sorted. Calculate mid and compare nums[left] with nums[mid] to determine which half (left or right) is normally sorted.
Check if the target falls within the boundaries of that sorted half (e.g., nums[left] <= target < nums[mid]). If the target is within the sorted half, narrow the search to that side. 
otherwise, move the pointers to search the opposite half, halving the array each time.