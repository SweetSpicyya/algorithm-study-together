class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return

        intervals = sorted(intervals)
        ans = []

        for i in intervals:
            if not ans or i[0] > ans[-1][1]:
                ans.append(i)
            else:
                ans[-1][1] = max(ans[-1][1], i[1])

        return ans