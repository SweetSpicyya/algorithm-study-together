# {39}. {Combination Sum}

**Link:** https://leetcode.com/problems/combination-sum/

**Difficulty:** Medium

**Topic:** Array, Backtracking

## Problem Summary
find all unique combinations of candidates that sum to a specific target.

## Approaches & Discussion
### Angela

- So, this problem is asking me to find all unique combinations of candidates that sum to a specific target.
- Since we need to explore all possible valid combinations, I will approach this by using **Backtracking**. Let me code this up.
- My approach is to initialize a result array and a temporary array to keep track of the current combination. I will create a recursive function that takes the `index` as an argument. Inside the function, if the sum of the temporary array equals the target, I append **a copy of the temporary array** to the result and return. If the sum exceeds the target, I simply return to **prune the search tree**.Next, I iterate through the candidates starting from the given `index`. This ensures we don't look back, preventing duplicate combinations. For each number, I append it to the temporary array and recursively call the function **with the same index**, allowing unlimited reuse of the current number.After the recursive call returns, I **pop the number** from the temporary array to backtrack and explore other choices. Lastly, I initiate the recursive function starting at index 0 and return the result array.
- This runs in **$O(N^{\frac{T}{M}})$ time complexity**, where $N$ is the number of candidates and $\frac{T}{M}$ is the maximum depth of the recursion tree. The space complexity is **$O(\frac{T}{M})$** in the worst case due to the call stack and the temporary array.