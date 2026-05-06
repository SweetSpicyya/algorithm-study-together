# {232}. {Implement Queue using Stacks}

**Link:** https://leetcode.com/problems/implement-queue-using-stacks/
**Difficulty:** Easy
**Topic:** Stack, Design, Queue

## Problem Summary
Implement a first in first out (FIFO) queue using only two stacks

## Approaches & Discussion
### Yourim
- **Coding interview**:
<details>
  <summary>Click to view details </summary>
This problem asks us to implement a queue using only stacks.
The core challenge is that a stack is LIFO but a queue is FIFO — so we need to reverse that order somehow. The trick is using two stacks.
I maintain an in_stack for incoming elements and an out_stack for outgoing. Push always goes to in_stack in O(1). The key is the _move helper — it transfers everything from in_stack to out_stack, but only when out_stack is empty. That reversal is what gives us FIFO order.
Pop and peek both call _move first, then operate on out_stack. Empty just checks that both stacks have nothing left.
The important thing to highlight here is the amortized time complexity. Each element is moved at most once — pushed onto in_stack once, popped and transferred to out_stack once. So even though a single pop could trigger an O(n) transfer, averaged across all operations it's O(1) amortized. Space is O(n).
The naive alternative would be to re-sort the stack on every push or pop, but that's O(n) per operation.
</details>


## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by transferring all elements from stack1 to stack2 on every pop and peek call. Pushing all elements form stack1 into stack2 reverses the order, making the first element accessible from the top of the stack2. However, this caused a bug, if pop was called after elements were already in stack2, transferring stack1 again would mix the order.
- **Optimization**: The fix was to only transfer from stack1 to stack2 when stack2 is empty. This way, leftover elements in stack2 are consunmed first before refilling from stack1.
- **Complexity Analysis**:
  push - Time: O(1), Space: O(n)
  pop/peek - Time: worst case O(n) amortized O(1), Space: O(1)
  empty - Time: O(1), Space: O(1), Space: O(1)
