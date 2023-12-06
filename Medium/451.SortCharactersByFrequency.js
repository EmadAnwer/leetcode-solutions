//https://leetcode.com/problems/sort-characters-by-frequency/description/

var frequencySort = function (s) {
  const uperLowerDigits = new Array(75).fill([0, 0]);

  for (let i = 0; i < s.length; i++) {
    console.log(s[i]);
    uperLowerDigits[s.charCodeAt(i) - 48] = [
      s[i],
      uperLowerDigits[s.charCodeAt(i) - 48][1] + 1,
    ];
  }

  uperLowerDigits.sort((a, b) => b[1] - a[1]);

  let result = [];

  for (let i = 0; i < uperLowerDigits.length; i++) {
    if (uperLowerDigits[i][1] === 0) break;
    result.push(uperLowerDigits[i][0].repeat(uperLowerDigits[i][1]));
  }

  return result.join("");
};

const testCases = [
  ["tree", "eert"],
  ["cccaaa", "cccaaa"],
  ["Aabb", "bbAa"],
  ["", ""],
  ["2a554442f544asfasssffffasss", "sssssssffffff44444aaaa55522"],
];

for (const test of testCases) {
  console.log(frequencySort(test[0]), "expected: ", test[1]);
}
