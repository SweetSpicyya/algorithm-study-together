/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let start = 0;
  let end = 0;
  let map = {};
  let max = 0;

  for (let end = 0; end < s.length; end++) {
    let curr = s[end];

    if (map[curr] >= start) {
      start = map[curr] + 1;
    }

    map[curr] = end;
    max = Math.max(max, end - start + 1);
  }
  return max;
};
