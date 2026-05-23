# {238}. {Product of Array Except Self}

**Link:** https://leetcode.com/problems/product-of-array-except-self
**Difficulty:** Medium
**Topic:** Array, Prefix Sum

## Approaches & Discussion

### Rachel

- **Understand**: We're given an array and need to return a new array where each element is the product of all other elements except itself. Division is not allowed and it must run in O(n).
- **Match**:This is a prefix/suffix product problem. prefix[i] stores the product of all elements to the left of i, and suffix[i] stores the product of all elements to the right of i. Multiplying them gives the answer for each index.
- **Plan**: I'll build a prefix array where prefix[i] = prefix[i-1] _ nums[i-1], starting with prefix[0]=1 since there's nothing to the left. Then I'll build a suffix array going right to left where suffix[i] = suffix[i+1] _ nums[i+1], starting with suffix[nums.length-1]=1 since there's nothing to the right. Finally I multiply prefix[i] \* suffix[i] for each index.
- **Evaluate**:
  Time: O(n) - three separate linear passes through the array
  Space: O(n) - prefix and suffix arrays each of size n
