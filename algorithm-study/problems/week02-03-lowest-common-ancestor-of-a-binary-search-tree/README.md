# {235}. {Lowest Common Ancestor of a Binary Search Tree}

**Link:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
**Difficulty:** Medium
**Topic:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

## Problem Summary

Find the lowest common ancestor node of two given nodes in Binary Search Tree

## Approaches & Discussion

### Yourim
Since it's a Binary Search Tree, we know exactly where nodes are based on their values relative to the root.
I start at the root and compare its value with our two target nodes, p and q. 
First, if both p and q are greater than the current node, it means they’re both tucked away in the right subtree. So, I’ll just move my pointer to the right and keep looking.
Second, if they’re both smaller, they must be in the left subtree, so I’ll move to the left.
The third case is the most important—the split point. If one node is smaller and the other is larger, or if the current node is actually equal to one of them, then we've found our LCA. 
This is because any further down we go, we'd lose the connection to one of the nodes.
Efficiency-wise, this is great. The time complexity is O(h), where h is the height of the tree, because we're just moving down a single path. 
And if I implement this iteratively, the space complexity is a solid O(1) since I'm not using any extra data structures or recursion.
