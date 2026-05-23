# {3}. {Longest Substring Without Repeating Characters}

**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters
**Difficulty:** Medium
**Topic:** Staff, Hash Table, String, Sliding Window

## Problem Summary

Find the length of the longest substiring without duplicate charaters, given a string

## Approaches & Discussion
### Yourim

naive approach is we use two loops. The outer loop picks a starting point, and the inner loop keeps extending the substring character by character. 
Every time we hit a duplicate, we record the length of what we built so far and break out. We do this for every possible starting position and return the max.
Time complexity is O(N²). For each of the N starting points we're potentially scanning the whole string again.
Instead of restarting from scratch every time we hit a duplicate, we can just slide the window forward. 
We keep a start pointer and an end pointer, and we expand end one step at a time. When we hit a character that's already inside the window, we jump start right past the previous occurrence of that character.
And the way we track positions is with a hash map. we store each character's most recent index. So when we see a duplicate, we know exactly where to move start.
when we find a duplicate, we only move start if the previous occurrence is actually inside the current window. 
Otherwise we might move start backwards which would break everything.
At every step we compute the current window length as end - start + 1 and update the max.
Time complexity is O(N). We move end through the string once. 
Space is O(1). The map holds at most 26 keys for lowercase letters.