// https://leetcode.com/problems/isomorphic-strings/
var isIsomorphic = function (s, t) {
  for (let i = 0; i < s.length; i++) {
    if (t.indexOf(t[i]) !== s.indexOf(s[i])) return false;
  }
  return true;
};

const testCases = [[["badc", "baba"], false]];

testCases.forEach((element) => {
  console.log(
    isIsomorphic(element[0][0], element[0][1]),
    "expected value = ",
    element[1]
  );
});
