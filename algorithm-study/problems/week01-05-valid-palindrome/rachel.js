/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  let arr = s.toLowerCase().match(/[a-z0-9]/g);
  if (!arr) return true;
  for (let i = 0; i < arr.length / 2; i++) {
    let fp = arr[i];
    let lp = arr[arr.length - 1 - i];

    if (fp !== lp) {
      return false;
    }
  }
  return true;
};

// Better way
var isPalindrome2 = function (s) {
  const chars = s.toLowerCase().match([/a-z0-9/g]) || [];
  const original = chars.join("");
  const reversed = chars.reverse().join("");

  return original === reversed;
};
