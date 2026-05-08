# {3}. {Longest Substring Without Repeating Characters}

**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters
**Difficulty:** Medium
**Topic:** Staff, Hash Table, String, Sliding Window

## Problem Summary

Find the length of the longest substiring without duplicate charaters, given a string

## Approaches & Discussion

### Rachel

- **Optimization**: I approached this problem using a sliding window with two pointers and a hashmap. As a end pointer moves through the string, I store each character's most recent index in the map. When a duplicate is detected, I slide a start pointer to one position after the duplicate's previous position. At each step, I update max by comparing the current window size with the previous maximum.
- **Complexity Analysis**:
  Time: O(n) - each character is visited once as end moves through the string
  Space: O(1) - the map stores at most 26 lowercase letters, so the size is constant regardless of input
