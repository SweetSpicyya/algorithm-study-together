# {33}. {Search in Rotated Sorted Array}

**Link:** https://leetcode.com/problems/search-in-rotated-sorted-array/
**Difficulty:** Medium
**Topic:** Array, Binary Search

## Problem Summary
find the index of a target value in a rotated sorted array.

## Approaches & Discussion
### Angela

- So, this problem is asking me to find the index of a target value in a rotated sorted array.
- Since the problem explicitly requires an $O(\log n)$ runtime complexity, an $O(N)$ linear scan is not an option.
- I will approach this by using Binary Search. Let me code this up.
- My approach is to initialize two pointers, `left` and `right`, to set the search boundaries. Next, while `left` is less than or equal to `right`, I calculate the `mid` index. If the `mid` element is the target, I return `mid`.
If not, I determine which half of the array is strictly sorted. If the left half is sorted, I check if the target falls within this range. If it does, I narrow the search to the left by updating `right = mid - 1`; otherwise, I update `left = mid + 1` to search the right half. Conversely, if the right half is sorted, I check if the target is within the right bounds and update the pointers accordingly. Lastly, if the target is not found, I return `-1`.
- This runs in $O(\log n)$ time complexity because this approach halves the search space at each step. The space complexity is $O(1)$ in the worst case, because we only use a constant extra space for pointers.

## Approaches & Discussion
### Yourim
The problem requires finding a target's index in a rotated sorted array in O(log n) time, which dictates using a modified Binary Search. 
No matter where you split a rotated sorted array in half, at least one of the halves is guaranteed to be perfectly sorted. Calculate mid and compare nums[left] with nums[mid] to determine which half (left or right) is normally sorted.
Check if the target falls within the boundaries of that sorted half (e.g., nums[left] <= target < nums[mid]). If the target is within the sorted half, narrow the search to that side. 
otherwise, move the pointers to search the opposite half, halving the array each time.

## Approaches & Discussion
### Rachel
- **Understand**: We're given a sorted array that has been rotated at an unknown index, and need to find the target in O(log n). A normal binary search won't work because the array isn't fully sorted.
- **Match**: This is a modified binary search problem. The key insight is that when you split a rotated sorted array in half, one side is always fully sorted. We can use that sorted side to determine which half the target belongs in
- **Plan**: At each step I find mid and check if the left half is sorted. If it is, I check if target falls within the left range. If yes, go left, otherwise go right. If the right half is sorted instead, I check if target falls withing the right range. If yes, go right, otherwise go left.
- **Evaluate**:
  Time: O(log n) - search space halves each iteration
  Space: O(1) - only left, right, mid pointers used
