# {383}. {Ransom Note}

**Link:** https://leetcode.com/problems/ransom-note/description/

**Difficulty:** Easy

**Topic:** Hash Table, String, Counting

## Problem Summary
Determine whether the ransomNote is contructed by using the letters from magazine once

## Approaches & Discussion
### Angela

- **This problem is asking me to** determine whether the ransomNote is constructed by using the letters from magazine once.
- **The brute force could be to** iterate all letter from the both strings and compare if the letter is included in the other which runs in O(n^2) but it's wasteful since we don't need to repeatedly scan the same characters
- **We can optimize this by** using hashmap, reducing it to O(n)
- **My approach is to make** hashmap called dic and save letter in magazine as a key and the count as a value. If letter in ransomNote is included in dic and dic[letter] is greater than 0, decrement the count value otherwise return False.
- **This runs in** O(n) time complexity because this approach iterates over every letter in both strings and O(n) space complexity since the hashmap can hold at most 26 unique characters