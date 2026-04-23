# {53}. {Maximum Subarray}

**Link:** https://leetcode.com/problems/maximum-subarray/
**Difficulty:** Easy
**Topic:** Array, Divide and Conquer, Dynamic Programming

## Problem Summary

Find the subarray with the largest sum and return its sum

## Approaches & Discussion

### Rachel

- **My way**: I initially thought to accumulate numbers from index 0 and compare the sums. However, this approach only blindly accumulates numbers from the beginning, failing to determine when to discard the previous sum and start fresh. It couldn't handle cases where a large negative prefix reduces the overall sum.
- **Better way**: To solve the problem using Divide and Conquer, splitting the array into two halves and consider three possible scenarios for the maximum subarray, left case - The maximum subarray is entirely located in the left half, right case - right half, cross case - crosses the midpoint. Recursively split the array into smaller subarrays until each contains only one element. For each split, find the maximum sum of the left half and the right half. Calculate the Cross Maximum Sum by starting from the midpoint and extending to both ends to find the best possible combined sum. Finally, return the maximum of the three cases (Left, Right, and Cross).
