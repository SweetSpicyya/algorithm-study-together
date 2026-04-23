# {53}. {Maximum Subarray}

**Link:** https://leetcode.com/problems/maximum-subarray/description/
**Difficulty:** Medium
**Topic:** Array, Divide and Conquer, Dynamic Programming

## Problem Summary
Return the subarray with the largest sum.

## Approaches & Discussion

### Angela

- **Understand** : So the problem is asking me to find the subarray with the largest sum. 
- **Brute force** : The brute force way would be to explore all possible subarrays and compare each sum from subarray, return maximum sum value which runs in O(n^2) 
- **Better way**: We can optimize this by using Kadane's Algorithm which runs in O(n). 
- **Approach**: My approach is to use Kadane's Algorithm. Set up the initial current_sum and max_sum variable and using loop, to handle the edge case where all elements are negative, max_sum is initialized to nums[0] instead of 0. Explore the num in the nums and add current value to current_sum and compare max_sum with current_sum. If current_sum is bigger than max_sum, update max_sum to current_sum. Also if current_sum is less than 0, reset the current_sum to 0 according to Kadane's Algorithm. Finally, return max_sum. 
- **Complexity** : This runs in O(n) time complexity because this approach visits every element once and O(1) space complexity since only a constant number of variables(current_sum, max_sum) are used.











