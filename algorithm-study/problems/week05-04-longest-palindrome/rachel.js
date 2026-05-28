/**
 * @param {string} s
 * @return {number}
 */
var longestPalindrome = function (s) {
  const map = new Map();

  for (let c of s) {
    if (!map.get(c)) {
      map.set(c, 1);
    } else {
      map.set(c, map.get(c) + 1);
    }
  }

  let length = 0;
  let hasOdd = false;
  for (let [char, count] of map) {
    length += Math.floor(count / 2) * 2;
    if (count % 2 === 1) hasOdd = true;
  }

  if (hasOdd) length += 1;

  return length;
};
