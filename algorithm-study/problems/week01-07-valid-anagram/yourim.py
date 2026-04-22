class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_map = {}
        for char in s:
            if char in anagram_map:
                anagram_map[char] = anagram_map[char]+1
            else:
                anagram_map[char] = 1

        for char in t:
            if char in anagram_map:
                anagram_map[char] = anagram_map[char]-1
            else:
                return False

        return all(val==0 for val in anagram_map.values())


###########
## better way

def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    freq = {}

    for char in s:
        freq[char] = freq.get(char, 0) + 1

    for char in t:
        if char not in freq:
            return False
        freq[char] -= 1

    return all(v == 0 for v in freq.values())