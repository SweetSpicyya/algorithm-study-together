# {973}. {K Closest Points to Origin}

**Link:** https://leetcode.com/problems/k-closest-points-to-origin/
**Difficulty:** Medium
**Topic:** Mid Level, Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect, Weekly Contest 119

## Problem Summary

Find suggested number of closest points from origin

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by calculating the Eucidean distance for every poing and sort the entire array. For each point, since we only need to compare the distance from the origin, we can simplify x²+y².
- **Optimization**: we could use a Max-Heap of size K to achieve O(NlogK) or Quick Select to achieve an average of O(N).
- **Complexity Analysis**: Time Complexity: O(NlogN), Space Complexity: O(N) (or O(logN) depending on the sort implementation)


## Problem Summary
Return the k closest points to the origin (0,0)

## Approaches & Discussion
### Angela

- **So the problem is asking me to** return the k closest points to the origin(0,0).
- **The brute force could be to** iterate and calculate all possible distance values and sorting the calculated values and return the k of closest points which runs in O(nlogn) but this is wasteful since sorting all values is unnecessary when we only need k closest.
- **We can optimize by** using heap, reducing it to O(nlogk) since we maintain a heap of size k instead of sorting all n values.
- **My approach is to** iterate points and calculate distance and save distance and the point to heap. Since we limited the heap size to k, if the size of the heap exceeds k, pop the greatest value from the heap then only k closest points remain in the heap and return the result.
- **This runs in** O(nlogk) time complexity because this approach maintains the size of heap to k and iterates over all n points and O(k) space complexity since the heap maintains at most k elements at any time
