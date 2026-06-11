class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        visited = [False] * len(nums)

        def backtrack(curr_permutation):
            if len(curr_permutation) == len(nums):
                result.append(curr_permutation[:])
                return

            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    curr_permutation.append(nums[i])

                    backtrack(curr_permutation)

                    curr_permutation.pop()
                    visited[i] = False

        backtrack([])
        return result
