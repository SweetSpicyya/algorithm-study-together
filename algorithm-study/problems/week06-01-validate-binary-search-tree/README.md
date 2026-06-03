# {98}. {Validate Binary Search Tree}

**Link:** https://leetcode.com/problems/validate-binary-search-tree/

**Difficulty:** Medium

**Topic:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

## Problem Summary
determine whether the given tree is a valid Binary Search Tree

## Approaches & Discussion
### Angela

- So, this problem is asking me to determine whether the given tree is a valid Binary Search Tree. Since we need to visit all nodes in the tree at least once, an **O(N) time complexity** solution is already optimal.
- I will approach this by using Depth-First Search (DFS). Let me code this up.
- My approach is to make a helper `dfs` function that takes a node along with its allowed `min_val` and `max_val`. Initially, I will pass negative infinity and positive infinity.
- In this function, **if the node is null, I will return `True`** because an empty tree doesn't break any BST rules. Next, I check if the current node's value is **within the allowed bounds**. If the current node's value is out of bounds, I return `False`. After checking the current node, I **recursively validate the left and right subtrees**, updating the `max_val` and `min_val` accordingly.
- This runs in **O(N) time complexity** because this approach traverses every node at most once. The **space complexity is O(N)** in the worst case due to the recursion call stack if the tree is completely unbalanced.