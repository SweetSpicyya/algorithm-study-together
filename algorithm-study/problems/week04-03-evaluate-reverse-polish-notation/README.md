# {150}. {Evaluate Reverse Polish Notation}

<<<<<<< HEAD
**Link:** https://leetcode.com/problems/binary-tree-level-order-traversal

**Difficulty:** Medium
**Topic:** Array, Math, Stack

## Problem Summary
Return an integer that represents the value of the expression.


## Approaches & Discussion
### Yourim
Approach: We can solve this problem efficiently using a Stack data structure to evaluate the expression in a single pass.
Algorithm: As we iterate through the tokens, we push numbers onto the stack. when we encounter an operator, we pop the top two numbers.
Order of Operation: The first popped number is the right operand and the second is the left operand, which we evaluate and push the result back onto the stack.
Complexity: This takes O(N) time and O(N) space, where N is the number of tokens, since we process each token exactly once.

## Approaches & Discussion
### Rachel
- **Problem Summary**: Evaluate the expression in Reverse Polish Notation and return the result as an integer.
- **Plan**: I'll iterate through each token. If it's a number, I convert it to an integer and push it onto the stack. If it's an operator, I pop two values, last in first(b) then first in last, apply the operation in a operation b order, and push the result back. At the end, the stack will have exactly one value which is the answer.
- **Evaluate**: Time complexity is O(n) since each token is processed exactly once. Space complexity is O(n) in the worst case all tokens are numbers and get pushed onto the stack.

## Approaches & Discussion
### Angela

- **So this problem is asking me** to evaluate the value of a Reverse Polish Notation expression.
- **We should traverse** all values in the array, so O(n) is already optimal.
- **My approach is to** use stack and while iterating over the tokens, if the current token is an operator, pop the two most recent values from the stack. Next, calculate using the current operator,  push the result to stack again otherwise, push the value onto the stack. The remaining value in the stack is the result.
- **This runs in** O(n) time complexity because this approach iterates over all values in the array and O(n) space complexity since the stack can hold up to n values of array
