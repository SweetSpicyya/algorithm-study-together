# {39}. {Combination Sum}

**Link:** https://leetcode.com/problems/combination-sum
**Difficulty:** Medium
**Topic:** Array, Backtracking

## Problem Summary
return a list of all unique combinations of candidates where the chosen numbers sum to target.

## Approaches & Discussion
### Yourim
The problem requires finding a target's index in a rotated sorted array in O(log n) time, which dictates using a modified Binary Search. 
No matter where you split a rotated sorted array in half, at least one of the halves is guaranteed to be perfectly sorted. Calculate mid and compare nums[left] with nums[mid] to determine which half (left or right) is normally sorted.
Check if the target falls within the boundaries of that sorted half (e.g., nums[left] <= target < nums[mid]). If the target is within the sorted half, narrow the search to that side. 
otherwise, move the pointers to search the opposite half, halving the array each time.

## Approaches & Discussion
### Rachel
- **Understand**: We're given an array of distinct integers and a target. We need to find all unique comninations that sum to target, where the same number can be used multiple times.
- **Match**: This is a classic Backtracking problem. We build combinations incrementally. At each step we choose a candidate, recurse with the remaining sum, then pop to try the next candidate. Passing start index prevents duplicate comninations like [2,3] and [3,2] from both appearing.
- **Plan**: I'll use a recursive backtrack function with three parameters: start(which index to start from), current(current combination), and remaining(how much sum is left). If remaining === 0 we found a valid combination and save a copy. If remaining < 0 we exceeded target and return. For each candidate from start onwards, I push it, recurse with the same start index (to allow reuse), then pop to backtrack.
- **Evaluate**:
  Time: O(n^(t/m)) - where n is candidates length, t is target, m is the minimum candidate value, branching factor n, max depth t/m
  Space: O(t/m) - maximum recursion depth is target divided by smallest candidate.

## Approaches & Discussion
### Angela

- So, this problem is asking me to find all unique combinations of candidates that sum to a specific target.
- Since we need to explore all possible valid combinations, I will approach this by using **Backtracking**. Let me code this up.
- My approach is to initialize a result array and a temporary array to keep track of the current combination. I will create a recursive function that takes the `index` as an argument. Inside the function, if the sum of the temporary array equals the target, I append **a copy of the temporary array** to the result and return. If the sum exceeds the target, I simply return to **prune the search tree**.Next, I iterate through the candidates starting from the given `index`. This ensures we don't look back, preventing duplicate combinations. For each number, I append it to the temporary array and recursively call the function **with the same index**, allowing unlimited reuse of the current number.After the recursive call returns, I **pop the number** from the temporary array to backtrack and explore other choices. Lastly, I initiate the recursive function starting at index 0 and return the result array.
- This runs in **$O(N^{\frac{T}{M}})$ time complexity**, where $N$ is the number of candidates and $\frac{T}{M}$ is the maximum depth of the recursion tree. The space complexity is **$O(\frac{T}{M})$** in the worst case due to the call stack and the temporary array.
