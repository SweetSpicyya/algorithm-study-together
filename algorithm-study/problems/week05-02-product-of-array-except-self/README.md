# {238}. {Product of Array Except Self}

**Link:** https://leetcode.com/problems/product-of-array-except-self/description/

**Difficulty:** Medium

**Topic:** 

## Problem Summary
make an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`

## Approaches & Discussion
### Angela

- So, this problem is asking me to make an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
- Since we need to process every element in the array at least once, an **$O(N)$ time complexity is already optimal.**
- I will approach this by using **prefix and suffix products**. Now, let me code this up.
- My approach is to initialize `left`, `right`, and `output` arrays **to 1**. Next, I will **go through the array forward and backward** to calculate the left side and the right side. After that, I will calculate the final result by **multiplying the left and right products**.
- Let's say **$N$** represents the number of elements in the `nums` array.
This runs in **$O(N)$ time complexity** because this approach iterates over all elements once, and **$O(N)$ space complexity** since the `left` and `right` arrays can grow up to **the size of the array**.