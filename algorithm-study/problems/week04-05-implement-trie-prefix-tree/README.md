# {208}. {Implement Trie (Prefix Tree)}

**Link:** https://leetcode.com/problems/implement-trie-prefix-tree/description/

**Difficulty:** Medium

**Topic:** Hash Table, String, Design, Trie

## Problem Summary
Implement the Trie class

## Approaches & Discussion
### Angela

- **So this problem is asking me to** implement a Trie, or Prefix Tree, to efficiently store and search words.
- **I will approach this by** using a nested HashMap structure where each node contains a `children` dictionary and an `is_end_of_word` boolean flag.
- **Now, let me code this up.**
- **My approach is to** initialize the object itself as the root. Next, in the `insert` function, I'll use a pointer `curr = self` to loop through each character. If it doesn't exist in `curr.children`, I'll create a new `Trie()` object and register it, then move `curr` deeper. After the loop, change the last node's `is_end_of_word` flag to `True`.
For the `search` function, I'll trace characters using the `curr` pointer. If any character is missing, return `False`. If the loop finishes, return `curr.is_end_of_word` to check if a complete word ends there.
Lastly, `startsWith` works almost identically to `search`, but once it successfully traces the entire prefix without breaking, it just returns `True` immediately, because we don't care about the word completion.
- **This runs in** $O(L)$ time complexity for all operations ($L$ = length of the word) because we only traverse down the length of the string, and up to $O(N \times L)$ space complexity to store all unique nodes.