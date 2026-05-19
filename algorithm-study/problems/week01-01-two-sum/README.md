# {Problem Number}. {Problem Title}

**Link:** https://leetcode.com/problems/two-sum/  
**Difficulty:** Easy
**Topic:** Array, Hash Table

## Problem Summary

Get indices of the two numbers to add up to target number

## Approaches & Discussion

### Yourim

- Approach: get the index of the number needed to reach the target
- My way : First of all, I thought in the loop, search the difference in the list.
  If it has the different number, put the index to the array with current index.
- Better way : In the loop, put each value and index to the HashMap.
  At this point, if the difference is already in the HashMap, then return difference index and current index.

### Rachel

- Approach: Although the title is Two "Sum" but it is not really about the sum method
- My way: Substract the current element from the target and find the same value as the difference in the remaining part of the array.
- Cons: Since it has double loops, in the worst case it takes more time and might fail the time test.
- Better way: Using a map minimizes the time for looping. By inserting elements one by one, we prevent the same element from being used twice.

### Angela

- Approach: Search for two numbers that add up to the target by comparing each element with the others.
- My way: I first tried a brute force approach using double loops to check every possible pair in the array.
- Cons : The $O(n^2)$ time complexity was too slow for large inputs, resulting in a Time Limit Exceeded (TLE) error.
- Better way : Switched to a Hash Map approach. By storing {value : index}, I can find the required complement($target - element$) in $O(1)$ time with a single pass, achieving $O(n)$ complexity.