//https://leetcode.com/problems/roman-to-integer/description/

var romanToInt = function (s) {
  const intRepresentations = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  let intNum = 0;
  for (let i = 0; i < s.length; i++) {
    if (intRepresentations[s[i]] < intRepresentations[s[i + 1]])
      intNum -= intRepresentations[s[i]];
    else intNum += intRepresentations[s[i]];
  }
  return intNum;
};

const testCases = [
  [["III"], 3],
  [["LVIII"], 58],
  [["MCMXCIV"], 1994],
];

testCases.forEach((element) => {
  console.log(
    romanToInt(element[0][0], element[0][1]),
    "expected value = ",
    element[1]
  );
});
