/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function (numCourses, prerequisites) {
  const graph = [];
  for (let i = 0; i < numCourses; i++) {
    graph.push([]); //graph = [[], [] ...]
  }
  for (let [a, b] of prerequisites) {
    //prerequisites = [[1,0]]
    graph[b].push(a); //graph[0] =[1]
  }

  const state = new Array(numCourses).fill(0);

  function dfs(course) {
    if (state[course] === 1) return false; //state[0] = 0; state[1] = 0;
    if (state[course] === 2) return true; //state[0] = 0; state[1] = 0;

    state[course] = 1; //state[0] = 1; state[1] = 1;

    for (let next of graph[course]) {
      if (!dfs(next)) return false; //graph[0] = [1]; graph[1] = [];
    }

    state[course] = 2; //state[1] = 2;
    return true;
  }
  for (let i = 0; i < numCourses; i++) {
    if (!dfs(i)) return false;
  }
  return true;
};
