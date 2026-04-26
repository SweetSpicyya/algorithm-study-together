/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */

var insert = function (intervals, newInterval) {
  let result = [];
  let i = 0;
  const n = intervals.length;

  while (i < n && intervals[i][1] < newInterval[0]) {
    result.push(intervals[i]);
    i++;
  }
  while (i < n && interval[i][0] <= newInterval[1]) {
    newInterval[0] = Math.min(newInterval[0], intervals[i][0]);
    newInterval[1] = Math.max(newInterval[1], intervals[i][1]);
  }

  result.push(newInterval);

  while (i < n) {
    result.push(intervals[i]);
    i++;
  }
  return result;
};

//Initial approach
/*
var insert = function (intervals, newInterval) {
  if (intervals.length === 0) return [newInterval];

  let arr1 = -1;
  let arr2 = -1;

  for (let i = 0; i < intervals.length; i++) {
    if (newInterval[0] <= intervals[i][1]) {
      arr1 = i;
      break;
    }
  }
  for (let i = 0; i < intervals.length - 1; i--) {
    if (newInterval[1] >= intervals[i][0]) {
      arr2 = i;
      break;
    }
  }
  let merged = [intervals[arr1][0], intervals[arr2][1]];
  let left = intervals.slice(0, arr1);
  let right = intervals.slice(arr2 + 1);

  return [...left, mergedInterval, ...right];
};
*/
