# {53}. {Maximum Subarray}

**Link:** https://leetcode.com/problems/maximum-subarray/  
**Difficulty:** Medium
**Topic:** Array, Divide and Conquer, Dynamic Programming

## Problem Summary
Find the subarray with the largest sum in given array, and return its sum.

## Approaches & Discussion
### Yourim
- **Coding interview**:
So, my first approach is just brute-force it.
Simply try every possible subarray using nested loop.
But using nested loop takes nxn time complexity, so it's not efficient.
So how do we optimize it?
I think we need global max sum variable to keep maximum sum.
And compare current item and sum that summed so far and then, get max result between those.
if current item is greater than sum, the result will be current item.
Now compare global max sum variable and previous result, that will be the largest sum.
Time complexity is O(n) because it iterates the given array once.

## Approaches & Discussion
### Angela

- **Understand** : So the problem is asking me to find the subarray with the largest sum. 
- **Brute force** : The brute force way would be to explore all possible subarrays and compare each sum from subarray, return maximum sum value which runs in O(n^2) 
- **Better way**: We can optimize this by using Kadane's Algorithm which runs in O(n). 
- **Approach**: My approach is to use Kadane's Algorithm. Set up the initial current_sum and max_sum variable and using loop, to handle the edge case where all elements are negative, max_sum is initialized to nums[0] instead of 0. Explore the num in the nums and add current value to current_sum and compare max_sum with current_sum. If current_sum is bigger than max_sum, update max_sum to current_sum. Also if current_sum is less than 0, reset the current_sum to 0 according to Kadane's Algorithm. Finally, return max_sum. 
- **Complexity** : This runs in O(n) time complexity because this approach visits every element once and O(1) space complexity since only a constant number of variables(current_sum, max_sum) are used.

## Approaches & Discussion
### Rachel

- **My way**: I initially thought to accumulate numbers from index 0 and compare the sums. However, this approach only blindly accumulates numbers from the beginning, failing to determine when to discard the previous sum and start fresh. It couldn't handle cases where a large negative prefix reduces the overall sum.
- **Better way**: To solve the problem using Divide and Conquer, splitting the array into two halves and consider three possible scenarios for the maximum subarray, left case - The maximum subarray is entirely located in the left half, right case - right half, cross case - crosses the midpoint. Recursively split the array into smaller subarrays until each contains only one element. For each split, find the maximum sum of the left half and the right half. Calculate the Cross Maximum Sum by starting from the midpoint and extending to both ends to find the best possible combined sum. Finally, return the maximum of the three cases (Left, Right, and Cross).










