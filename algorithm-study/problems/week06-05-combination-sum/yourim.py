class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def tracking(remain, start, path) -> List(List[int]):
            if remain == 0:
                return ans.append(list(path))

            if remain < 0:
                return False

            for i in range(start, len(candidates)):
                path.append(candidates[i])

                tracking(remain-candidates[i], i, path)
                path.pop()

        tracking(target, 0, [])
        return ans

