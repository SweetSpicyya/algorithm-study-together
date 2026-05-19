# {150}. {Evaluate Reverse Polish Notation}

**Link:** https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

**Difficulty:** Medium

**Topic:** Array, Math, Stack

## Problem Summary
return a deep copy(clone) of the given graph of a connected undirected graph

## Approaches & Discussion
### Angela

- **So this problem is asking me** to evaluate the value of a Reverse Polish Notation expression.
- **We should traverse** all values in the array, so O(n) is already optimal.
- **My approach is to** use stack and while iterating over the tokens, if the current token is an operator, pop the two most recent values from the stack. Next, calculate using the current operator,  push the result to stack again otherwise, push the value onto the stack. The remaining value in the stack is the result.
- **This runs in** O(n) time complexity because this approach iterates over all values in the array and O(n) space complexity since the stack can hold up to n values of array