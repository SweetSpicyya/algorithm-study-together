# {973}. {K Closest Points to Origin}

**Link:** https://leetcode.com/problems/k-closest-points-to-origin
**Difficulty:** Medium
**Topic:** Mid Level, Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect, Weekly Contest 119

## Problem Summary
Return the k closest points to the origin (0, 0).

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

  
## Approaches & Discussion
### Yourim
- **Coding interview**:
<details>
  <summary>Click to view details </summary>

So the problem is, um, given a list of points on a 2D plane, we want to find the k closest points to the origin. 
And distance here is just the standard Euclidean distance.

Okay so the naive approach, the idea is pretty straightforward. We iterate through every single point, calculate the distance using the formula, 
so like, square root of x squared plus y squared — and we just collect all of those into a new array as a tuple of distance and the point itself.
Then we sort that array in ascending order. And I guess once it's sorted, we just loop from the front and grab the first k items.
So the time complexity on this is O(N log N) because of the sort. And I mean, that's not terrible, but the thing is.
we're sorting the entire array when we only actually care about the top k elements. So there's definitely room to improve here.

So the key insight is instead of sorting everything, what if we just maintain a heap of size k as we go through the points? 
That way we never have to touch more than k elements at a time.
And one thing I want to talk about here is the heap trick. So like, Python only gives us a min-heap out of the box. 
But what we actually want here is a max-heap. So that we can quickly identify and kick out the farthest point whenever the heap gets too big. 
So the way we handle that is we just negate the distance before we push it in. That way the largest distance becomes the smallest number, and the min-heap behaves like a max-heap.
And I guess another thing. we don't actually need the square root here. So like, if we're just comparing distances, square root is a monotonic function, meaning the order doesn't change whether we apply it or not. 
So we can just use x² + y² directly and skip the sqrt entirely. Saves us some computation.
So the setup is we iterate through every point. For each one we compute the negated squared distance. If the heap has fewer than k elements, we just push it in. 
Otherwise, we do a pushpop which pushes the new element and pops the current maximum in one step. So at the end of the loop, the heap always holds the k closest points we've seen so far.
Time complexity here is O(N log K) — for each of the N points we do a heap operation that costs log K. And space is O(K) since we're only ever keeping k elements in the heap.
</details>

