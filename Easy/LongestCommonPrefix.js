// https://leetcode.com/problems/longest-common-prefix/

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function (strs) {
  let longCommonPrfx = strs[0];

  for (let i = 0; i < strs.length; i++) {
    if (strs[i].startsWith(longCommonPrfx)) {
      continue;
    } else {
      i = 0;
      longCommonPrfx = longCommonPrfx.slice(0, -1);
      if (longCommonPrfx === "") {
        return "";
      }
    }
  }

  return longCommonPrfx;
};

const testCases = [
  [["flower", "flow", "flight"], "fl"],
  [["puppy", "pup", "puppie"], "pup"],
  [["man", "man", "man"], "man"],
  [["dog", "racecar", "car"], ""],
  [["man", "fan", "can"], ""],
  [["boy"], "boy"],
];

testCases.forEach((element) => {
  console.log(longestCommonPrefix(element[0]), "expected value = ", element[1]);
});
