//https://leetcode.com/problems/license-key-formatting/

var licenseKeyFormatting = function (s, k) {
  const upperCaseWithoutDash = s.replace(/-/g, "").toUpperCase().split("");

  const upperCaseWithDash = [];
  let nextDash = k;
  if (upperCaseWithoutDash.length % k !== 0) {
    nextDash = upperCaseWithoutDash.length % k;
  }

  for (let i = 0; i < upperCaseWithoutDash.length; i++) {
    if (nextDash == 0) {
      upperCaseWithDash.push("-");
      nextDash = k;
    }
    upperCaseWithDash.push(upperCaseWithoutDash[i]);
    nextDash--;
  }

  return upperCaseWithDash.join("");
};

const testCases = [
  [{ s: "2-4A0r7-4k", k: 3 }, "24-A0R-74K"],
  [{ s: "2-4A0r7-4k", k: 4 }, "24A0-R74K"],
  [{ s: "a-a-a-a-", k: 1 }, "A-A-A-A"],
];

testCases.forEach((element) => {
  const x = licenseKeyFormatting(element[0].s, element[0].k);
  console.log(x, "expected value = ", element[1], x === element[1]);
});
