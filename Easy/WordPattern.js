var wordPattern = function (pattern, s) {
  const s_list = s.split(" ");

  if (pattern.length !== s_list.length) return false;

  const patternMap = new Map();
  for (let i = 0; i < pattern.length; i++) {
    if (patternMap.has(pattern[i])) {
      if (patternMap.get(pattern[i]) !== s_list[i]) {
        return false;
      }
    } else {
		for (const pv of patternMap.values()) {
			if (s_list[i] === pv)
			{
				return false
			}
		} 
      patternMap.set(pattern[i], s_list[i]);
    }
  }
  return true;
};

const testCases = [[["abba", "b a a b"], true]];

testCases.forEach((element) => {
  console.log(
    wordPattern(element[0][0], element[0][1]),
    "expected value = ",
    element[1]
  );
});
