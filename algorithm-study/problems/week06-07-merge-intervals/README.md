# {56}. {Merge Intervals}

**Link:** https://leetcode.com/problems/merge-intervals/description/

**Difficulty:** Medium

**Topic:** Array, Sorting

## Problem Summary
to merge overlapping intervals.

## Approaches & Discussion
### Angela

- So, this problem is asking me to merge overlapping intervals.
- To solve this easily, I will sort the array first. Let me code this up.
- First, I will sort the `intervals` by their start times. Then, I will create an `output` array. I also set `curr_start` and `curr_end` to the very first interval. Next, I will loop through the rest of the intervals. For each interval, I check if the new start time is less than or equal to the `curr_end`. If it is, it means they overlap. So, I update `curr_end` using the `max` function to merge them. If they don't overlap, I simply append the current interval to the `output` array, and update my pointers to the new interval. After the loop, I must remember to append the last leftover interval. Finally, I return the output.
- This runs in **$O(N \log N)$ time complexity** because the sorting step takes the most time. The space complexity is **$O(N)$** because we need extra space for the output array.