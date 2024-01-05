//https://leetcode.com/problems/combinations/

var combine = function (n, k) {
  const combinations = [];

  const helper = (arr, start) => {
    if (arr.length === k) {
      combinations.push(arr);
      return;
    }
    for (let i = start; i <= n; i++) {
      helper([...arr, i], i + 1);
    }
  };
  helper([], 1);
  return combinations;
};

console.log(combine(4, 2));
console.log(combine(1, 1));
