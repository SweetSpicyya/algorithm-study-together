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

Overlap the new interval into the original interval

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by trying to find the exact left and right boundaries where the newInterval should be inserted. My logic was to find the specific intervals where the overlap starts and ends, and then create a merged interval. However, this approach failed in a few cases: when the new interval engulfs the existing intervals, when it should be placed entirely at the beginning or the end, and when it fits perfectly between two existing intervals without overlapping.
- **Optimization**: To overcome the edge cases, I optimized the algotithm by adopting a single-pass linear scan approach. For left, iterate and push all intervals that end before the new interval starts. While intervals overlap with the new Interval, expand the boundaries by comparing existing ones with new interval's each end. And push the remaining intervals that start after the new interval ends.
- **Complexity Analysis**: This optimized approach gives me a time and space complexity of O(n), where n is the number of intervals in the input array.

**Difficulty:** Medium

**Topic:** Array

## Problem Summary
Insert newInterval into non-overlapping intervals.

## Approaches & Discussion
### Angela

- **So the problem is asking me to** insert newInterval into an array of non-overlapping intervals.
- **The brute force way would be to** insert newInterval and re-sort the entire array **which runs in** O(nlogn), **but this is wasteful since** the intervals are already sorted **so** re-sorting is unnecessary.
- **We can optimize this by** recognizing that intervals are already sorted, so we can find the correct position in a single pass, **reducing it to** O(n).
- **My approach is to** make new array called result, and if the newInterval's end value is less than current start value in the intervals, append newInterval to result and replace newInterval with current intervals. Also, if the newInterval's start value is greater than current's end value in the intervals, append the current value into the result. Otherwise, it would need to merge so compare the newInterval and current intervals and save the minimum value to newInterval's start value also the maximum value to newInterval's end value. Finally, out of the loop, append newInterval to result to handle the remaining cases and return the result.
- **This runs in** O(n) **time complexity because this approach** checks every interval at least once **and** O(n) **space complexity since** the result array can grow up to the length of the input


