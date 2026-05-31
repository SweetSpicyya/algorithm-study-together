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

## Approaches & Discussion
### Angela

- So, this problem is asking me to reverse a singly linked list and return the new head.
- I will approach this **iteratively** using two main pointers, `prev` and `curr`, to reverse the arrows in-place. Let me explain the logic.
First, I'll initialize `curr` to the `head` of the list and `prev` to `null`.
Then, I'll use a `while` loop that continues as long as `curr` is not `null`. Inside the loop, I will do four steps:
1. I'll temporarily store the next node in a `tmp` variable so I don't lose the rest of the list.
2. I'll reverse the pointer of the current node to point to `prev`.
3. I'll move the `prev` pointer one step forward to `curr`.
4. I'll move the `curr` pointer one step forward using the `tmp` variable.
Once the loop finishes, `curr` will fall off the end of the list, and `prev` will safely point to the new head. So, I'll return `prev`.
- This runs in **$O(N)$ time complexity** because we visit each node exactly once. The **space complexity is $O(1)$** constant space because we only use a few pointers to reverse the list in-place, without allocating any extra memory