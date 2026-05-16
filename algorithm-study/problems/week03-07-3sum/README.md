# {15}. {3Sum}

**Link:** https://leetcode.com/problems/3Sum
**Difficulty:** Medium
**Topic:** Array, Two Pointers, Sorting

## Problem Summary

Return all unique triplets from a given array that sum to zero

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I approached this problem by sorting the array first, then fixing one element i and using two pointers left and right to find the remaining twe elements. Since the array is sorted, if the sum is too small I move left pointer to right, and if the sum is too large i move right to left. When the sum equals zero, I store the triplet.
- **Optimization**: The main challenge after getting the basic logic right was handling duplicate triplets. I added two layers of dupicate skipping. First, if nums[i] is the same as nums[i-1], I skip that i entirely with continue to avoid starting a search from the same value twice. Second, after storing a valid triplet, I skip over any consecutive duplicate values at left and right before moving the pointers, to avoid pushing the same triplet again.
- **Complexity Analysis**:
  Time: O(n²) - outer for loop is O(n), inner while loop is O(n), sorting is O(n log n) but dominated by O(n²)
  Space: O(n) - sorting takes O(log n) space, result array takes O(n) in the worst case
