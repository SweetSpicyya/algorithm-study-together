from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        temp_max = nums[0]

        for n in nums[1:]:
            temp_max = max(n, temp_max+n)

            max_sum = max(temp_max, max_sum)

        return max_sum
