# {235}. {Lowest Common Ancestor of a Binary Search Tree}

**Link:** https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
**Difficulty:** Medium
**Topic:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

## Problem Summary

Find the lowest common ancestor node of two given nodes in Binary Search Tree

## Approaches & Discussion

### Rachel

- **Clarification & Constraints**: Ask Constraints like
  What is the expected size of the input?(Scale),
  Are there any constraints on the values?(Data Range),
  Can the node values be negative or duplicates?(Data type),
  Should I conseder cases where p or q might not exist in the tree?(Edge Cases)
- **Brute-force / Initial Approach**: My initial approach would be visually reconstructing the tree but I noticed this might lead to unnecessaty space complexity.
- **Optimization**: To optimize this, I can leverage the BST property. Since p and q must eventually diverge, the LCA is simply the first split point.
- **Complexity Analysis**: This optimized approach gives me a time complexity of O(h), where h is the height of the tree

Find the lowest common ancestor(LCA) node of two given nodes in the BST.

## Approaches & Discussion
### Angela

- **Understand** : So the problem is asking me to find the lowest common ancestor node of two given nodes in the BST.  
- **Brute force** : The brute force way would be to traverse and save each LCA node of entire nodes. Compare LCA nodes of p and q and find the same LCA node which runs in O(n^2). 
- **Better way**: We can optimize this by using DFS which runs in O(logn) in the best or O(n) in the worst case. 
- **Approach**: My approach is to make inner function called 'dfs' by using DFS and initialize the 'current' variable to root node to traverse the tree. In the 'dfs' function, if 'p' and 'q' are smaller than 'current', 'current' moves to the left and return 'dfs' function recursively. Otherwise, if 'p' and 'q' are bigger than 'current', 'current' moves to the right and return 'dfs' function as well. Lastly, 'p' and 'q' are neither smaller nor bigger than 'current', the LCA node is 'current'. 
- **Complexity** : This runs in O(logn) time complexity in the best case or O(n) in the worst case because this approach will traverse and divide every level of the tree and overall O(logn) space complexity since call stack grows up to O(logn) due to recursive calls.

