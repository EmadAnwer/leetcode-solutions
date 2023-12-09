//https://leetcode.com/problems/find-the-duplicate-number/description/

var findDuplicate = function (nums) {
  const array = Array(nums.length).fill(0);

  for (let i = 0; i < nums.length; i++) {
    array[nums[i]]++;
    if (array[nums[i]] > 1) return nums[i];
  }
};

const testCases = [
  [1, 3, 4, 2, 2],
  [3, 1, 3, 4, 2],
  [1, 1],
  [1, 1, 2],
  [2, 2, 2, 2, 2],
];

for (const test of testCases) {
  console.log(findDuplicate(test));
}
