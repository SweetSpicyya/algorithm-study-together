# {208}. {Implement Trie (Prefix Tree)}

**Link:** https://leetcode.com/problems/implement-trie-prefix-tree

**Difficulty:** Medium
**Topic:** Hash Table, String, Design, Trie

## Problem Summary
string insertion, exact word searching, and prefix matching operations.

## Approaches & Discussion
### Yourim
I implement a Trie by creating a TrieNode class that utilizes a dictionary to map characters to child nodes, along with a boolean flag to mark the end of a valid word. 
For insert, we traverse from the root character by character, dynamically creating new nodes as needed and marking the final node's end flag as True. 
For search and startsWith, we follow the character paths down the tree, immediately returning False if any character mismatch breaks the chain. 
Ultimately, startsWith returns True if the path exists, whereas search strictly requires the terminal node's end flag to be set.