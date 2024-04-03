//https://leetcode.com/problems/valid-parentheses/description/

var isValid = function (s) {
  const stack = [];
  const parentheses = { "(": ")", "{": "}", "[": "]" };
  for (let i = 0; i < s.length; i++) {
    if (parentheses[s[i]]) {
      stack.push(parentheses[s[i]]);
    } else {
      if (stack.pop() !== s[i]) return false;
    }
  }
  return stack.length === 0;
};

const testCases = [
  ["()", true],
  ["()[]{}", true],
  ["(]", false],
  ["([)]", false],
  ["{[]}", true],
  ["", true],
  ["((", false],
];

for (const test of testCases) {
  console.log(isValid(test[0]), test[1]);
}
