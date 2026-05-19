# {133}. {Clone Graph}

**Link:** https://leetcode.com/problems/clone-graph/
**Difficulty:** Medium
**Topic:** Hash Table, Depth-First Search, Breadth-First Search, Graph Theory

## Approaches & Discussion

### Rachel

- **Problem Summary**: Return a deep copy of a node in a connected undirected graph.
- **Plan**: I'll use a hashmap where the key is the original node and the value is its clone. Before creating a new clone, I check if the node already exists in the map. If it does, I return the existing clone immediately to prevent infinite recursion. Otherwise, I create a new node, store it in the map right away, then recursively clone each neighbor and push them into the clone's neighbors list.
- **Evaluate**: Time complexity is O(n) since every node and edge is visited exactly once. Space complexity is O(n) because the map stores one entry per node, and the recursion call stack goes as deep as the number of nodes in the worst case.
