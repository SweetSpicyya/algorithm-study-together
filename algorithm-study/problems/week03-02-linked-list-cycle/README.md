# {141}. {Linked List Cycle}

**Link:** https://leetcode.com/problems/linked-list-cycle/
**Difficulty:** Easy
**Topic:** Hash Table, Linked List, Two Pointers

## Problem Summary
Search if there is a cycle in a linked list.

## Approaches & Discussion
### Yourim
- **Coding interview**:
<details>
  <summary>Click to view details </summary>
This problem asks to detect whether a linked list contains a cycle.
My first approach is using a HashSet. The idea is simple. if we ever visit a node we've already seen, there's a cycle. 
I traverse the list and at each node, check if it's already in the set. If it is, return True. If we reach null, return False. 
Time complexity is O(n), space is O(n) since we're storing every node reference.
That works, but we can do better on space. That leads me to Floyd's Cycle Detection.
The insight is if a cycle exists, a fast pointer moving twice as fast as a slow pointer will eventually meet it. 
I start both at head, slow moves one step, fast moves two. If they ever point to the same node, there's a cycle. If fast falls off the end, there isn't.
Time complexity stays O(n), but space drops to O(1), just two pointers, nothing extra.
In an interview I'd always present the HashSet solution first to establish correctness, then optimize with Floyd's. 
That brute force to optimal progression is exactly what interviewers want to see. And a common follow-up, Floyd's can also be extended to find the exact node where the cycle begins.
</details>

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by traversing the linked list and storing each visited node in a Set. At each step, I check if the current node already exists in the Set.
- **Optimization**: Instead of using a Set to track visited nodes, I applied Floyd's Cycle Detection algorithm using two pointers. If a cycle exists, fast pointer will eventually lap slow pointer and they will meet at the same node. If there is no cycle, fast will reach null first.
- **Complexity Analysis**: Time: O(n), Space: O(n) - Each node visited once, but all nodes stored in a Set.

## Approaches & Discussion
### Angela

- **This problem is asking me to** determine if the given head which is linked list has a cycle in it.
- **The brute force could be to** traverse and compare every node which runs in O(n^2) but it's wasteful since we could traverse every node once.
- **We can optimize this by** using hash map which runs in O(n).
- **My approach is to** make hash map to check whether if the node already visited before. Before traverse the nodes, if the head is None, return False. While traversing the head, if the current node is already in the visited hashmap return True, otherwise save it as key and True as value to visited and move to next node.
- **This runs in** O(n) time complexity because this approach traverses every node in the linkedlist and O(n) space complexity since the hashmap can hold up to n nodes
  
