# {409}. {Longest Palindrome}

**Link:** https://leetcode.com/problems/longest-palindrome

**Difficulty:** Easy
**Topic:** Junior, Hash Table, String, Greedy

## Problem Summary
Return the length of the longest palindrome that can be built with given letters.

## Approaches & Discussion
### Yourim
let me walk you through my approach for this problem. 
The goal is to find the length of the longest palindrome we can build using the characters from the given string.
To form a palindrome, characters need to be mirrored on both sides. 
This means we need an even number of each character to place them symmetrically. 
If a character appears an odd number of times, we can still use most of them by taking the largest even number 
less than that count—essentially count - 1.
Also, a palindrome can have at most one unique character in the dead center. So, if there are any characters with an odd count, 
we can pick one of them to sit right in the middle, which adds 1 to our total length.
Time complexity is O(n).
