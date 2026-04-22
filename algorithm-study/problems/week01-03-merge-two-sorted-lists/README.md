# {22}. {Merge Two Sorted Lists}

**Link:** https://leetcode.com/problems/merge-two-sorted-lists/  
**Difficulty:** Easy
**Topic:** Linked List, Recursion

## Problem Summary
Merge two linked lists into one single linked list.

## Approaches & Discussion
### Angela

- **Approach**: At  first, I thought that using one list like a pointer and compare with others and save the smaller value in a new array list. 
- **My way** : Make a new Linkedlist called dummy and a new pointer called cur. Using 'while' loop, compare the node which has the smaller value and connect to 'dummy'. When the logic finish, return 'dummy.next' since now 'dummy' ponits to a fake start node. The time complexity is O(n+m) 
- **Better way** : Reduce conditional sentence like 'cur.next = list1 or list2'. Because, 'or' returns truthy value in Python so "list1 or list2" means if the list1 exists, return list1 otherwise return list2.

