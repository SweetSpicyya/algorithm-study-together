/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  const stack = [];
  for (let p of s) {
    if (p === "(" || p === "{" || p === "[") {
      stack.push(p);
    } else {
      if (stack.length == 0) {
        return false;
      } else {
        let top = stack.pop();
        if (p === ")" && top !== "(") return false;
        if (p === "}" && top !== "{") return false;
        if (p === "]" && top !== "[") return false;
      }
    }
  }
  return stack.length === 0;
};

//Better way
var isValid = function (s) {
  const stack = [];
  const bracketMap = {
    //make the map with corresponding pairs
    "(": ")",
    "{": "}",
    "[": "]",
  };

  for (let char of s) {
    if (bracketMap[char]) {
      stack.push(char);
    } else {
      const lastOpen = stack.pop();

      if (bracketMap[lastOpen] !== char) {
        return false;
      }
    }
  }

  return stack.length === 0;
};
