// https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

// var countCharacters = function (words, chars) {
//   const charsCounter = {};
//   let counter = 0;
//   for (const char of chars) {
//     charsCounter[char] = (charsCounter[char] || 0) + 1;
//   }

//   for (const word of words) {
//     let isValidWord = true;
//     const newCounter = { ...charsCounter };
//     for (const char of word) {
//       if (!newCounter[char] || newCounter[char] === 0) {
//         isValidWord = false;
//         break;
//       }
//       newCounter[char]--;
//     }
//     if (isValidWord) {
//       counter += word.length;
//     }
//   }

//   return counter;
// };

var countCharacters = function (words, chars) {
  const charsCounter = Array(26);
  let counter = 0;
  for (let i = 0; i < chars.length; i++) {
    charsCounter[chars.codePointAt(i) - 97] =
      (charsCounter[chars.codePointAt(i) - 97] || 0) + 1;
  }

  for (const word of words) {
    let isValidWord = true;
    const newCounter = [...charsCounter];

    for (let i = 0; i < word.length; i++) {
      if (
        !newCounter[word.codePointAt(i) - 97] ||
        newCounter[word.codePointAt(i) - 97] === 0
      ) {
        isValidWord = false;
        break;
      }
      newCounter[word.codePointAt(i) - 97]--;
    }

    if (isValidWord) {
      counter += word.length;
    }
  }

  return counter;
};
console.log(countCharacters(["cat", "bt", "hat", "tree"], "atach"));
