# {57}. {Insert Interval}

**Link:** https://leetcode.com/problems/insert-interval/
**Difficulty:** Medium
**Topic:** Array

## Problem Summary

Overlap the new interval into the original interval

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by trying to find the exact left and right boundaries where the newInterval should be inserted. My logic was to find the specific intervals where the overlap starts and ends, and then create a merged interval. However, this approach failed in a few cases: when the new interval engulfs the existing intervals, when it should be placed entirely at the beginning or the end, and when it fits perfectly between two existing intervals without overlapping.
- **Optimization**: To overcome the edge cases, I optimized the algotithm by adopting a single-pass linear scan approach. For left, iterate and push all intervals that end before the new interval starts. While intervals overlap with the new Interval, expand the boundaries by comparing existing ones with new interval's each end. And push the remaining intervals that start after the new interval ends.
- **Complexity Analysis**: This optimized approach gives me a time and space complexity of O(n), where n is the number of intervals in the input array.
