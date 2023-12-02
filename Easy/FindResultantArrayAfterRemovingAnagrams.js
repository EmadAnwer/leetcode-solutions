//https://leetcode.com/problems/valid-anagram/description/

// var isAnagram = function (s, t) {
//   if (s.length !== t.length) return false;

//   sObj = {};

//   for (const char of s) {
//     sObj[char] = (sObj[char] || 0) + 1;
//   }

//   for (const char of t) {
//     if (!sObj[char] || sObj[char] - 1 === -1) return false;

//     sObj[char]--;
//   }

//   return true;
// };

// var removeAnagrams = function (words) {
//   const uniqueWords = [];
//   uniqueWords.push(words[0]);
//   let word = words[0];
//   for (let i = 1; i < words.length; i++) {
//     if (!isAnagram(word, words[i])) {
//       uniqueWords.push(words[i]);
//       word = words[i];
//     }
//   }
//   return uniqueWords;
// };

var removeAnagrams = function (words) {
  let i = 1;
  let currentWord = words[0].split("").sort().join("");

  while (words[i]) {
    let newWord = words[i].split("").sort().join("");
    if (currentWord === newWord) words.splice(i, 1);
    else {
      currentWord = newWord;
      i++;
    }
  }
  return words;
};
const testCases = [
  [
    ["abba", "baba", "bbaa", "cd", "cd"],
    ["abba", "cd"],
  ],
  [
    ["a", "b", "c", "d", "e"],
    ["a", "b", "c", "d", "e"],
  ],
  [
    ["a", "b", "a"],
    ["a", "b", "a"],
  ],
];

testCases.forEach((element) => {
  console.log(removeAnagrams(element[0]), "expected value = ", element[1]);
});
