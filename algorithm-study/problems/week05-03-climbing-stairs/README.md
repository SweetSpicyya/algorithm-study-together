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
