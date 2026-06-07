# {33}. {Search in Rotated Sorted Array}

**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array
**Difficulty:** Medium
**Topic:** Array, Binary Search

## Approaches & Discussion

### Rachel

- **Understand**: We're given a sorted array that has been rotated at an unknown index, and need to find the target in O(log n). A normal binary search won't work because the array isn't fully sorted.
- **Match**: This is a modified binary search problem. The key insight is that when you split a rotated sorted array in half, one side is always fully sorted. We can use that sorted side to determine which half the target belongs in
- **Plan**: At each step I find mid and check if the left half is sorted. If it is, I check if target falls within the left range. If yes, go left, otherwise go right. If the right half is sorted instead, I check if target falls withing the right range. If yes, go right, otherwise go left.
- **Evaluate**:
  Time: O(log n) - search space halves each iteration
  Space: O(1) - only left, right, mid pointers used
