# {542}. {01 Matrix}

**Link:** https://leetcode.com/problems/01-matrix/
**Difficulty:** Medium
**Topic:** Principal, Array, Dynamic Programming, Breadth-First Search, Matrix

## Problem Summary

Find the distance of the nearest 0 for each cell

## Approaches & Discussion

### Rachel

- **Brute-force / Initial Approach**: I initially approached the problem by setting 0 for the cells that is 0, and then searching 4 directions of the 1 while finding 0.
- **Optimization**: Instead of calculating the distance for each 1 individualy, I optimized the solution by using a Multi-source Breadth-First Search. By initiating the BFS from 0, it can propagate the distance incrementally. I initialized all 1s as Infinity to track unvisited cells.
