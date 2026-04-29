/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function (points, k) {
  points.sort((a, b) => {
    const distanceA = a[0] * a[0] + a[1] * a[1];
    const distanceB = b[0] * b[0] + b[1] * b[1];
    return distanceA - distanceB;
  });
  return points.slice(0, k);
};
