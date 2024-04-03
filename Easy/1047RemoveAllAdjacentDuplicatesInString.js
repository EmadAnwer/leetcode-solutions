//https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

var removeDuplicates = function (s) {
  const stack = [];

  for (let i = 0; i < s.length; i++) {
    if (s[i] !== stack[stack.length - 1]) {
      stack.push(s[i]);
    } else {
      stack.pop();
    }
  }

  return stack.join("");
};

testCases = [
  ["abbaca", "ca"],
  ["azxxzy", "ay"],
  ["aaaaaaaa", ""],
  ["aaaaaaaaa", "a"],
  ["aaaaaaaaaa", ""],
  ["aaaaaaaaaab", "b"],
  ["aaaaaaaaaabbbbbbbbbbb", ""],
];

for (const test of testCases) {
  console.log(removeDuplicates(test[0]), test[1]);
}
