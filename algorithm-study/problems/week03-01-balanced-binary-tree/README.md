# {110}. {Balanced Binary Tree}

**Link:** https://leetcode.com/problems/balanced-binary-tree
**Difficulty:** Easy
**Topic:** Tree, Depth-First Search, Binary Tree

## Problem Summary
Given a binary tree, determine if it is height-balanced.

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

