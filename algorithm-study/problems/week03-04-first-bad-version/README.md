# {278}. {First Bad Version}

**Link:** https://leetcode.com/problems/first-bad-version/description/

**Difficulty:** Easy

**Topic:** Binary Search, Interactive

## Problem Summary
Find out the first bad one, which causes all the following ones to be bed.

## Approaches & Discussion
### Angela

- **This problem is asking me to** find out first bad one, which causes all the following ones to be bad.
- **The brute force could be to** iterate and call isBadVersion function till find the first bad version **which runs in** O(n) **but it is wasteful since** we should minimize the number of calls to isBadVersion.
- **We can optimize this by** using Binary Search, **reducing it to** O(logn).
- **My approach is to** use left, right as pointers and set up the initial middle value. First of all, iteratively calling isBadVersion(middle) while left is less than right. If it is True, move right pointer to middle and update middle value otherwise move left pointer to middle+1 since the first bad version would be greater than middle and update middle value. Lastly, if two pointers point to the same position, return left
- **This runs in** O(logn) time complexity because this approach divides the search range in half each iteration and O(1) space complexity since only constant variables are used.