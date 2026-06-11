# {46}. {Permutations}

**Link:** https://leetcode.com/problems/permutations
**Difficulty:** Medium
**Topic:** Array, Backtracking

## Problem Summary
return all the possible permutations in given array.

## Approaches & Discussion
### Yourim
This solution uses backtracking with a recursive helper function to generate all possible permutations. 
We maintain a visited boolean array to keep track of which numbers are already used in the current path. 
The recursive function acts as a decision tree, iterating through every number and building up a curr_permutation list. 
Once the list reaches the same length as the input array, a copy of it is added to our final result list. 
After each deep dive, the code performs backtracking by popping the last element and resetting its visited status back to False to explore the next alternative path.

## Approaches & Discussion
### Angela

- So, this problem is asking me to **generate** all possible permutations of a given array.
- Since we need to explore all possible permutations, I will approach this by using Backtracking. Let me code this up.
- My approach is to initialize a result array and a temporary array to keep track of the **current permutation**. Next, I will create a recursive function. Inside the function, if the length of the temporary array **equals the length of the input array**, I append a copy of the temporary array to the result and return.
- Then, I iterate through the given numbers. **If the current number is already in the temporary array, I skip it.** Otherwise, I append it to the temporary array and call the backtracking function. **After the recursive call returns**, I pop the number from the temporary array to backtrack and explore other choices. Lastly, I initiate the recursive function and return the result array.
- This runs in **O(N!)** time complexity because we generate all N factorial permutations. The space complexity is **O(N)** since the call stack and the temporary array can grow up to the length of the input array.
