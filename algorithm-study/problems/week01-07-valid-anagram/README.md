# {242}. {Valid Anagram}

**Link:** https://leetcode.com/problems/valid-anagram/description/
**Difficulty:** Easy
**Topic:** Hash Table, String, Sorting

## Problem Summary

Determine whether t is an anagram of s

## Approaches & Discussion

### Rachel

- **My way**: I thought about comparing unique characters using Set, but I realized that character frequency matters. It the string contains repetitive characters, Set won't work.
- **Better way**: Use a Hash Map with characters as keys and their frequencies as values. After populating the map with string s, iterate through string t and substract the count of each character one by one to verify the anagram.
