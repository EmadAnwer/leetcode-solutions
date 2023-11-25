//https://leetcode.com/problems/search-insert-position/

var searchInsert = function (nums, target) {
  let l = 0,
    r = nums.length - 1,
    m;

  while (l <= r) {
    m = Math.trunc((l + r) / 2);

    if (nums[m] === target) {
      return m;
    } else if (nums[m] < target) {
      l = m + 1;
    } else {
      r = m - 1;
    }
  }

  return l;
};

testCases = [
  [[1, 3, 5, 6], 5, 2],
  [[1, 3, 5, 6], 2, 1],
  [[1, 3, 5, 6], 7, 4],
  [[1, 3, 5, 6], 0, 0],
  [[1, 3, 5, 6], 2, 1],
  [[1], 0, 0],
];

testCases.forEach((element) => {
  console.log(
    searchInsert(element[0], element[1]),
    "expected value = ",
    element[2]
  );
});
