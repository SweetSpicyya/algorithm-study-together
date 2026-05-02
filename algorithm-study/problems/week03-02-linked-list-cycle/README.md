# {141}. {Linked List Cycle}

**Link:** https://leetcode.com/problems/linked-list-cycle/description/

**Difficulty:** Easy

**Topic:** Hash Table, Linked List, Two Pointers

## Problem Summary
Determine if the given linked list has a cycle in it

## Approaches & Discussion
### Angela

- **This problem is asking me to** determine if the given head which is linked list has a cycle in it.
- **The brute force could be to** traverse and compare every node which runs in O(n^2) but it's wasteful since we could traverse every node once.
- **We can optimize this by** using hash map which runs in O(n).
- **My approach is to** make hash map to check whether if the node already visited before. Before traverse the nodes, if the head is None, return False. While traversing the head, if the current node is already in the visited hashmap return True, otherwise save it as key and True as value to visited and move to next node.
- **This runs in** O(n) time complexity because this approach traverses every node in the linkedlist and O(n) space complexity since the hashmap can hold up to n nodes