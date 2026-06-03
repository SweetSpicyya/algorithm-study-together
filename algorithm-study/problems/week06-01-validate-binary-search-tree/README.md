# {98}. {Validate Binary Search Tree}


**Link:** https://leetcode.com/problems/validate-binary-search-tree
**Difficulty:** Medium
**Topic:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

## Problem Summary
determine whether the given tree is a valid Binary Search Tree

## Approaches & Discussion
### Yourim
Goal: I'll explain how to validate a Binary Search Tree (BST), which can be solved by checking node values within valid ranges either recursively or using in-order traversal.
The Flaw: Checking only immediate children (local subtree) is insufficient. A valid BST requires all nodes in the left subtree to be smaller than the root, and all nodes in the right subtree to be larger (global constraint).
Recursive Idea: The optimal approach uses a helper function that passes down a dynamic range (min_val and max_val) to ensure every node satisfies the global BST properties.
Recursive Steps: For each node, we check if its value falls outside the (min_val, max_val) range. If valid, we recursively check the left child with an updated max_val (current node's value) and the right child with an updated min_val (current node's value).
Complexity: The approach takes O(N) time because it visits every node exactly once, and O(H) space (where H is the tree height) for the recursive call stack.

## Approaches & Discussion
### Angela

- So, this problem is asking me to determine whether the given tree is a valid Binary Search Tree. Since we need to visit all nodes in the tree at least once, an **O(N) time complexity** solution is already optimal.
- I will approach this by using Depth-First Search (DFS). Let me code this up.
- My approach is to make a helper `dfs` function that takes a node along with its allowed `min_val` and `max_val`. Initially, I will pass negative infinity and positive infinity.
- In this function, **if the node is null, I will return `True`** because an empty tree doesn't break any BST rules. Next, I check if the current node's value is **within the allowed bounds**. If the current node's value is out of bounds, I return `False`. After checking the current node, I **recursively validate the left and right subtrees**, updating the `max_val` and `min_val` accordingly.
- This runs in **O(N) time complexity** because this approach traverses every node at most once. The **space complexity is O(N)** in the worst case due to the recursion call stack if the tree is completely unbalanced.
