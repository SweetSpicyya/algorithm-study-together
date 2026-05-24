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

### Rachel

- **Understand**: We're given an array of coin denominations and a target amount. We need to return the minimum number of coins to make up that amount, or -1 if it's impossible.
- **Match**: This is a classic Dynamic Programming problem. if we know the minimum coins needed for every amount from 0 to i-1, we can compute the answer for i by trying each coin and taking the minimum.
- **Plan**: I'll create a dp array of size amount+1 filled with Infinity. For each amount from 1 to amount, I try every coin
- **Evaluate**:
  Time: O(n×m) where n is amount and m is coins.length for each amount we try every coin
  Space: O(n) dp array of size amount+1
