# {102}. {Binary Tree Level Order Traversal}

**Link:** https://leetcode.com/problems/binary-tree-level-order-traversal

**Difficulty:** Medium

**Topic:** Tree, Breadth-First Search, Binary Tree

## Problem Summary
return the level order traversal of its node's value 

## Approaches & Discussion
### Angela

- **This problem is asking me to** return the level order traversal of its node's value.
- **My approach is to** use queue to traverse with BFS. Group nodes at the same level into a level array. Next, pop nodes from the queue and save to level array and if node.left or node.right exist, append to queue. Lastly return result.
- **This runs in** O(n) time complexity because this approach iterates over every node once to save level array to result array and O(n) space complexity since the result array can hold up to n nodes