//https://leetcode.com/problems/baseball-game/description/

var calPoints = function (operations) {
  const stack = [];

  for (let i = 0; i < operations.length; i++) {
    if (operations[i] === "+") {
      stack.push(+stack[stack.length - 1] + +stack[stack.length - 2]);
    } else if (operations[i] === "D") {
      stack.push(+stack[stack.length - 1] * 2);
    } else if (operations[i] === "C") {
      stack.pop();
    } else {
      stack.push(+operations[i]);
    }
  }

  let sum = 0;

  stack.forEach((n) => {
    sum += n;
  });

  return sum;
};

const testCases = [
  [["1"], 1],
  [["1", "C"], 0],
  [["5", "-2", "4", "C", "D", "9", "+", "+"], 27],
  [["5", "2", "C", "D", "+"], 30],
];

testCases.forEach((element) => {
  testCases.length;
  console.log(calPoints(element[0]), "expected value = ", element[1]);
});
