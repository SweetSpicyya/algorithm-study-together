# {322}. {Coin Change}

**Link:** https://leetcode.com/problems/coin-change/
**Difficulty:** Medium
**Topic:** Array, Dynamic Programming, Breadth-First Search

## Approaches & Discussion
### Yourim
This solution uses Bottom-up Dynamic Programming to find the minimum number of coins needed for each amount from 1 to the target.
The dp array is initialized with a large value (amount + 1) to represent infinity, while dp[0] is set to 0 as the base case.
The outer loop iterates through all amounts, and the inner loop checks each coin to update the optimal count.
Finally, it returns dp[amount] if the value was updated, or -1 if the target amount cannot be reached with the given coins.
