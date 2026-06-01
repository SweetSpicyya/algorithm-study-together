# {206}. {Reverse Linked List}

**Link:** https://leetcode.com/problems/reverse-linked-list
**Difficulty:** Easy
**Topic:** Linked List, Recursion

## Approaches & Discussion
### Yourim
Goal: I'll explain how to reverse a singly linked list, which can be solved either iteratively or recursively.
Iterative Idea: The optimal approach uses three pointers—prev, curr, and a temporary next_node to reverse the links one by one.
Iterative Steps: In a loop, we save curr. next, point curr.next to prev, and then shift both prev and curr one step forward.
Recursive Alternative: Alternatively, we can use recursion to reach the tail first, then reverse the pointers backwards as the call stack pops.
Complexity: Both methods take O(N) time, but the iterative approach is preferred because it uses efficient O(1) space instead of O(N) stack space.