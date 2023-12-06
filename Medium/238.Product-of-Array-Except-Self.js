//https://leetcode.com/problems/product-of-array-except-self/description/

var productExceptSelf = function (nums) {
  const resultValues = {};
  const result = [];
  for (let i = 0; i < nums.length; i++) {
    if (resultValues[nums[i]]) {
      result.push(resultValues[nums[i]]);
      continue;
    }
    result.push(nums.reduce((a, b, index) => (index !== i ? a * b : a), 1));

    resultValues[nums[i]] = result[i];
  }

  return result;
};

const testCases = [
  [
    [1, 2, 3, 4],
    [24, 12, 8, 6],
  ],
  [
    [-1, 1, 0, -3, 3],
    [0, 0, 9, 0, 0],
  ],
  [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [
      3628800, 1814400, 1209600, 907200, 725760, 604800, 518400, 453600, 403200,
      362880,
    ],
  ],
];

for (const test of testCases) {
  console.log(productExceptSelf(test[0]), "expected: ", test[1]);
}
