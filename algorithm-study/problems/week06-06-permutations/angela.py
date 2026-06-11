class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        tmp_array=[]
        output=[]

        def backtracking(nums):
            if len(tmp_array)==len(nums):
                output.append(tmp_array[:])
                return

            for now in nums:
                if now in tmp_array:
                    continue
                    
                tmp_array.append(now)
                backtracking(nums)
                tmp_array.pop()
            
        backtracking(nums)
        return output