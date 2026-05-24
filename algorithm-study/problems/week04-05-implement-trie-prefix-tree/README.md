# {208}. {Implement Trie (Prefix Tree)}

**Link:** https://leetcode.com/problems/implement-trie-prefix-tree

**Difficulty:** Medium
**Topic:** Hash Table, String, Design, Trie

## Problem Summary
Implement the Trie class

## Approaches & Discussion
### Yourim
I implement a Trie by creating a TrieNode class that utilizes a dictionary to map characters to child nodes, along with a boolean flag to mark the end of a valid word.
For insert, we traverse from the root character by character, dynamically creating new nodes as needed and marking the final node's end flag as True.
For search and startsWith, we follow the character paths down the tree, immediately returning False if any character mismatch breaks the chain.
Ultimately, startsWith returns True if the path exists, whereas search strictly requires the terminal node's end flag to be set.

## Approaches & Discussion
### Angela

- **So this problem is asking me to** implement a Trie, or Prefix Tree, to efficiently store and search words.
- **I will approach this by** using a nested HashMap structure where each node contains a `children` dictionary and an `is_end_of_word` boolean flag.
- **Now, let me code this up.**
- **My approach is to** initialize the object itself as the root. Next, in the `insert` function, I'll use a pointer `curr = self` to loop through each character. If it doesn't exist in `curr.children`, I'll create a new `Trie()` object and register it, then move `curr` deeper. After the loop, change the last node's `is_end_of_word` flag to `True`.
For the `search` function, I'll trace characters using the `curr` pointer. If any character is missing, return `False`. If the loop finishes, return `curr.is_end_of_word` to check if a complete word ends there.
Lastly, `startsWith` works almost identically to `search`, but once it successfully traces the entire prefix without breaking, it just returns `True` immediately, because we don't care about the word completion.
- **This runs in** $O(L)$ time complexity for all operations ($L$ = length of the word) because we only traverse down the length of the string, and up to $O(N \times L)$ space complexity to store all unique nodes.


## Approaches & Discussion
### Rachel
- **Understand**: We need to implement a Trie data structure that supports inserting words, searching for exact words and checking if any inserted word starts with a given prefix.The key difference between search and startsWith is that search requires the full word to exist with isEnd=true, while startsWith only requires the path to exist
- **Match**:This is a classic Trie implementation problem. Each node stores a children map of next characters and an isEnd flag to mark word boundaries. I'll factor out a shared \_find helper that both search and startsWith can use, since they both need to traverse the same path.
- **Plan**: For insert, I traverse the trie character by character, creating new nodes in children when a character doesn't exist yet, and mark isEnd=true at the last character. For \_find, I traverse the path and return the final node, or null if the path doesn't exist. search uses \_find and checks that the node exists and isEnd is true. startsWith just checks that \_find doesn't return null.
- **Evaluate**:
  Insert - Time:O(m), Space:O(m) where m is the length of the word
  Search - Time: O(m), Space:O(1)
  StartsWith - Time: O(m), Space: O(1)
  Overall Space: O(n\*m) where n is the number of words and m is the average word length
