from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        for i in range(1, n):
            ans[i] = ans[i -1] * nums[i-1]

        p=1
        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * p
            p = p * nums[i]


        return ans


sol = Solution()
nums1 = [1,2,3,4]
sol.productExceptSelf(nums1)

