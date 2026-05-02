# {110}. {Balanced Binary Tree}

**Link:** https://leetcode.com/problems/balanced-binary-tree/

**Difficulty:** Easy

**Topic:** Tree, Depth-First Search, Binary Tree

## Problem Summary
Determine if given a binary tree is height-balanced

## Approaches & Discussion
### Angela

- **This problem is asking me to** determine if given a binary tree is height-balanced.
- **The brute force could be to** traverse all nodes in the tree and calculate each height which runs in O(n^2) **but this is wasteful since** it recalculates heights repeatedly for the same nodes.
- **We can optimize by** using DFS, **reducing it to** O(n) since we can calculate each height of each node in a single pass.
- **My approach is to** make DFS function and use left_h, right_h variables to calculate each side's height recursively. And check the left_h or right_h return -1 or the difference of left_h and right_h greater than 1. If it is, return -1 to indicate imbalance otherwise return the current height. if the final return value is -1, return False.
- **This runs in** O(n) time complexity because this approach calculates heights of all nodes in the tree in a single pass and O(logn) space complexity in the best case or O(n) in the worst case since the call stack can grow up to O(n) due to recursive calls


## Problem Summary

Determine if given binary tree is height-balanced

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by identifying patterns based on the number of nodes and the position of null values in the array.
- **Optimization**: Instead of computing height and balance check separately, I combined both into a single DFS traversal using a helper function getHeight(). The key insight is using -1. Normally getHeight() returns the actual height of a subtree, but when imbalance is detected, it immediately returns -1 as an error signal. If either left or right is -1, we propagate -1 upward.
- **Complexity Analysis**: Time Complexity: O(n) - each node is visited exactly once during the DFS traversal
  Space Complexity: O(h) = the call stack grows as deep as the height of the tree, where h is O(log n) for a balanced tree and O(n) in the worst case


