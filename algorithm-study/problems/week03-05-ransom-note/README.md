# {383}. {Ransom Note}

**Link:** https://leetcode.com/problems/ransom-note
**Difficulty:** Easy
**Topic:** Hash Table, String, Counting

## Problem Summary

Determine whether a given string can be constructed by using the letters from the other given string

## Approaches & Discussion

### Yourim
The problem is given a ransom note string and a magazine string, we want to check if we can construct the ransom note using letters from the magazine. 
Each letter in the magazine can only be used once.

we just need to know if the magazine has enough of each letter. And a hash map is the natural fit for tracking letter counts.
First, quick sanity check, if the ransom note is longer than the magazine, we can just return false immediately. 
There's no way we have enough letters.
Then we build a frequency map of the magazine. For each letter in the ransom note, we check two things.
Does this letter exist in the map, and is the count still above zero. If either fails, we return false. 
Otherwise we decrement the count and keep going.
Time complexity is O(N + M). We iterate through the magazine once to build the map, then through the ransom note once to check. 
Space is O(1). I guess technically the map holds at most 26 keys since we're only dealing with lowercase letters, so it's constant space.
