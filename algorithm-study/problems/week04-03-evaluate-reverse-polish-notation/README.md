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
