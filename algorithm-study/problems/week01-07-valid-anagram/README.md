# {242}. {Valid Anagram}

**Link:** https://leetcode.com/problems/valid-anagram/
**Difficulty:** Easy
**Topic:** Hash Table, String, Sorting

## Problem Summary

Determine whether t is an anagram of s

## Approaches & Discussion

### Yourim
Okay, so I'll start by clarifying the problem.
I'm given two strings, s and t, and I need to determine whether t is an anagram of s, 
meaning they contain exactly the same characters with the same frequencies.

My approach is to use a HashMap.
First, I iterate through s and build a frequency map, each character as a key, and its count as the value.
Then I iterate through t. For each character, I check if it exists in the map. If it doesn't exist,
meaning t has a character that s doesn't have at all — I can immediately return False, because that already violates the anagram condition.
If it does exist, I decrement the count.
Finally, I check if all values in the map are zero. If yes, return True. Otherwise, False.

<details>
"Let me code this up now."
"First, an early exit — if the lengths are different, they can't be anagrams. 
No point going further."
```python
if len(s) != len(t):
    return False
```
"Now I'll build the frequency map by iterating through s. 
I'm using dict.get() here with a default of zero, so I don't need to check if the key exists first."
```python
freq = {}

for char in s:
freq[char] = freq.get(char, 0) + 1
```
"Next, I iterate through t. Here's the key part. 
if I see a character that's not in my map at all, I return False immediately. 
That means t has something s never had, so it can't be a valid anagram."
```python
for char in t:
    if char not in freq:
        return False
    freq[char] -= 1
```

"Finally, I verify that every count in the map has been fully cancelled out, all values should be zero."
```python
return all(v == 0 for v in freq.values())
```
</details>


### Rachel
- **My way**: I thought about comparing unique characters using Set, but I realized that character frequency matters. It the string contains repetitive characters, Set won't work.
- **Better way**: Use a Hash Map with characters as keys and their frequencies as values. After populating the map with string s, iterate through string t and substract the count of each character one by one to verify the anagram.
