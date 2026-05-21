# {150}. {Evaluate Reverse Polish Notation}

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
