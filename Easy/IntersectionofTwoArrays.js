//https://leetcode.com/problems/intersection-of-two-arrays/
var intersection = function (nums1, nums2) {
  const resultesSet = new Set();
  for (let i = 0; i < nums1.length; i++) {
    for (let j = 0; j < nums2.length; j++) {
      if (nums2[j] === nums1[i]) resultesSet.add(nums1[i]);
    }
  }

  return Array.from(resultesSet);
};

const testCases = [
  [
    [
      [1, 2, 2, 1],
      [2, 2],
    ],
    [2],
  ],
];

testCases.forEach((element) => {
  console.log(
    intersection(element[0][0], element[0][1]),
    "expected value = ",
    element[1]
  );
});
