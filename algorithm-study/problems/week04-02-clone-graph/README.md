# {133}. {Clone Graph}

**Link:** https://leetcode.com/problems/clone-graph

**Difficulty:** Medium
**Topic:** Hash Table, Depth-First Search, Breadth-First Search, Graph Theory

## Problem Summary
return a deep copy(clone) of the given graph of a connected undirected graph

## Approaches & Discussion
### Yourim
This problem requires making a deep copy while properly handling potential cycles. 
I would solve this by using DFS (or BFS) to traverse the graph, combined with a hash map to map each [original node] to its [cloned node]. 
This hash map acts as a visited set to prevent infinite loops, allowing us to clone all nodes and edges efficiently in $O(V + E)$ time and space complexity.

## Approaches & Discussion
### Angela

- **This problem is asking me to** make a deep clone graph of a connected undirected graph.
- **My approach is to** make hashmap called visited and dfs function to call recursively. If the node is None, return None or if the node already visited, return the cloned node stored in visited. Otherwise, create a new node with the same value and save to visited hashmap and iterate over neighbors of node by calling dfs recursively. Lastly return a deep clone graph.
- **This runs in** O(V+E) time complexity because this approach iterates over every vertex and edge once and O(V) space complexity since a deep clone graph can hold up to n nodes.


## Approaches & Discussion
### Rachel
- **Problem Summary**: Return a deep copy of a node in a connected undirected graph.
- **Plan**: I'll use a hashmap where the key is the original node and the value is its clone. Before creating a new clone, I check if the node already exists in the map. If it does, I return the existing clone immediately to prevent infinite recursion. Otherwise, I create a new node, store it in the map right away, then recursively clone each neighbor and push them into the clone's neighbors list.
- **Evaluate**: Time complexity is O(n) since every node and edge is visited exactly once. Space complexity is O(n) because the map stores one entry per node, and the recursion call stack goes as deep as the number of nodes in the worst case.
