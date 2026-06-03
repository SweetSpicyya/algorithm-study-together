# {98}. {Validate Binary Search Tree}

**Link:** https://leetcode.com/problems/validate-binary-search-tree
**Difficulty:** Medium
**Topic:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

## Approaches & Discussion
### Yourim
Goal: I'll explain how to validate a Binary Search Tree (BST), which can be solved by checking node values within valid ranges either recursively or using in-order traversal.
The Flaw: Checking only immediate children (local subtree) is insufficient. A valid BST requires all nodes in the left subtree to be smaller than the root, and all nodes in the right subtree to be larger (global constraint).
Recursive Idea: The optimal approach uses a helper function that passes down a dynamic range (min_val and max_val) to ensure every node satisfies the global BST properties.
Recursive Steps: For each node, we check if its value falls outside the (min_val, max_val) range. If valid, we recursively check the left child with an updated max_val (current node's value) and the right child with an updated min_val (current node's value).
Complexity: The approach takes O(N) time because it visits every node exactly once, and O(H) space (where H is the tree height) for the recursive call stack.