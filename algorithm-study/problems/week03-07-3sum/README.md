# {15}. {3Sum}

**Link:** https://leetcode.com/problems/3sum/

**Difficulty:** Medium

**Topic:** Array, Two Pointers, Sorting

## Problem Summary
Find all triplets whose sum is 0 from the given integer array nums

## Approaches & Discussion
### Angela

- **This problem is asking me to** find all triplets whose sum is 0 from the given integer array nums.
- **The brute force would be** to iterate over all possible triplets from nums which runs in O(n^3) but it's wasteful because we can use sorting to efficiently narrow the search range with two pointers.
- **We can optimize this by** using sorting and two-pointer, reducing it to O(n^2).
- **My approach is to** sort nums and iterate over nums with fixed index and setting two pointers as index+1, length of nums -1. And to avoid duplication, if the current index or pointer has the same value as the previous one, skip it. Next, if total sum with nums[index], nums[left], nums[right] is 0, append to result array or if total sum is less than 0, move the left pointer to right otherwise move the right pointer to left. Lastly return the result array.
- **This runs in** O(n^2) time complexity because this approach iterates all possible triplets with fixed index and O(n) space complexity since the result array can hold up to O(n) triplets.