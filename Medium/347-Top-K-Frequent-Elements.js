//https://leetcode.com/problems/top-k-frequent-elements/description/
var topKFrequent = function (nums, k) {
  if (nums.length === 1) return nums;

  nums.sort((a, b) => a - b);
  const x = [];
  

  for (let i = 0; i < nums.length; i++) {
    frequentNums[nums[i]] = (frequentNums[nums[i]] || 0) + 1;
  }
  
  
  console.log(frequentNums);
  return [];
};

const testCases = [
  [[1, 1, 1, 2, 2, 3,3,3,3,3], 2],
  [[1], 1],
];

for (const test of testCases) {
  console.log(topKFrequent(test[0], test[1]));
}
