# {238}. {Product of Array Except Self}

**Link:** https://leetcode.com/problems/product-of-array-except-self

**Difficulty:** Medium
**Topic:** Array, Prefix Sum

## Problem Summary
Given an array of integers, return an array where each element is the product of all numbers except itself, without using division and in O(n) time.

## Approaches & Discussion
### Yourim
To solve this problem efficiently in O(n) time without using division, I used a two-pass prefix and suffix product approach. 
First, I iterated forward through the array to calculate the prefix product for each element, which represents the product of all numbers to its left. 
Then, I iterated backward to compute the suffix product of all numbers to its right, multiplying it directly into our result array to save space. 
This allows us to find the total product except self for every position in just two linear passes.
Ultimately, this optimizes the time complexity to O(n) while maintaining an O(1) auxiliary space complexity.