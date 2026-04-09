# {20}. {Valid Parentheses}

**Link:** https://leetcode.com/problems/valid-parentheses/  
**Difficulty:** Easy
**Topic:** String, Stack

## Problem Summary
Validate each open bracket matches its close bracket

## Approaches & Discussion
### Yourim
- Approach: Store closing brackets as keys in a dictionary to validate pairs within a loop.
- My way : Iterate through the string and push each character onto a stack.
When it encounter a closing bracket (stored as a key in a map), compare it with the top item of the stack.
if the top item matches the corresponding opening bracket value from the map, pop it from the stack.
Otherwise, leave it After the loop finishes, if the stack is empty, return true.
- Better way : To optimize the process, implement an early return strategy.
If the stack is empty(it means there is no opening bracket) or the top item doesn't match the closing brackets, 
return false immediately to avoid unnecessary iterations.