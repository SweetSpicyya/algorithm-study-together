class Solution(object):
    def twoSum(self, nums, target):
        """    
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                index = hashMap[diff]
            
                return [index, i]
            else:
                hashMap[n] = i

        return []