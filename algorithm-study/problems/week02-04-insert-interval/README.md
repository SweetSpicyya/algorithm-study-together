# {57}. {Insert Interval}

**Link:** https://leetcode.com/problems/insert-interval/

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


