//https://leetcode.com/problems/decode-string/description/

var decodeString = function (s) {
  function helpr(n, s) {
    console.log(n, s);
    let num = [];
    if (s.length === 0) return;
    for (let i = 0; i < s.length; i++) {
      if (!isNaN(s[i])) {
        num.push(s[i]);
      } else if (s[i] === '[') {
        helpr(num.join(''), s.slice(i + 1));
      } else {
        num = [];
      }
    }
    return s.repeat(n);
  }

  return helpr(1, s);
};

const testCases = [
  '3s23[a]2[bc]',
  //  '3[a2[c]]', '2[abc]3[cd]ef'
];

for (const test of testCases) {
  console.log(decodeString(test));
}
