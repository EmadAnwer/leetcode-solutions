//https://leetcode.com/problems/longest-repeating-character-replacement/description/

// bad understanding of the problem
// var characterReplacement = function (s, k) {
// 	if (s.length === 1) return 1;
//   const arrayofChars = Array(26).fill(0);
//   for (let i = 0; i < s.length; i++) {
// 	console.log(s.charCodeAt(i) - 65);
//     arrayofChars[s.charCodeAt(i) - 65]++;
//   }
//   console.log(arrayofChars);
//   arrayofChars.sort((a, b) => b - a);

//   return arrayofChars[0] + k > s.length ? s.length : arrayofChars[0] + k;
// };

var characterReplacement = function (s, k) {
  const count = {}
  let result = 0
  let l = 0

  for (let r = 0; r < s.length; r++) {
    count[s[r]] = (count[s[r]] || 0) + 1
    while (r - l + 1 - Math.max(...Object.values(count)) > k) {
      count[s[l]]--
      l++
    }
    result = Math.max(result, r - l + 1)
  }

  return result
};
const testCases = [
  //   ["ABAB", 2, 4],
  //   ["AABABBA", 1, 4],
  //   ["AABA", 0, 2],
  //   ["AABBBBA", 1, 5],
  ["AABABBA", 1, 4],
  //   ["i", 0, 1],
];

for (const test of testCases) {
  console.log(characterReplacement(test[0], test[1]), test[2]);
}
