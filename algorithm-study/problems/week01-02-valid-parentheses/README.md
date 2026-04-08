# {Problem Number}. {Problem Title}

**Link:** https://leetcode.com/problems/valid-parentheses/description/  
**Difficulty:** Easy
**Topic:** String, Stack

## Problem Summary

Validate each open bracket matches its close bracket

## Approaches & Discussion

### Rachel

- Approach: At first, I was planning to count the number of close bracket because I misunderstand the third condition. However, I noticed the topic of the problem and I tried to use stack.
- My way: put into the stack when it's open bracket, and matches the same type of close bracket.
- Better way: I create a map with open brackets as keys and their corresponding close bracket as values. I pushed open brackets onto a stack and upon encuntering a closing bracket, verified if it matched the value of the most recent element popped from the stack
