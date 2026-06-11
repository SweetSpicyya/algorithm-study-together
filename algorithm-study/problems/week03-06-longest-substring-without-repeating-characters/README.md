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

## Approaches & Discussion
### Yourim

naive approach is we use two loops. The outer loop picks a starting point, and the inner loop keeps extending the substring character by character. 
Every time we hit a duplicate, we record the length of what we built so far and break out. We do this for every possible starting position and return the max.
Time complexity is O(N²). For each of the N starting points we're potentially scanning the whole string again.
Instead of restarting from scratch every time we hit a duplicate, we can just slide the window forward. 
We keep a start pointer and an end pointer, and we expand end one step at a time. When we hit a character that's already inside the window, we jump start right past the previous occurrence of that character.
And the way we track positions is with a hash map. we store each character's most recent index. So when we see a duplicate, we know exactly where to move start.
when we find a duplicate, we only move start if the previous occurrence is actually inside the current window. 
Otherwise we might move start backwards which would break everything.
At every step we compute the current window length as end - start + 1 and update the max.
Time complexity is O(N). We move end through the string once. 
Space is O(1). The map holds at most 26 keys for lowercase letters.