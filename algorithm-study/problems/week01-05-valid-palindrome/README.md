# {125}. {Valid Palindrome}

**Link:** https://leetcode.com/problems/valid-palindrome/  
**Difficulty:** Easy
**Topic:** Two Pointers, String

## Problem Summary

Determine if the given string is a palindrome.

## Approaches & Discussion

### Angela

- **Approach**: Remove non-alphanumeric characters and convert uppercase characters to lowercase. And using two-pointers called right and left, compare each value which pointed each pointers. If they are not the same, break the loop and return False. 
- **My way**: At first, check whether the string 's' includes non-alphanumeric characters and save only alphanumeric characters to a new string 'str1'. Convert all characters in 'str1' to lowercase. Using While-loop with two-pointers, compare each value which pointed by pointers. If the values are not the same, set the result value to 'False' and break the loop. The time complexity is O(n).
- **Better way**: Because we can check whether the string 's' includes non-alphanumeric characters and compare each value at the same time, we can merge two loops to reduce the code and execution time. (135ms -> 14ms)
