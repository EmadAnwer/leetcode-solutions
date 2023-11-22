//https://leetcode.com/problems/crawler-log-folder/description/

var minOperations = function (logs) {
  let count = 0;

  for (let i = 0; i < logs.length; i++) {
    if (logs[i] === "../") {
      if (count > 0) count--;
    } else if (logs[i] !== "./") {
      count++;
    }
  }
  return count;
};

const testCases = [
  [["d1/", "d2/", "../", "d21/", "./"], 2],
  [["d1/", "d2/", "./", "d3/", "../", "d31/"], 3],
  [["d1/", "../", "d1/", "../", "d1/", "../"], 0],
  [["d1/", "../", "../", "../"], 0],
  [["d1/"], 1],
  [["./"], 0],
  [["../"], 0],
];

testCases.forEach((element) => {
  console.log(minOperations(element[0]), "expected value = ", element[1]);
});
