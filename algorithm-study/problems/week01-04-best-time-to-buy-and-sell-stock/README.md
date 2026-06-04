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

### Rachel

- **Approach**: Renew the max difference while iterating the array
- **My way**: Using double to check every pair led time limit exceeded error
- **Better way**: Trackiung the minimum price and maximum profit in a single loop. Using two if statements rather than if-else can reduce more time.

### Angela

- **Approach**: At first, I thought that storing the current price in a 'tmp' variable and calculate profit. If calculated profit is greater than saved profit value, update the profit value. If the final profit is less than 0, save 0 and return it. 
- **My way**: Using 'price', 'profit' and 'tmp' variables to store each current price value in prices array, current profit value, current calculated value. When the 'price' is smaller than current value in 'prices', update the 'price' value to the current 'prices' value. And when the 'tmp' is bigger than 'profit' value, update the 'profit' value to 'tmp'. Finally, check whether 'profit' is greater than 0. If not, save 0 to 'profit' and return the 'profit'. The time complexity is O(n)
- **Better way**: Focus on min and max value. Using 'cur_min', 'cur_max' variables and calculate the difference using 'diff_max' variable. Finally, return 'diff_max'. It can reduce code. 




