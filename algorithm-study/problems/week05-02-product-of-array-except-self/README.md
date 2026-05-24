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


## Approaches & Discussion
### Rachel
- **Understand**: We're given an array and need to return a new array where each element is the product of all other elements except itself. Division is not allowed and it must run in O(n).
- **Match**:This is a prefix/suffix product problem. prefix[i] stores the product of all elements to the left of i, and suffix[i] stores the product of all elements to the right of i. Multiplying them gives the answer for each index.
- **Plan**: I'll build a prefix array where prefix[i] = prefix[i-1] _ nums[i-1], starting with prefix[0]=1 since there's nothing to the left. Then I'll build a suffix array going right to left where suffix[i] = suffix[i+1] _ nums[i+1], starting with suffix[nums.length-1]=1 since there's nothing to the right. Finally I multiply prefix[i] \* suffix[i] for each index.
- **Evaluate**:
  Time: O(n) - three separate linear passes through the array
  Space: O(n) - prefix and suffix arrays each of size n