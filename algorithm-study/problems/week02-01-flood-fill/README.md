# {733}. {Flood Fill}

**Link:** https://leetcode.com/problems/flood-fill/description/
**Difficulty:** Easy
**Topic:** Mid Level, Array, Depth-First Search, Breadth-First Search, Matrix, Weekly Contest 60

## Problem Summary

Fill adjacent pixels with the same color

## Approaches & Discussion

### Rachel

- **My way**: Check if the adgacent pixels have the same value and then check their neighbors before changing the color
- **Better answer**: The pronlem asks us to find all pixels that are 4-directionally connected to the starting pixel and have the same initial color. First, store the color of the starting pixel image[sr][sc] as the target color. If the target color is already the same as the new color, return the image immediately to avoid an infinite loop. U
