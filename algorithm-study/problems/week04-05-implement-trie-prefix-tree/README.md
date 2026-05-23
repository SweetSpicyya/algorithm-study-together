# {208}. {Implement Trie (Prefix Tree)}

**Link:** https://leetcode.com/problems/implement-trie-prefix-tree/
**Difficulty:** Medium
**Topic:** Hash Table, String, Design, Trie

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
