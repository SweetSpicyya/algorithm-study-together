# {409}. {Longest Palindrome}

**Link:** https://leetcode.com/problems/longest-palindrome/
<<<<<<< HEAD
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

## Approaches & Discussion
### Angela

- **So this problem is asking me to** find the length of the longest palindrome that can be built with given letters.
- **The brute force way would be** to check all possible combinations using loop, which runs in O(n!) time complexity.
- **We can optimize this by** using Hash Map, which reduces the time complexity to O(n).
- **I will approach this by** using Hash Map to store the number of each characters in the s. Now, let me code this up.
- **My approach is to** initialize a Hash Map called count and iterate over the s, count the number of characters. Next, if the number of character is even in the Hash Map, add all to the length otherwise, add to the length after decrement -1 also, if the odd exists in the Hash Map, it means we can use only one character to the center of the palindrome so increment the length. Lastly, return the final length.
- **This runs in** O(n) time complexity because thanks to the count map, we visit each characters from the s at most once and O(n) space complexity since the count map can hold up to the number of unique characters in the input string.