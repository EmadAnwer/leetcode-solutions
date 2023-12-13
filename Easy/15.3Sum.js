//https://leetcode.com/problems/3sum/description/

// var threeSum = function (nums) {
//   const resultSet = new Set();
//   for (let i = 0; i < nums.length; i++) {
//     for (let j = 0; j < nums.length; j++) {
//       if (j === i || j === i + 1 || i + 1 === nums.length) continue;
//       console.log(nums[i], nums[i + 1], nums[j]);
//       if (nums[i] + nums[i + 1] + nums[j] === 0) {
//         const result = [nums[i], nums[i + 1], nums[j]].sort((a, b) => a - b);
//         const resultString = result.join(',');
//         if (!resultSet.has(resultString)) resultSet.add(resultString);
//       }
//     }
//   }

//   return Array.from(resultSet, str => str.split(',').map(Number));
// };

// time: O(n^3) time limit exceeded
// var threeSum = function (nums) {
//   const resultSet = new Set();
//   const results = [];
//   for (let i = 0; i < nums.length; i++) {
//     for (let j = 0; j < nums.length; j++) {
//       if (j === i) continue;
//       for (let z = 0; z < nums.length; z++) {
//         if (z === i || z === j) continue;
//         if (nums[i] + nums[j] + nums[z] === 0) {
//           const result = [nums[i], nums[j], nums[z]].sort((a, b) => a - b);
//           const resultString = result.join(",");
//           if (!resultSet.has(resultString)) 
//           {
//             results.push(result);
//             resultSet.add(resultString);
//           }
          
//         }
//       }
//     }
//   }
//   return results;
// };

var threeSum = function (nums) {
  const results = [];

  // Sort the array
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    // Skip duplicates
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
      const sum = nums[i] + nums[left] + nums[right];

      if (sum === 0) {
        results.push([nums[i], nums[left], nums[right]]);

        // Skip duplicates
        while (left < right && nums[left] === nums[left + 1]) left++;
        while (left < right && nums[right] === nums[right - 1]) right--;

        left++;
        right--;
      } else if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }

  return results;
};
const testCases = [
  [
    [-1, 0, 1, 2, -1, -4],
    [
      [-1, -1, 2],
      [-1, 0, 1],
    ],
  ],
  // [[], []],
  // [[0], []],
];

for (const test of testCases) {
  console.log(threeSum(test[0]), "expected: ", test[1]);
}
