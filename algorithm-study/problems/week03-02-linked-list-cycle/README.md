# {141}. {Linked List Cycle}

**Link:** https://leetcode.com/problems/linked-list-cycle
**Difficulty:** Easy
**Topic:** Hash Table, Linked List, Two Pointers

## Problem Summary

Determine if given linked list has a cycle in it

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by traversing the linked list and storing each visited node in a Set. At each step, I check if the current node already exists in the Set.
- **Optimization**: Instead of using a Set to track visited nodes, I applied Floyd's Cycle Detection algorithm using two pointers. If a cycle exists, fast pointer will eventually lap slow pointer and they will meet at the same node. If there is no cycle, fast will reach null first.
- **Complexity Analysis**: Time: O(n), Space: O(n) - Each node visited once, but all nodes stored in a Set.
