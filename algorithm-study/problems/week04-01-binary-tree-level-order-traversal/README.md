# {102}. {Binary Tree Level Order Traversal}

**Link:** https://leetcode.com/problems/binary-tree-level-order-traversal/
**Difficulty:** Medium
**Topic:** Tree, Breadth-First Search, Binary Tree

## Approaches & Discussion

### Rachel

- **Problem Summary**: Return the values of a binary tree level by level, from left to right, grouped into separate arrays.
- **Plan**: I approached this problem using BFS with a queue. I'll push the root into a queue. While the queue isn't empty, I'll save the current queue length as size to know how many nodes belong to the current level. I'll iterate size times, popping each node, collecting its value, and pushing its children into the queue. After each level, I push the collected values into result.
- **Review**: Let me trace through [3,9,20,null,null,15,7]. Queue starts as [3]. First iteration: size=1, pop 3 push 9 and 20, level=[3]. Secont iteration: size=2, pop 9, no children, pop 20, push 15 and 7, level=[9, 20]. Third iteration: size=2, pop 15 and 7, no children, level=[15, 7]. Result is [[3], [9,20], [15,7]]
- **Evaluate**:
  Time complexity is O(n) since every node is visited exactly once. Space complexity is O(n) because the queue holds at most one full level of nodes, which in the worst case is n/2 nodes in ta complete binary tree
