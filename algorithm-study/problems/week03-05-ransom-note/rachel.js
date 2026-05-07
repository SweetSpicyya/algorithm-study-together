/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
var canConstruct = function (ransomNote, magazine) {
  let map = new Map();
  for (let m of magazine) {
    map[m] = (map[m] || 0) + 1;
  }

  for (let r of ransomNote) {
    if (map[r]) {
      map[r] -= 1;
    } else {
      return false;
    }
  }
  return true;
};
