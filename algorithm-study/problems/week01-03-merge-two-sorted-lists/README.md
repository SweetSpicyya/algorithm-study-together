# {Problem Number}. {Problem Title}

**Link:** https://leetcode.com/problems/merge-two-sorted-lists/description/
**Difficulty:** Easy
**Topic:** Linked List, Recursion

## Problem Summary

Merge two linked list into one single linked list.

## Approaches & Discussion

### Rachel

- Approach: At first, I was planning to count the number of close bracket because I misunderstand the third condition. However, I noticed the topic of the problem and I tried to use stack.
- Better way: Create a dummy to act as the start. Compare the value of elements of the lists and link the smaller node to the next. Return dummys next at the end to figure out what the real starting point is.
- P.S.: Try other linked-list problems for your further understandings!
  - https://leetcode.com/problems/remove-duplicates-from-sorted-list/
  - https://leetcode.com/problems/reverse-linked-list/*
