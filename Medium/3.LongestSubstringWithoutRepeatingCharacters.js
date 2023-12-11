//https://leetcode.com/problems/longest-substring-without-repeating-characters/
var lengthOfLongestSubstring = function (s) {
	if (s.length === 0) return 0;
	let [result, max] = [0, 0];
	const seen = new Set();
	let leftPointer = 0;
  
	for (let i = 0; i < s.length; i++) {
	  while (seen.has(s[i])) {
		seen.delete(s[leftPointer]);
		leftPointer++;
	  }
  
	  seen.add(s[i]);
	  result = i - leftPointer + 1;
  
	  if (result > max) {
		max = result;
	  }
	}
  
	return max;
  };

const testCases = [
  ["abcabcbb", 3],
  ["bbbbb", 1],
  ["pwwkew", 3],
  ["", 0],
  [" ", 1],
  ["dvdf", 3],
  ["abba", 2],
];

for (const test of testCases) {
  console.log(lengthOfLongestSubstring(test[0]), test[1]);
}
