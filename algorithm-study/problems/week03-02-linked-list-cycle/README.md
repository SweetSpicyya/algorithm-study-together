# {141}. {Linked List Cycle}

**Link:** https://leetcode.com/problems/linked-list-cycle/
**Difficulty:** Easy
**Topic:** Hash Table, Linked List, Two Pointers

## Problem Summary
Search if there is a cycle in a linked list.

## Approaches & Discussion
### Yourim
- **Coding interview**:
<details>
  <summary>Click to view details </summary>
This problem asks to detect whether a linked list contains a cycle.
My first approach is using a HashSet. The idea is simple. if we ever visit a node we've already seen, there's a cycle. 
I traverse the list and at each node, check if it's already in the set. If it is, return True. If we reach null, return False. 
Time complexity is O(n), space is O(n) since we're storing every node reference.
That works, but we can do better on space. That leads me to Floyd's Cycle Detection.
The insight is if a cycle exists, a fast pointer moving twice as fast as a slow pointer will eventually meet it. 
I start both at head, slow moves one step, fast moves two. If they ever point to the same node, there's a cycle. If fast falls off the end, there isn't.
Time complexity stays O(n), but space drops to O(1), just two pointers, nothing extra.
In an interview I'd always present the HashSet solution first to establish correctness, then optimize with Floyd's. 
That brute force to optimal progression is exactly what interviewers want to see. And a common follow-up, Floyd's can also be extended to find the exact node where the cycle begins.
</details>

