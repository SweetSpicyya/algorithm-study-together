# {Problem Number}. {Problem Title}

**Link:** https://leetcode.com/problems/merge-two-sorted-lists/description/
**Difficulty:** Easy
**Topic:** Linked List, Recursion

## Problem Summary

Merge two linked lists into one single linked list.

## Approaches & Discussion

### Rachel

- Approach: At first, I thought they were arrays, so I tried to merge and sort. After I realized they were linked lists, I planned to push the values into an array and sort them, and make them into the nodes.
- Better way: Create a dummy to act as the start. Compare the value of elements of the lists and link the smaller node to the next. Return dummys next at the end to figure out what the real starting point is.
- P.S.: Try other linked-list problems for your further understandings!
  - https://leetcode.com/problems/remove-duplicates-from-sorted-list/
  - https://leetcode.com/problems/reverse-linked-list/*
