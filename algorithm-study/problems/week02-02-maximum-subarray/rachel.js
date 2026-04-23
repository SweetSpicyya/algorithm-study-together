/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function (nums) {
  let maxSum = nums[0];
  let currentSum = nums[0];

  for (let i = 1; i < nums.length; i++) {
    currentSum = Math.max(nums[i], currentSum + nums[i]);
    maxSum = Math.max(maxSum, currentSum);
  }
  return maxSum;
};

//Divide and Conquer
var maxSubArray = function (nums) {
  return findMaxSum(nums, 0, nums.length - 1);
};
function findMaxSum(nums, left, right) {
  if (left === right) return nums[left]; //only one element

  const mid = Math.floor((left + right) / 2);

  const leftMax = findMaxSum(nums, left, mid);
  const rightMax = findMaxSum(nums, mid + 1, right);
  const crossMax = findCrossMax(nums, left, mid, right);

  return Math.max(crossMax, rightMax, leftMax);
}

function findCrossMax(nums, left, mid, right) {
  let leftSum = -Infinity;
  let sum = 0;
  for (let i = mid; i >= left; i--) {
    sum += nums[i];
    leftSum = Math.max(leftSum, sum);
  }

  let rightSum = -Infinity;
  sum = 0;
  for (let i = mid; i <= right; i--) {
    sum += nums[i];
    rightSum = Math.max(rightSum, sum);
  }
  return leftSum + rightSum;
}
