# {232}. {Implement Queue using Stacks}

**Link:** https://leetcode.com/problems/implement-queue-using-stacks
**Difficulty:** Easy
**Topic:** Stack, Design, Queue

## Problem Summary

Implement a FIFO queue using two stacks.

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by transferring all elements from stack1 to stack2 on every pop and peek call. Pushing all elements form stack1 into stack2 reverses the order, making the first element accessible from the top of the stack2. However, this caused a bug, if pop was called after elements were already in stack2, transferring stack1 again would mix the order.
- **Optimization**: The fix was to only transfer from stack1 to stack2 when stack2 is empty. This way, leftover elements in stack2 are consunmed first before refilling from stack1.
- **Complexity Analysis**:
  push - Time: O(1), Space: O(n)
  pop/peek - Time: worst case O(n) amortized O(1), Space: O(1)
  empty - Time: O(1), Space: O(1), Space: O(1)
