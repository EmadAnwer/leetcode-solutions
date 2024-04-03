//https://leetcode.com/problems/first-bad-version/description/

var solution = function (isBadVersion) {
  /**
   * @param {integer} n Total versions
   * @return {integer} The first bad version
   */
  return function (n) {
    // Binary search
    let left = 1;
    let right = n;
    while (left < right) {
      const mid = Math.floor((left + right) / 2);
      if (isBadVersion(mid)) right = mid;
      else left = mid + 1;
    }
    return left;
  };
};

const testcases = [
  [5, 4],
  [1, 1],
];

const expected = [4, 1];

testcases.forEach((testcase, index) => {
  const actual = solution(...testcase);
  console.log(`Testcase ${index + 1}: ${actual}`);
  console.assert(actual === expected[index], "Wrong answer");
});
