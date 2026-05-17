# {133}. {Clone Graph}

**Link:** https://leetcode.com/problems/clone-graph

**Difficulty:** Medium
**Topic:** Hash Table, Depth-First Search, Breadth-First Search, Graph Theory

## Problem Summary
Return a deep copy (clone) of the graph.

## Approaches & Discussion
### Yourim
This problem requires making a deep copy while properly handling potential cycles. 
I would solve this by using DFS (or BFS) to traverse the graph, combined with a hash map to map each [original node] to its [cloned node]. 
This hash map acts as a visited set to prevent infinite loops, allowing us to clone all nodes and edges efficiently in $O(V + E)$ time and space complexity.