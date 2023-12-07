//https://leetcode.com/problems/valid-palindrome/description/

var isPalindrome = function (s) {
  if (s.length === 0 || s.length === 1) return true;
  let [i, j] = [0, s.length - 1];
  s = s.toLowerCase();
  while (i <= j) {
    while (i < s.length) {
      if (
        (s.codePointAt(i) >= 97 && s.codePointAt(i) <= 122) ||
        (s.codePointAt(i) >= 48 && s.codePointAt(i) <= 57)
      ) {
        break;
      }
      i++;
    }

    while (j >= 0) {
      if (
        (s.codePointAt(j) >= 97 && s.codePointAt(j) <= 122) ||
        (s.codePointAt(j) >= 48 && s.codePointAt(j) <= 57)
      ) {
        break;
      }
      j--;
    }

    if (s[i] !== s[j]) return false;

    i++;
    j--;
  }
  return true;
};

const testCases = [
  ["A man, a plan, a canal: Panama", true],
  ["race a car", false],
  [".,", true],
  ["0P", false],
];

testCases.forEach(([input, output]) => {
  console.log("input", input);
  console.log("output", output);
  console.log(isPalindrome(input) === output ? "pass" : "fail");
  console.log("------------");
});
