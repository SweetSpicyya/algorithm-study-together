# {383}. {Ransom Note}

**Link:** https://leetcode.com/problems/ransom-note
**Difficulty:** Easy
**Topic:** Hash Table, String, Counting

## Problem Summary

Determine whether a given string can be constructed by using the letters from the other given string

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by iterating through each character in ransomBote and checking if it exists in magazine. However, this would require scanning magazine for every character in ransomNote, resulting in O(n\*m) tima complexity.
- **Optimization**: Instead of scanning magazine repeatedly, I used a hashmap where each key is a character from magazine and its value is the frequency of that character. And then ransomNote iterates the map and decrement the count for each character used. If a character is missing from the map of its count drops to 0, I return false immediately.
- **Complexity Analysis**:
  Time: O(n+m) - one pass through magazine, one pass through ransomNote
  Space: O(1) - at most 26 lowercase letters in the map, so the map size is constant regardless of input size.
