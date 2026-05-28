# {409}. {Longest Palindrome}

**Link:** https://leetcode.com/problems/longest-palindrome/
**Difficulty:** Easy
**Topic:** Junior, Hash Table, String, Greedy

## Approaches & Discussion

### Rachel

- **Understand**: We're given a string and need to find the length of the longest palindrome we can build using those characters. The key insight is that a palindrome can use any character that appears an even number of times, and at most one character that appears an odd number of times.
- **Match**: This is a frequency counting problem. I'll use a hashmap to count how many times each character appears, then calculate how many characters can be used in a palindrome.
- **Plan**: I'll build a frequency map for each character. Then iterate through the map. If any character has an odd count, I set flag and add 1 at the end for the middle character.
- **Evaluate**:
  Time: O(n) - one pass to build the map, one pass through the map.
  Space: O(n) - map stores at most 52 entries constant regardless of input size.
