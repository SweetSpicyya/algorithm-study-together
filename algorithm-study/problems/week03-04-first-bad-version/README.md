# {278}. {First Bad Version}

**Link:** https://leetcode.com/problems/first-bad-version
**Difficulty:** Easy
**Topic:** Binary Search, Interactive

## Problem Summary

Find the first bad version of the product line using minimum call of the API

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I approached this problem using binary search. Since all versions after the first bad one are also bad, the list has a sorted structure, a contiguous block of false followed by true, which makes binary search applicable. At each step, I check the middle version and halve the search space accordingly.
- **Optimization**: In standard binary search, when the condition is met we set right = mid-1, discarding mid entirely. However, since mid itself could be the first bad version, I set right = mid instead to keep it in the search space. When left ===right, that point is the first bad version.
- **Complexity Analysis**:
  Time: O(log n) - search space halves each iteration
  Space: O(1) - no extra data structures used
- 
## Approaches & Discussion

### Yourim
the naive approach is we just iterate from 1 to n and the first time isBadVersion returns true, we return that index. 
Time complexity is O(N), and i guess in the worst case we're calling the API n times.
there's this clean boundary where everything left is false and everything right is true. That's a binary search signal.
We keep left and right pointers and check the midpoint. If it's bad, we pull right down to mid, keeping mid in play because it could be the answer. 
If it's good, we push left up to mid + 1. We keep going until they converge, and that's our answer.
mid is left + (right - left) // 2 instead of (left + right) // 2. Mathematically the same, but this avoids integer overflow in languages like Java or C++.
Time complexity is O(log N), space is O(1).