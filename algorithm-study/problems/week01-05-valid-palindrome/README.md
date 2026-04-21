# {125}. {Valid Palindrome}

**Link:** https://leetcode.com/problems/valid-palindrome/  
**Difficulty:** Easy
**Topic:** Two Pointers, String

## Problem Summary

Determine if the given string is a palindrome.

## Approaches & Discussion

### Rachel

- **Approach**: Use two pointers starting from both ends to compare alphanumeric characters and determine if the string is a palindrome.
- **My way**: I converted the string to lowercase and used a regular expression to extract only aphanumeric characters. Then I iterated through the array, comparing elements from both ends using their indices.
- **Better way**: Compare the original filtered string with its reversed version.
