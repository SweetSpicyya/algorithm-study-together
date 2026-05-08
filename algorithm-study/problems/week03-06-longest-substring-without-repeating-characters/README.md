# {3}. {Longest Substring Without Repeating Characters}

**Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters
**Difficulty:** Medium
**Topic:** Staff, Hash Table, String, Sliding Window

## Problem Summary

Find the length of the longest substiring without duplicate charaters, given a string

## Approaches & Discussion

### Rachel

- **Optimization**: I approached this problem using a sliding window with two pointers and a hashmap. As a end pointer moves through the string, I store each character's most recent index in the map. When a duplicate is detected, I slide a start pointer to one position after the duplicate's previous position. At each step, I update max by comparing the current window size with the previous maximum.
- **Complexity Analysis**:
  Time: O(n) - each character is visited once as end moves through the string
  Space: O(1) - the map stores at most 26 lowercase letters, so the size is constant regardless of input


## Approaches & Discussion
### Angela

- **This problem is asking me to** find the length of the longest substring without duplicate characters from a string s.
- **The brute force could be to** iterate over all possible substrings which runs in O(n^2) but it's wasteful because we can avoid rechecking characters we've already seen.
- **We can optimize this by** using two pointers and hashmap which runs in O(n).
- **My approach is to** make two pointers to calculate the length of the substring called left,right and hashmap to store index of the letter in s called visited. While iterating over s, if the current character is not in visited, save to visited letter as a key and index as a value and increment the right pointer otherwise compare current left to value from the visited +1 and value+1 is greater than left pointer, move the left pointer to visited[character]+1, increment the right pointer and update the index in visited. Lastly, continuously update the maximum length using the max function
- **This runs in** O(n) time complexity because this approach iterates over characters once and O(n) space complexity since the hashmap can hold up to 26 unique characters.
