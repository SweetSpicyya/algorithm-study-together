# {56}. {Merge Intervals}

**Link:** https://leetcode.com/problems/merge-intervals/
**Difficulty:** Medium
**Topic:** Array, Sorting

## Approaches & Discussion

### Rachel

- **Understand**: We're given an array of intervals and need to merge all overlapping intervals into a non-overlapping set that covers the same ranges.
- **Match**: This is a classic sorting+greedy merge problem. By sorting intervals by their start value, any overlap can only happen between adjacent intervals in the sorted order.
- **Plan**: First I sort intervals by start value. I initialize result with the first interval. Then for each subsequent interval, I compare its start to the end of the last interval in result. If curr[0] <= last[1], they overlap, so I extend last[1] to Math.max(last[1], curr[1]). Otherwise, I push curr as a new seperate interval Using <= instead of < is important because intervals like[1,3] and [3,5] touch at the boundary and should still merge into [1,5].
- **Evaluate**:
  Time: O(n log n) - dominated by sorting; the merge pass itself is O(n)
  Space: O(n) - result array, plus O(log n) or O(n) for sort depending on implementation
