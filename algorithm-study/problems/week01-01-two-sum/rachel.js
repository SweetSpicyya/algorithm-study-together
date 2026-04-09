/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    let n = nums[i];
    let sub = target - n;
    let subIndex = nums.indexOf(sub, i + 1);
    if (subIndex !== -1) {
      return [i, subIndex];
    }
  }
};

//Better way:
function betterTwoSum(nums, target) {
  const map = new Map();

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const complement = target - num;
    if (map.has(complement)) {
      return [map.get(complement), i];
    }
    map.set(num, i);
    //If we populate the entire map first, we might accidentally pick the same element twice.
  }
}
