# {704}. {Binary Search}

**Link:** https://leetcode.com/problems/binary-search/description/
**Difficulty:** Easy
**Topic:** Array, Binary Search

## Problem Summary

Find the index having same integer. Otherwise, return -1

## Approaches & Discussion

### Rachel

- **My way**: Since the array is sorted, I thought about using Binary Search because the title of the problem is Binary Search. Initiall, I considered using length/2 but I realized that this calculates the midpoint from 0 index. Since binary search involves narrowing down the range, calculating the mid-index with left/right pointer is the correct way to find the mid-index.
- **Better answer**: To solve this problem, I implemented a Binary Search algorithm. Since the input array is already sorted in ascending order, Binary Search is the most efficient approach to find the target with a time complexity of O(log n).
  I used two pointers, left at index 0 and right at the end of the array. Inside a while loop, I calculated the mid index and compared nums[mid] with the target. if nums[mid] equals the target, I return the index. If the target is greater, I move the left pointer to mid + 1. Otherwise, right pointer to mid-1.
