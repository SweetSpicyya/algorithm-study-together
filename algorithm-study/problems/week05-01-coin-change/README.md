# {322}. {Coin Change}

**Link:** https://leetcode.com/problems/coin-change/
**Difficulty:** Medium
**Topic:** Array, Dynamic Programming, Breadth-First Search

## Approaches & Discussion

### Rachel

- **Understand**: We're given an array of coin denominations and a target amount. We need to return the minimum number of coins to make up that amount, or -1 if it's impossible.
- **Match**: This is a classic Dynamic Programming problem. if we know the minimum coins needed for every amount from 0 to i-1, we can compute the answer for i by trying each coin and taking the minimum.
- **Plan**: I'll create a dp array of size amount+1 filled with Infinity. For each amount from 1 to amount, I try every coin
- **Evaluate**:
  Time: O(n×m) where n is amount and m is coins.length for each amount we try every coin
  Space: O(n) dp array of size amount+1
