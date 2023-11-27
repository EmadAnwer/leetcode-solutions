//https://leetcode.com/problems/single-number/description/

var singleNumber = function (nums) {
  if (nums.length === 1) return nums[0];

  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length; i += 2) {
    if (nums[i] !== nums[i + 1]) {
      return nums[i];
    }
  }
};

const testCases = [
  [[2, 2, 1], 1],
  [[4, 1, 2, 1, 2], 4],
  [[1], 1],
];

testCases.forEach((element) => {
  console.log(singleNumber(element[0]), "expected value = ", element[1]);
});
