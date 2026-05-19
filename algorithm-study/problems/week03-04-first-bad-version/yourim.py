class Solution:
    def isBadVersion(version: int) -> bool:

    def firstBadVersion_nav(self, n: int) -> int:

        for i in range(1, n+1):
            if self.isBadVersion(i): return i


    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n

        while left < right:
            mid = left + (right-left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left