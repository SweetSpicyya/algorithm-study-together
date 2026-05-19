from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        hash_magazine = defaultdict(int)
        for m in magazine:
            hash_magazine[m] += 1

        for r in ransomNote:
            if (not r in hash_magazine) or hash_magazine[r] <= 0:
                return False

            hash_magazine[r] = hash_magazine[r] - 1

        return True



ransomNote = "aa"
magazine = "aab"
s = Solution()
s.canConstruct(ransomNote, magazine)