// https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

function isPalindrome(word) {
  for (let i = 0; i < word.length - 1 / 2; i++) {
    if (word[i] !== word[word.length - 1 - i]) return false;
  }

  return true;
}

var firstPalindrome = function (words) {
  for (const word of words) {
    if (isPalindrome(word)) {
      return word;
    }
  }

  return "";
};

const testCases = [[["abc", "car", "ada", "racecar", "cool"], "ada"]];

testCases.forEach((element) => {
  console.log(firstPalindrome(element[0]), "expected value = ", element[1]);
});
