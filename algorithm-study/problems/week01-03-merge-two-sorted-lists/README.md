# {22}. {Merge Two Sorted Lists}

**Link:** https://leetcode.com/problems/merge-two-sorted-lists/  
**Difficulty:** Easy
**Topic:** Linked List, Recursion

## Problem Summary
Merge two linked lists into one single linked list.

## Approaches & Discussion
### Yourim
- **Approach**: Iterate through both lists, compare the values and link the smaller or equal node to a new merged list.
- **My way** : Employs a nested loop structure where for each node in list1, all smaller or equal nodes from list2 are attached first.
While it correctly merges the lists in-place, the logic is more complex to maintain and slightly less intuitive than a single-pass
- **Better way** : Uses a single while loop to compare the heads of both lists simultaneously, picking the smaller node at each step.
This is the standard O(n+m) approach that minimize conditional checks and results in cleaner, more readable code


