# {70}. {Climbing Stairs}

**Link:** https://leetcode.com/problems/climbing-stairs/
**Difficulty:** Easy
**Topic:** Math, Dynamic Programming, Memoization

## Approaches & Discussion

### Rachel

- **Understand**: We're climbing a staircase with n steps, and we can take either 1 or 2 steps at a time. We need to count the total number of distinct ways to reach the top.
- **Match**: This is Dynamic Programming problem that follows the Fibonacci pattern. To reach step n, we can only come from step n-1 or n-2 These two groups never overlap because the last step is different, so f(n) = f(n-1) + f(n-2).
- **Plan**: I'll create a dp array and set the base cases dp[1]=1 and dp[2]=2 directly since these can't be derived from the formula. Then from i=3 to n, I apply dp[i] = dp[i-1]+ dp[i-2]. The base cases are necessary because the recurrence relation requires two previous values to exist
- **Evaluate**:
  Time: O(n) - single pass from 3 to n
  Space: O(n) - dp array of size n+1
