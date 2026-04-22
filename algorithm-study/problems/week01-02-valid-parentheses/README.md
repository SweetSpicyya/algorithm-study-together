# {20}. {Valid Parentheses}

**Link:** https://leetcode.com/problems/valid-parentheses/  
**Difficulty:** Easy
**Topic:** String, Stack

## Problem Summary
Validate each open bracket matches its close bracket

## Approaches & Discussion
### Angela

- Approach : At first, I tried to solve the problem using Binary Search but It couldn't handle cases like '(){}[]' and next, I tried to solve it using Hashmap    
- My way : Using Hashmap with Stack, I can deal with key-value pair and check the latest opening brackets that match with closing brackets.  The time complexity is O(n)  
- Better way : Don't need to use 'status' variable cuz can recognize True or False by checking the stack is empty or not. Using this, can simplify the code.