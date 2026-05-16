# {102}. {Binary Tree Level Order Traversal}

**Link:** https://leetcode.com/problems/binary-tree-level-order-traversal

**Difficulty:** Medium
**Topic:** Tree, Breadth-First Search, Binary Tree

## Problem Summary

Return the level order traversal of its nodes' values.


## Approaches & Discussion
### Yourim

Okay so... we've got a binary tree and we want to return the values level by level.
The brute force way I can think of is doing a full DFS — like a recursive preorder traversal — and tracking the depth of each node, then grouping them by depth into a hashmap. It works, but it's a bit clunky because you're doing extra bookkeeping to reconstruct the level order after the fact. The depth tracking adds overhead and the code isn't that clean.
So the more natural approach here is BFS, not DFS — because BFS expands outward layer by layer, which is exactly the shape of what we want. The level grouping comes for free.
First, I'm adding a guard clause to handle the empty tree case — if root is null, just return an empty list immediately.
Then I enqueue the root and loop until the queue is empty. On each iteration, I pop a node from the front of the queue, grab its value, and if it has a left or right child, I enqueue those too. Then I append the value to the current level's array and add that to the result.
But if I stop here, this won't actually return the output level by level — because right now I'm just appending each node one by one into the result. Everything ends up flat. There's no boundary between levels.
So I need a way to know when one level ends and the next begins. And the key insight is — right before I start processing a level, the queue contains exactly the nodes of that level and nothing else. So if I snapshot len(queue) at that moment, that count tells me exactly how many nodes belong to this level. Then I iterate that many times, collect those values, and anything I enqueue during that loop automatically belongs to the next level.
Now we're capturing nodes level by level.
For complexity — time is O(n) where n is the number of nodes, since we visit every node exactly once. Space is also O(n) because at peak the queue holds all the nodes at the widest level, which in the worst case is n/2 — still O(n).


## Approaches & Discussion
### Angela

- **This problem is asking me to** return the level order traversal of its node's value.
- **My approach is to** use queue to traverse with BFS. Group nodes at the same level into a level array. Next, pop nodes from the queue and save to level array and if node.left or node.right exist, append to queue. Lastly return result.
- **This runs in** O(n) time complexity because this approach iterates over every node once to save level array to result array and O(n) space complexity since the result array can hold up to n nodes