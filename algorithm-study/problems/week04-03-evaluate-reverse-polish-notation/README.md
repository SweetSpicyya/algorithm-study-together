# {150}. {Evaluate Reverse Polish Notation}

**Link:** https://leetcode.com/problems/evaluate-reverse-polish-notation/
**Difficulty:** Medium
**Topic:** Array, Math, Stack

## Approaches & Discussion

### Rachel

- **Problem Summary**: Evaluate the expression in Reverse Polish Notation and return the result as an integer.
- **Plan**: I'll iterate through each token. If it's a number, I convert it to an integer and push it onto the stack. If it's an operator, I pop two values, last in first(b) then first in last, apply the operation in a operation b order, and push the result back. At the end, the stack will have exactly one value which is the answer.
- **Evaluate**: Time complexity is O(n) since each token is processed exactly once. Space complexity is O(n) in the worst case all tokens are numbers and get pushed onto the stack.
