# {206}. {Reverse Linked List}

**Link:** https://leetcode.com/problems/reverse-linked-list/
**Difficulty:** Easy
**Topic:** Linked List, Recursion

## Approaches & Discussion

### Rachel

- **Understand**: We've given the head of a singly linked list and need to reverse it in place.
- **Match**: This is a classic iterative pointer manipulation problem. We need three pointers, prev, curr, and next, to reverse the direction of each node's next pointer one at a time without losion the rest of the list.
- **Plan**: I'll initialize prev=null and curr=head. On each iteration, I save curr.next as next before overwriting it, then point curr.next to prev to reverse the arrow. Then I advance prev to curr and curr to next. When curr reaches null, prev is pointing at the new head.
- **Evaluate**:
  Time: O(n) - every node is visited exactly once
  Space: O(1) - only three pointers used regardless of input size
