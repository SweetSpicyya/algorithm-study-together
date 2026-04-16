# {125}. {Valid Palindrome}

**Link:** https://leetcode.com/problems/valid-palindrome/  
**Difficulty:** Easy
**Topic:** Two Pointers, String

## Problem Summary

Determine if the given string is a palindrome.

## Approaches & Discussion

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

### Rachel

- **Approach**: Use two pointers starting from both ends to compare alphanumeric characters and determine if the string is a palindrome.
- **My way**: I converted the string to lowercase and used a regular expression to extract only aphanumeric characters. Then I iterated through the array, comparing elements from both ends using their indices.
- **Better way**: Compare the original filtered string with its reversed version.

### Angela

- **Approach**: Remove non-alphanumeric characters and convert uppercase characters to lowercase. And using two-pointers called right and left, compare each value which pointed each pointers. If they are not the same, break the loop and return False. 
- **My way**: At first, check whether the string 's' includes non-alphanumeric characters and save only alphanumeric characters to a new string 'str1'. Convert all characters in 'str1' to lowercase. Using While-loop with two-pointers, compare each value which pointed by pointers. If the values are not the same, set the result value to 'False' and break the loop. The time complexity is O(n).
- **Better way**: Because we can check whether the string 's' includes non-alphanumeric characters and compare each value at the same time, we can merge two loops to reduce the code and execution time. (135ms -> 14ms)
