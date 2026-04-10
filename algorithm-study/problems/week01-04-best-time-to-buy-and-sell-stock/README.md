# {121}. {Best Time to Buy and Sell Stock}

**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/  
**Difficulty:** Easy
**Topic:** Array, Dynamic Programming

## Problem Summary
Find best profit time

## Approaches & Discussion
### Yourim
- **Approach**: Iterate the list and find max profit time 
- **My way** : while iterating through the price list, update the min_price whenever it encounter a price lower than current minimum.
Also calculate the potential profit at each step and keep track of the max profit.
- **Better way** : Optimize the logic by removing the redundant max variable.
