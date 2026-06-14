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


## Approaches & Discussion
### Yourim
- **Coding interview**:
<details>
  <summary>Click to view details </summary>

So this problem is asking to determine whether a binary tree is height-balanced, meaning for every node in the tree, 
the height difference between its left and right subtrees is no greater than one.
A naive approach would be O(n²), where for each node, we separately calculate the height of its left and right subtrees. 
Instead, I'm using a single-pass post-order DFS that computes height and validates balance simultaneously.
I define a helper function check(node) that returns the height of the subtree rooted at that node, but uses -1 as a sentinel value to signal that an imbalance has already been detected somewhere below.
The base case is straightforward, a null node has height zero.
Then I recurse left first. If the left subtree already returned -1, I short-circuit and propagate that -1 immediately, no need to explore further.
Same thing for the right subtree.
Once I have both heights, I check if their absolute difference exceeds 1. If it does, this node is the point of imbalance, so I return -1.
Otherwise, the subtree rooted here is balanced, so I return its actual height, which is max(left, right) + 1.
Finally, the outer function just checks whether check(root) is not -1.
Time complexity is O(n) since every node is visited exactly once. Space complexity is O(h) where h is the height of the tree.
</details>
