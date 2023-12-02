//https://leetcode.com/problems/valid-anagram/description/

var isAnagram = function (s, t) {
  if (s.length !== t.length) return false;

  sObj = {};

  for (const char of s) {
    sObj[char] = (sObj[char] || 0) + 1;
  }

  for (const char of t) {
    if (!sObj[char] || sObj[char] - 1 === -1) return false;

    sObj[char]--;
  }

  return true;
};

// var isAnagram = function (s, t) {
// 	if (s.length !== t.length) return false;

// 	const sortedS = s.split('').sort().join('');
// 	const sortedT = t.split('').sort().join('');

// 	return sortedS === sortedT;
//   };
// wrong "bb"  ""
// var isAnagram = function (s, t) {
//   if (s.length !== t.length) return false;

//   let sTotalASCIIValues = 0;
//   for (let i = 0; i < s.length; i++) {
//     sTotalASCIIValues += s.codePointAt(i);
//   }

//   let tTotalASCIIValues = 0;
//   for (let i = 0; i < t.length; i++) {
//     tTotalASCIIValues += t.codePointAt(i);
//   }

//   return sTotalASCIIValues === tTotalASCIIValues;
// };

const testCases = [
  [["anagram", "nagaram"], true],
  [["rat", "car"], false],
  [["a", "ab"], false],
  [["a", "a"], true],
  [["", ""], true],
  [["a", ""], false],
  [["", "a"], false],
];

testCases.forEach((element) => {
  console.log(
    isAnagram(element[0][0], element[0][1]),
    "expected value = ",
    element[1]
  );
});
