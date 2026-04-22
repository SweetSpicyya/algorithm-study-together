# {704}. {Binary Search}

**Link:** https://leetcode.com/problems/binary-search/
**Difficulty:** Easy
**Topic:** Array, Binary Search

## Problem Summary
Find the index having same integer. Otherwise, return -1

## Approaches & Discussion

### Angela

- **Understand** : So the problem is asking me to find the index of a target value in a sorted array.
- **Brute force**: The brute force way would be to traverse the entire array to find the target which runs in O(n).
- **Better way** : We can optimize this by using the binary search.
- **Approach**: My approach is to divide nums in half and compare with target using left, right and mid variables. If nums[mid] is the same as the target, return mid immediately. If nums[mid] is bigger than target, set the right variable to mid-1 otherwise if nums[mid] is smaller than target, set the left variable to mid+1. Finally return the result.
- **Complexity** : This runs in O(log n) time complexity because this approach divides nums in half with every iteration and O(1) space complexity since only a constant number of variables(left, right, mid) are used
