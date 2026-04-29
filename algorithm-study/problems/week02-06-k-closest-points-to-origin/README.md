# {973}. {K Closest Points to Origin}

**Link:** https://leetcode.com/problems/k-closest-points-to-origin/
**Difficulty:** Medium
**Topic:** Mid Level, Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect, Weekly Contest 119

## Problem Summary

Find suggested number of closest points from origin

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by calculating the Eucidean distance for every poing and sort the entire array. For each point, since we only need to compare the distance from the origin, we can simplify x²+y².
- **Optimization**: we could use a Max-Heap of size K to achieve O(NlogK) or Quick Select to achieve an average of O(N).
- **Complexity Analysis**: Time Complexity: O(NlogN), Space Complexity: O(N) (or O(logN) depending on the sort implementation)
