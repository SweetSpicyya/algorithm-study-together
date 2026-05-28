# {409}. {Longest Palindrome}

**Link:** https://leetcode.com/problems/longest-palindrome/

**Difficulty:** Easy

**Topic:** 

## Problem Summary
find the length of the longest palindrome that can be built with given letters.

## Approaches & Discussion
### Angela

- **So this problem is asking me to** find the length of the longest palindrome that can be built with given letters.
- **The brute force way would be** to check all possible combinations using loop, which runs in O(n!) time complexity.
- **We can optimize this by** using Hash Map, which reduces the time complexity to O(n).
- **I will approach this by** using Hash Map to store the number of each characters in the s. Now, let me code this up.
- **My approach is to** initialize a Hash Map called count and iterate over the s, count the number of characters. Next, if the number of character is even in the Hash Map, add all to the length otherwise, add to the length after decrement -1 also, if the odd exists in the Hash Map, it means we can use only one character to the center of the palindrome so increment the length. Lastly, return the final length.
- **This runs in** O(n) time complexity because thanks to the count map, we visit each characters from the s at most once and O(n) space complexity since the count map can hold up to the number of unique characters in the input string.