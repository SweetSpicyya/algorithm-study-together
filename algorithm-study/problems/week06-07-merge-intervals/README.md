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