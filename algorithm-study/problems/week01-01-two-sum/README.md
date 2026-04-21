# {Problem Number}. {Problem Title}

**Link:** https://leetcode.com/problems/two-sum/  
**Difficulty:** Easy
**Topic:** Array, Hash Table

## Problem Summary

Get indices of the two numbers to add up to target number

## Approaches & Discussion

### Rachel

- Approach: Although the title is Two "Sum" but it is not really about the sum method
- My way: Substract the current element from the target and find the same value as the difference in the remaining part of the array.
- Cons: Since it has double loops, in the worst case it takes more time and might fail the time test.
- Better way: Using a map minimizes the time for looping. By inserting elements one by one, we prevent the same element from being used twice.
