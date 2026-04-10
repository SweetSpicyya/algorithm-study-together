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

## Approaches & Discussion
### Rachel

- Approach: At first, I was planning to count the number of close bracket because I misunderstand the third condition. However, I noticed the topic of the problem and I tried to use stack.
- My way: put into the stack when it's open bracket, and matches the same type of close bracket.
- Better way: I create a map with open brackets as keys and their corresponding close bracket as values. I pushed open brackets onto a stack and upon encuntering a closing bracket, verified if it matched the value of the most recent element popped from the stack

## Approaches & Discussion
### Angela

-Approach : At first, I tried to solve the problem using Binary Search but It couldn't handle cases like '(){}[]' and next, I tried to solve it using Hashmap    
-My way : Using Hashmap with Stack, I can deal with key-value pair and check the latest opening brackets that match with closing brackets.  The time complexity is O(n)  
-Better way : Don't need to use 'status' variable cuz can recognize True or False by checking the stack is empty or not. Using this, can simplify the code.