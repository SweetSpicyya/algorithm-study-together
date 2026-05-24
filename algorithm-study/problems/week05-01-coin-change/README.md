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


## Approaches & Discussion
### Angela

- **So this problem is asking me to** find the fewest number of coins that make up given amount.
- **I will approach this by** using HashMap and BFS by using queue.
- **Now, let me code this up.**
- **My approach is to** initialize the queue as set of given amount and count of coins 0. Next, while the queue is not empty, iterating calculation, pop amount, count from the queue and iterate over the coins and calculate current amount and count current number of coin. If current amount is less than 0, skip it also if current amount already exists in hashmap, it means we already calculated the fewest number of coins for that amount so we can skip it otherwise, add it to the hashmap and append it into queue aswell. If current amount is 0, return current count or If we can't find the answer, return -1
- **Let's say** A means our goal amount and C means number of the coins, this runs in O(AxC) time complexity because we visit each amount at most once and we check each coins at evert step and O(A) space complexity since the queue and hashmap can grow up to the A.
