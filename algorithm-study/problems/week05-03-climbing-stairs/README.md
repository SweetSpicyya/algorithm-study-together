# {70}. {Climbing Stairs}

**Link:** https://leetcode.com/problems/climbing-stairs

**Difficulty:** Easy
**Topic:** Math, Dynamic Programming, Memoization

## Problem Summary
Get distinct ways can you climb to the top

## Approaches & Discussion
### Yourim
To solve this problem, I used Dynamic Programming.
The core idea is that to reach the n-th step, you can only come from either the (n-1)-th step or the (n-2)-th step. 
Therefore, the total number of ways to reach step n is the sum of the ways to reach step n-1 and step n-2. This is exactly like the Fibonacci sequence.
First, I handled the base cases. if n is 1 or 2, the answer is simply 1 or 2.
Then, I used a loop to build up the solution from step 3 all the way to n, storing the values in an array. 
Finally, I returned the value at index n.
Time complexity is O(n).

## Approaches & Discussion
### Rachel

- **Understand**: We're climbing a staircase with n steps, and we can take either 1 or 2 steps at a time. We need to count the total number of distinct ways to reach the top.
- **Match**: This is Dynamic Programming problem that follows the Fibonacci pattern. To reach step n, we can only come from step n-1 or n-2 These two groups never overlap because the last step is different, so f(n) = f(n-1) + f(n-2).
- **Plan**: I'll create a dp array and set the base cases dp[1]=1 and dp[2]=2 directly since these can't be derived from the formula. Then from i=3 to n, I apply dp[i] = dp[i-1]+ dp[i-2]. The base cases are necessary because the recurrence relation requires two previous values to exist
- **Evaluate**:
  Time: O(n) - single pass from 3 to n
  Space: O(n) - dp array of size n+1


## Approaches & Discussion
### Angela

- So, this problem is asking me to find how many distinct ways we can climb to the top.
- The brute force way would be to check all possible combinations using pure recursion, which runs in **$O(2^N)$ time complexity**.
- We can optimize this by using the Fibonacci structure, which reduces the time complexity to **$O(N)$**.
- I will approach this by using a recursive Fibonacci function with a **HashMap to store the calculated values** and avoid recalculation. Now, let me code this up.
- My approach is to initialize a HashMap called `memo`. Inside the Fibonacci function, if the current `num` is already in `memo`, it means we already calculated it, so we can just return that value. If `num` is 1, return 1, and if `num` is 2, return 2. Otherwise, we calculate the answer recursively, store it in `memo`, and then return it.
- This runs in **$O(N)$ time complexity** because thanks to the `memo` map, we **visit each stair level at most once**. The **space complexity is also $O(N)$** since the `memo` map can hold up to $N$ results in the worst case.

