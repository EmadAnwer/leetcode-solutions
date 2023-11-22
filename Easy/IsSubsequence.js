//https://leetcode.com/problems/is-subsequence/description/

var isSubsequence = function (s, t) {
  if (s.length > t.length) return false;
  if (s === "") return true;
  if (s !== "" && t === "") return false;
  let j = 0;
  for (let i = 0; i < t.length; i++) {
    if (t[i] === s[j]) {
      j++;
      if (j === s.length) return true;
    }
  }
  return false;
};

const testCases = [
  [{ s: "abc", t: "ahbgdc" }, true],
  [{ s: "axc", t: "ahbgdc" }, false],
  [{ s: "", t: "" }, true],
  [{ s: "", t: "ahbgdc" }, true],
  [{ s: "abc", t: "" }, false],
  [{ s: "aaaaaa", t: "bbaaaa" }, false],
  [{ s: "acb", t: "ahbgdc" }, false],
];

testCases.forEach((element) => {
  const x = isSubsequence(element[0].s, element[0].t);
  console.log(x, "expected value = ", element[1]);
});
