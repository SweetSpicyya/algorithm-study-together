# {46}. {Permutations}

**Link:** https://leetcode.com/problems/permutations/
**Difficulty:** Medium
**Topic:** Array, Backtracking

## Approaches & Discussion

### Rachel

- **Understand**: We're given an array of distinct integers and need to return all possible permutations.
- **Match**: This is a Backtracking problem. We track which numbers have already been used in the current permutation since every number must appear exactly once but in any position.
- **Plan**: I'll use a recursive backtrack function that builds up current. The base case is when current.length === nums.length, at that point we save a copy as a complete permutation. For each number is nums, if it's already in current I skip it, otherwise I push it, recurse, then pop to backtrack and try other numbers.
- **Evaluate**:
  Time: O(n!\*n) - there are n! permutations, and current.includes() takes O(n) for each check
  Space: O(n) - recursion depth equals n, plus the current array of size n
