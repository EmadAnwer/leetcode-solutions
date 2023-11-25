//https://leetcode.com/problems/n-th-tribonacci-number/description/

// 1137. N-th Tribonacci Number

var tribonacci = function (n) {
  if (n === 0) return 0;
  if (n === 1 || n === 2) return 1;
  if (n === 3) return 2;
  
  //tribonacci 1 to 3
  let [t1, t2, t3] = [1, 1, 2];

  n = n - 3;
  while (n--) {
    [t1, t2, t3] = [t2, t3, t1 + t2 + t3];
  }

  return t3;
};

const testCases = [
  [0, 0],
  [1, 1],
  [2, 1],
  [3, 2],
  [4, 4],
  [25, 1389537],
];

testCases.forEach((element) => {
  console.log(tribonacci(element[0]), "expected value = ", element[1]);
});
