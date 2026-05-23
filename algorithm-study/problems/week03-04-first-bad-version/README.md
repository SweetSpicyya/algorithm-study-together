# {278}. {First Bad Version}

**Link:** https://leetcode.com/problems/first-bad-version
**Difficulty:** Easy
**Topic:** Binary Search, Interactive

## Problem Summary

Find the first bad version of the product line using minimum call of the API

## Approaches & Discussion

### Yourim
the naive approach is we just iterate from 1 to n and the first time isBadVersion returns true, we return that index. 
Time complexity is O(N), and i guess in the worst case we're calling the API n times.
there's this clean boundary where everything left is false and everything right is true. That's a binary search signal.
We keep left and right pointers and check the midpoint. If it's bad, we pull right down to mid, keeping mid in play because it could be the answer. 
If it's good, we push left up to mid + 1. We keep going until they converge, and that's our answer.
mid is left + (right - left) // 2 instead of (left + right) // 2. Mathematically the same, but this avoids integer overflow in languages like Java or C++.
Time complexity is O(log N), space is O(1).

