# {704}. {Binary Search}

**Link:** https://leetcode.com/problems/binary-search/
**Difficulty:** Easy
**Topic:** Array, Binary Search

## Problem Summary
Find the index having same integer. Otherwise, return -1

## Approaches & Discussion

### Yourim
As a brute force approach, I could simply iterate through the array to search the target.
However, that would be O(n) time complexity, and since the problem asks for O(log n), I need a better approach.
The given array is a sorted list in ascending order, so I can apply binary search.
My approach is to search for the target starting from the middle of list.
I'll maintain two pointers left and right representing the current search boundaries.
First, if the target equals the middle element, I immediately return its index and we're done.
If the target is larger than the middle element, I move the left boundary to mid+1, narrowing the search to the right half.
Otherwise, the target is lower than middle elements, so I move the right boundary to mid -1, narrowing the search to the right half.
I repeat this until the target is found or left exceeds right, meaning the target doesn't exist in the array,
so I return -1.


### Rachel

- **My way**: Since the array is sorted, I thought about using Binary Search because the title of the problem is Binary Search. Initiall, I considered using length/2 but I realized that this calculates the midpoint from 0 index. Since binary search involves narrowing down the range, calculating the mid-index with left/right pointer is the correct way to find the mid-index.
- **Better answer**: To solve this problem, I implemented a Binary Search algorithm. Since the input array is already sorted in ascending order, Binary Search is the most efficient approach to find the target with a time complexity of O(log n).
  I used two pointers, left at index 0 and right at the end of the array. Inside a while loop, I calculated the mid index and compared nums[mid] with the target. if nums[mid] equals the target, I return the index. If the target is greater, I move the left pointer to mid + 1. Otherwise, right pointer to mid-1.

### Angela

- **Understand** : So the problem is asking me to find the index of a target value in a sorted array.
- **Brute force**: The brute force way would be to traverse the entire array to find the target which runs in O(n).
- **Better way** : We can optimize this by using the binary search.
- **Approach**: My approach is to divide nums in half and compare with target using left, right and mid variables. If nums[mid] is the same as the target, return mid immediately. If nums[mid] is bigger than target, set the right variable to mid-1 otherwise if nums[mid] is smaller than target, set the left variable to mid+1. Finally return the result.
- **Complexity** : This runs in O(log n) time complexity because this approach divides nums in half with every iteration and O(1) space complexity since only a constant number of variables(left, right, mid) are used
