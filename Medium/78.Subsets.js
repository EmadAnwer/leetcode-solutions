//https://leetcode.com/problems/subsets/

var subsets = function (nums) {
  const results = [[]];

  const helper = (arr, start) => {
    if (start === nums.length) return;
    for (let i = start; i < nums.length; i++) {
      results.push([...arr, nums[i]]);
      helper([...arr, nums[i]], i + 1);
    }
  };
};

console.log(subsets([1, 2, 3]));
