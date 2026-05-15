# {133}. {Clone Graph}

**Link:** https://leetcode.com/problems/clone-graph/description/

**Difficulty:** Medium

**Topic:** Hash Table, Depth-First Search, Breadth-First Search, Graph Theory

## Problem Summary
return a deep copy(clone) of the given graph of a connected undirected graph

## Approaches & Discussion
### Angela

- **This problem is asking me to** make a deep clone graph of a connected undirected graph.
- **My approach is to** make hashmap called visited and dfs function to call recursively. If the node is None, return None or if the node already visited, return the cloned node stored in visited. Otherwise, create a new node with the same value and save to visited hashmap and iterate over neighbors of node by calling dfs recursively. Lastly return a deep clone graph.
- **This runs in** O(V+E) time complexity because this approach iterates over every vertex and edge once and O(V) space complexity since a deep clone graph can hold up to n nodes.