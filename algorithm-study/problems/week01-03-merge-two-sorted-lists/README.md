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


## Approaches & Discussion
### Rachel

- Approach: At first, I thought they were arrays, so I tried to merge and sort. After I realized they were linked lists, I planned to push the values into an array and sort them, and make them into the nodes.
- Better way: Create a dummy to act as the start. Compare the value of elements of the lists and link the smaller node to the next. Return dummys next at the end to figure out what the real starting point is.
- P.S.: Try other linked-list problems for your further understandings!
  - https://leetcode.com/problems/remove-duplicates-from-sorted-list/
  - https://leetcode.com/problems/reverse-linked-list/*


## Approaches & Discussion
### Angela

- **Approach**: At  first, I thought that using one list like a pointer and compare with others and save the smaller value in a new array list. 
- **My way** : Make a new Linkedlist called dummy and a new pointer called cur. Using 'while' loop, compare the node which has the smaller value and connect to 'dummy'. When the logic finish, return 'dummy.next' since now 'dummy' ponits to a fake start node. The time complexity is O(n+m) 
- **Better way** : Reduce conditional sentence like 'cur.next = list1 or list2'. Because, 'or' returns truthy value in Python so "list1 or list2" means if the list1 exists, return list1 otherwise return list2.

