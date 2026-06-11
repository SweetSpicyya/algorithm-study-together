# {39}. {Combination Sum}

**Link:** https://leetcode.com/problems/combination-sum/
**Difficulty:** Medium
**Topic:** Array, Backtracking

## Approaches & Discussion

### Rachel

- **Understand**: We're given an array of distinct integers and a target. We need to find all unique comninations that sum to target, where the same number can be used multiple times.
- **Match**: This is a classic Backtracking problem. We build combinations incrementally. At each step we choose a candidate, recurse with the remaining sum, then pop to try the next candidate. Passing start index prevents duplicate comninations like [2,3] and [3,2] from both appearing.
- **Plan**: I'll use a recursive backtrack function with three parameters: start(which index to start from), current(current combination), and remaining(how much sum is left). If remaining === 0 we found a valid combination and save a copy. If remaining < 0 we exceeded target and return. For each candidate from start onwards, I push it, recurse with the same start index (to allow reuse), then pop to backtrack.
- **Evaluate**:
  Time: O(n^(t/m)) - where n is candidates length, t is target, m is the minimum candidate value, branching factor n, max depth t/m
  Space: O(t/m) - maximum recursion depth is target divided by smallest candidate.
