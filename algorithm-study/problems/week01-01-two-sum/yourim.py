class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = [];
        for (i, n) in enumerate(nums):
            left = target - n

            if left in nums[i+1:]:
                left_index = nums.index(left, i+1)

                indices.append(i)
                indices.append(left_index)

                return indices

        return []

##################################################

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for (idx, val) in nums:
            diff = target - val

            if diff in hashMap:
                return [hashMap[diff], idx]

            hashMap[val] = idx