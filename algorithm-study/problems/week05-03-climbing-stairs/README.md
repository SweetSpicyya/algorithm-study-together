# {70}. {Climbing Stairs}

**Link:** https://leetcode.com/problems/climbing-stairs/description/

**Difficulty:** Easy

**Topic:** 

## Problem Summary
find how many distinct ways we can climb to the top.

## Approaches & Discussion
### Angela

- So, this problem is asking me to find how many distinct ways we can climb to the top.
- The brute force way would be to check all possible combinations using pure recursion, which runs in **$O(2^N)$ time complexity**.
- We can optimize this by using the Fibonacci structure, which reduces the time complexity to **$O(N)$**.
- I will approach this by using a recursive Fibonacci function with a **HashMap to store the calculated values** and avoid recalculation. Now, let me code this up.
- My approach is to initialize a HashMap called `memo`. Inside the Fibonacci function, if the current `num` is already in `memo`, it means we already calculated it, so we can just return that value. If `num` is 1, return 1, and if `num` is 2, return 2. Otherwise, we calculate the answer recursively, store it in `memo`, and then return it.
- This runs in **$O(N)$ time complexity** because thanks to the `memo` map, we **visit each stair level at most once**. The **space complexity is also $O(N)$** since the `memo` map can hold up to $N$ results in the worst case.