//https://leetcode.com/problems/sort-colors/description/

var sortColors = function (nums) {
  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length - 1; j++) {
      if (nums[j] > nums[j + 1]) {
        [nums[j], nums[j + 1]] = [nums[j + 1], nums[j]];
      }
    }
  }
  return nums;
};

nums = [2, 0, 2, 1, 1, 0];

console.log(sortColors(nums));
