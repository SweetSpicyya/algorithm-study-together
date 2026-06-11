# {46}. {Permutations}

**Link:** https://leetcode.com/problems/permutations/description/

**Difficulty:** Medium

**Topic:** Array, Backtracking

## Problem Summary
find all unique combinations of candidates that sum to a specific target.

## Approaches & Discussion
### Angela

- So, this problem is asking me to **generate** all possible permutations of a given array.
- Since we need to explore all possible permutations, I will approach this by using Backtracking. Let me code this up.
- My approach is to initialize a result array and a temporary array to keep track of the **current permutation**. Next, I will create a recursive function. Inside the function, if the length of the temporary array **equals the length of the input array**, I append a copy of the temporary array to the result and return.
- Then, I iterate through the given numbers. **If the current number is already in the temporary array, I skip it.** Otherwise, I append it to the temporary array and call the backtracking function. **After the recursive call returns**, I pop the number from the temporary array to backtrack and explore other choices. Lastly, I initiate the recursive function and return the result array.
- This runs in **O(N!)** time complexity because we generate all N factorial permutations. The space complexity is **O(N)** since the call stack and the temporary array can grow up to the length of the input array.