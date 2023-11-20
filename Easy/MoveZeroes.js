// https://leetcode.com/problems/move-zeroes/

var moveZeroes = function (nums) {
  let l = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      [nums[i], nums[l]] = [nums[l], nums[i]];
      l++;
    }
  }
};

const testCases = [
  [
    [0, 1],
    [1, 0],
  ],
  [
    [0, 1, 0, 3, 12],
    [1, 3, 12, 0, 0],
  ],
];

testCases.forEach((element) => {
  moveZeroes(element[0]);
  console.log(element[0], "expected value = ", element[1]);
});
