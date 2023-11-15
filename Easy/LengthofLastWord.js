// https://leetcode.com/problems/length-of-last-word/

const isalphabet = (l) => {
  return (l >= "a" && l <= "z") || (l >= "A" && l <= "Z");
};
var lengthOfLastWord = function (s) {
  let laswWordLen = 0;
  for (let index = s.length - 1; index >= 0; index--) {
    if (isalphabet(s[index])) {
      laswWordLen++;
    } else if (laswWordLen === 0) {
      continue;
    } else {
      break;
    }
  }
  return laswWordLen;
};

const testCases = [
  ["Hello World", 5],
  ["   fly me   to   the moon  ", 4],
  ["luffy is still joyboy", 6],
  ["", 0],
  ["                          ", 0],
  ["Emad", 4],
];

testCases.forEach((element) => {
  console.log(lengthOfLastWord(element[0]), "expected value = ", element[1]);
});
