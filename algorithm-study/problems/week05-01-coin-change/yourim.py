class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
        dp[0] = 0 # [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]

        for a in range(1, amount+1): # 7
            for c in coins: # 5
                if a >= c:
                    dp[a] = min(dp[a], dp[a - c] + 1) # dp[2] = min(12, dp[5]+1) # 2

        if dp[amount] == amount+1:
            return -1
        else:
            return dp[amount]

s = Solution()
coins = [1,2,5]
amount = 11
print(s.coinChange(coins, amount))