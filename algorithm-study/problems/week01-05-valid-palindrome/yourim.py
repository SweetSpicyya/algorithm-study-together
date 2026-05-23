import math
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        formattedS = s.lower()
        formattedS = re.sub(r'[^a-zA-Z0-9]', '', formattedS)

        midIdx = math.ceil((len(formattedS)-1) / 2)

        if len(formattedS) % 2 == 0:
            leftIdx = midIdx - 1
            rightIdx = midIdx
        else:
            leftIdx = midIdx - 1
            rightIdx = midIdx + 1

        while leftIdx >= 0:
            if formattedS[leftIdx] != formattedS[rightIdx]:
                return False

            leftIdx -= 1
            rightIdx += 1

        return True

sol = Solution()
result = sol.isPalindrome("ab")

print(result)

#################

# Simple way
# 공간 복잡도가 O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l += 1

            elif not s[r].isalnum():
                r -= 1

            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1

        return True

#################

# Faster way
# O(n) -> 전제 string을 탐색하며 새로운 문자열을 만들기 때문

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = "".join(char for char in s if char.isalnum()).lower()
        return s == s[::-1]