# {Problem Number}. {Problem Title}

**Link:** https://leetcode.com/problems/two-sum/  
**Difficulty:** Easy
**Topic:** Array, Hash Table

## Problem Summary

Get indices of the two numbers to add up to target number

## Approaches & Discussion

### Angela

- Approach: Search for two numbers that add up to the target by comparing each element with the others.
- My way: I first tried a brute force approach using double loops to check every possible pair in the array.
- Cons : The $O(n^2)$ time complexity was too slow for large inputs, resulting in a Time Limit Exceeded (TLE) error.
- Better way : Switched to a Hash Map approach. By storing {value : index}, I can find the required complement($target - element$) in $O(1)$ time with a single pass, achieving $O(n)$ complexity.