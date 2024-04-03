//https://leetcode.com/problems/generate-parentheses/description/

// var generateParenthesis = function (n) {
//   if (n === 0) return [];
//   if (n === 1) return ["()"];
//   let result = [];
//   function isValid(s) {
//     let stack = [];
//     for (let i = 0; i < s.length; i++) {
//       if (s[i] === "(") stack.push("(");
//       else {
//         if (stack.length === 0) return false;
//         stack.pop();
//       }
//     }
//     return stack.length === 0;
//   }

//   function generate(s) {
//     if (s.length === n * 2) {
//       if (isValid(s)) result.push(s);
//       return;
//     }
//     generate(s + "(");
//     generate(s + ")");
//   }

//   generate("");
//   return result;
// };

var generateParenthesis = function(n) {
  let res=[]
  recur('', 0, 0)
  return res
  function recur(curr, open, close){
      if(curr.length==n*2)
          res.push(curr)
      if(open<n)
          recur(curr+'(', open+1, close)
      if(close < open)
          recur(curr+')', open, close+1)
  }
};
console.log(generateParenthesis(3));
