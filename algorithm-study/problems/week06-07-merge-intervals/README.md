# {56}. {Merge Intervals}

**Link:** https://leetcode.com/problems/merge-intervals
**Difficulty:** Medium
**Topic:** Array, Sorting

## Problem Summary
Merge all overlapping intervals in the given array, and return an array.

## Approaches & Discussion
### Yourim
First, I sort the intervals by their start times to ensure we can process them sequentially.
We initialize an empty list called ans to store the final merged intervals.
We iterate through each interval, checking if it overlaps with the last interval added to ans.
If they don't overlap, we simply append the current interval to ans.
If they do overlap, we update the end time of the last interval in ans to the maximum of the two end times to effectively merge them.

## Approaches & Discussion
### Rachel
- **Understand**: We're given an array of intervals and need to merge all overlapping intervals into a non-overlapping set that covers the same ranges.
- **Match**: This is a classic sorting+greedy merge problem. By sorting intervals by their start value, any overlap can only happen between adjacent intervals in the sorted order.
- **Plan**: First I sort intervals by start value. I initialize result with the first interval. Then for each subsequent interval, I compare its start to the end of the last interval in result. If curr[0] <= last[1], they overlap, so I extend last[1] to Math.max(last[1], curr[1]). Otherwise, I push curr as a new seperate interval Using <= instead of < is important because intervals like[1,3] and [3,5] touch at the boundary and should still merge into [1,5].
- **Evaluate**:
  Time: O(n log n) - dominated by sorting; the merge pass itself is O(n)
  Space: O(n) - result array, plus O(log n) or O(n) for sort depending on implementation

## Approaches & Discussion
### Angela

- So, this problem is asking me to merge overlapping intervals.
- To solve this easily, I will sort the array first. Let me code this up.
- First, I will sort the `intervals` by their start times. Then, I will create an `output` array. I also set `curr_start` and `curr_end` to the very first interval. Next, I will loop through the rest of the intervals. For each interval, I check if the new start time is less than or equal to the `curr_end`. If it is, it means they overlap. So, I update `curr_end` using the `max` function to merge them. If they don't overlap, I simply append the current interval to the `output` array, and update my pointers to the new interval. After the loop, I must remember to append the last leftover interval. Finally, I return the output.
- This runs in **$O(N \log N)$ time complexity** because the sorting step takes the most time. The space complexity is **$O(N)$** because we need extra space for the output array.
