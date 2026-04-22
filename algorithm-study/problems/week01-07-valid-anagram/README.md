# {242}. {Valid Anagram}

**Link:** https://leetcode.com/problems/valid-anagram/
**Difficulty:** Easy
**Topic:** Hash Table, String, Sorting

## Problem Summary

Determine whether t is an anagram of s

## Approaches & Discussion

### Angela

- **Understand** : So the problem is asking me to determine whether two strings are valid anagrams.
- **Brute force**: The brute force way would be to sort both strings and compare which runs in O(nlogn).
- **Better way** : We can optimize this by using the hashmap.
- **Approach**: My approach is to create a Hashmap and save the characters as key in 's' and the count as value. After then, using loop and check whether the characters in 't' includes in hashmap. If it exists, decrement the count, otherwise set the result to 'False' and return. Finally, if any value in the hashmap is not zero, set the result to 'False' and return the result.
- **Complexity** : This runs in O(n) time complexity since this approach visits every character in the string and O(1) which is constant space complexity because the hashmap can hold at most 26 unique characters.