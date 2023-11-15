var mergeAlternately = function (word1, word2) {
  let margedString = "";

  if (word1 === "" || word2 === "") {
    return word1 + word2;
  }

  for (let i = 0; true; i++) {
    if (!word1[i] && !word2[i]) {
      return margedString;
    } else if (!word1[i]) {
      return margedString + word2.slice(i);
    } else if (!word2[i]) {
      return margedString + word1.slice(i);
    }
    margedString += word1[i] + word2[i];
  }
};

const testCases = [[["emad", "ali"], "eamlaid"]];

testCases.forEach((element) => {
  console.log(
    mergeAlternately(element[0][0], element[0][1]),
    "expected value = ",
    element[1]
  );
});
