/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
var updateMatrix = function (mat) {
  const rows = mat.length;
  const cols = mat[0].length;
  const queue = [];

  for (let r = 0; r < rows; r++) {
    for (let c = 0; c < cols; c++) {
      if (mat[r][c] === 0) {
        queue.push([r, c]);
      } else {
        mat[r][c] = Infinity;
      }
    }
  }

  const directions = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1],
  ];
  let head = 0;

  while (head < queue.length) {
    const [r, c] = queue[head++];

    for (const [dr, dc] of directions) {
      const nextR = r + dr;
      const nextC = c + dc;

      if (nextR >= 0 && nextR < rows && nextC >= 0 && nextC < cols) {
        if (mat[nextR][nextC] === Infinity) {
          mat[nextR][nextC] = mat[r][c] + 1;

          queue.push([nextR, nextC]);
        }
      }
    }
  }
  return mat;
};
