# {121}. {Best Time to Buy and Sell Stock}

**Link:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/  
**Difficulty:** Easy
**Topic:** Array, Dynamic Programming

## Problem Summary

Find best profit time

## Approaches & Discussion

### Angela

- **Approach**: At first, I thought that storing the current price in a 'tmp' variable and calculate profit. If calculated profit is greater than saved profit value, update the profit value. If the final profit is less than 0, save 0 and return it. 
- **My way**: Using 'price', 'profit' and 'tmp' variables to store each current price value in prices array, current profit value, current calculated value. When the 'price' is smaller than current value in 'prices', update the 'price' value to the current 'prices' value. And when the 'tmp' is bigger than 'profit' value, update the 'profit' value to 'tmp'. Finally, check whether 'profit' is greater than 0. If not, save 0 to 'profit' and return the 'profit'. The time complexity is O(n)
- **Better way**: Focus on min and max value. Using 'cur_min', 'cur_max' variables and calculate the difference using 'diff_max' variable. Finally, return 'diff_max'. It can reduce code. 




