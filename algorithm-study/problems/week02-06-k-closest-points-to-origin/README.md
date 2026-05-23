# {973}. {K Closest Points to Origin}

**Link:** https://leetcode.com/problems/k-closest-points-to-origin
**Difficulty:** Medium
**Topic:** Mid Level, Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect, Weekly Contest 119

## Problem Summary
Return the k closest points to the origin (0, 0).

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

