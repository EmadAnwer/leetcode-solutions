// https://leetcode.com/problems/keyboard-row/description/

var findWords = function (words) {
  const output = [];
  const rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"];

  for (const word of words) {
    for (const row of rows) {
      let isValid = true;
      for (const letter of word) {
        if (!row.includes(letter.toLowerCase())) {
          isValid = false;
          break;
        }
      }
      if (!isValid) {
        continue;
      } else {
        output.push(word);
        break;
      }
    }
  }

  return output;
};

const testCases = [
  [
    ["Hello", "Alaska", "Dad", "Peace"],
    ["Alaska", "Dad"],
  ],
  [["omk"], []],
  [
    ["adsdf", "sfd"],
    ["adsdf", "sfd"],
  ],
];

testCases.forEach((element) => {
  console.log(findWords(element[0]), "expected value = ", element[1]);
});
