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