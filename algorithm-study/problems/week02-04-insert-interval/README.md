# {57}. {Insert Interval}

**Link:** https://leetcode.com/problems/insert-interval/  
**Difficulty:** Medium
**Topic:** Array

## Problem Summary
Insert newInterval into intervals.

## Approaches & Discussion
### Yourim
- **Coding interview**:
  Since the intervals are already sorted, we can solve this in one single pass, which gives us an O(N) time complexity. 
  I'm going to process this in three clear steps. handling intervals before the new one, merging the overlapping parts, and then finishing with the rest.
  First, I’ll iterate through the intervals that end before the newInterval starts. Since these definitely don't overlap, I’ll just add them straight to the result list.
  Now, we move to the overlapping part. As long as the current interval's start is less than or equal to the newInterval’s end, they are overlapping. 
  In this case, I'll merge them by updating the newInterval’s start to the minimum of both starts, and its end to the maximum of both ends. This way, we 'absorb' all overlapping pieces into one big interval. 
  Once that's done, I'll add this finalized newInterval to the result.
  Finally, there might be some intervals left in the list. These are all guaranteed to be after the merged interval and won't have any overlaps, so I’ll just append everything that's remaining to the result and return it.
  So, the time complexity is O(N) because we only touch each interval once, and the space complexity is also O(N) to store the output. 
  This is the most efficient way to handle the problem by using the sorted property of the input.

