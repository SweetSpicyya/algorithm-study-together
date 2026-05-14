# {15}. {3Sum}

**Link:** https://leetcode.com/problems/3sum/
**Difficulty:** Medium
**Topic:** Array, Two Pointers, Sorting

## Problem Summary

Return the level order traversal of its nodes' values.

## Approaches & Discussion

## Approaches & Discussion
### Yourim
The first thing we do is sort the array. 
Sorting gives us two big advantages: it lets us apply the two-pointer technique, and it makes duplicate skipping trivial since identical values end up adjacent.

Breaking down the logic, step by step.
First, early termination. Since the array is sorted, if the smallest element. which is nums[i] at the front is already greater than zero, there's no way any triplet can sum to zero. We break immediately.
Second, outer loop deduplication. If the current anchor value is the same as the previous one, we skip it. This prevents us from recording the same triplet twice when there are duplicate values in the array.
Third, the two-pointer squeeze. We set left just after i, and right at the end of the array. We calculate the total of all three. If it's too small, we move left up. If it's too big, we move right down. If it hits zero, we record the triplet.
Fourth, inner deduplication, this is the subtle part. After recording a valid triplet, we skip over any duplicate values on both sides before advancing the pointers. Without this, we'd end up recording the same triplet multiple times with different index combinations.
Time is O(n²) — O(n log n) for the sort, plus O(n²) for the two-pointer pass. Space is O(1) extra, not counting the output list.