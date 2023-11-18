//https://leetcode.com/problems/missing-number/
var missingNumber = function (nums) {
  let sumOfnums = 0;

  nums.forEach((n) => (sumOfnums += n));
  return (nums.length * (1 + nums.length)) / 2 - sumOfnums;
};

const testCases = [
  [[3, 0, 1], 2],
  [[0, 1], 2],
  [[9, 6, 4, 2, 3, 5, 7, 0, 1], 8],
  [[0], 1],
];

testCases.forEach((element) => {
  console.log(missingNumber(element[0]), "expected value = ", element[1]);
});
