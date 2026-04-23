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

### Yourim

- **Coding interview**:
  So before I dive in, just to clarify
  "are we considering only ASCII alphanumeric characters, and is an empty string treated as a valid palindrome?"
  My initial approach would be to convert everything to lowercase, remove non-alphanumeric characters using regex,
  then find the midpoint of the cleaned string and expand outward from there, comparing left and right characters as I go.
  If everything matches I return true, if anything mismatches I return false.
  This works, but one thing I want to flag is that even-length strings don't have a single center character, so I'd need to handle that edge case separately.
  For even-length strings the right pointer starts at the midpoint and the left pointer starts at mid minus one.

  A cleaner approach that avoids that edge case entirely is two pointers. I put one pointer at the very start and one at the very end and walk them toward each other.
  Whenever I hit a non-alphanumeric character I just skip it, and when both pointers are on valid characters I compare them. If there's a mismatch I return false immediately,
  otherwise I keep going until the pointers cross and return true. That also brings space down to O(1) while keeping time at O(n),
  since we're operating directly on the original string with no extra allocation.
