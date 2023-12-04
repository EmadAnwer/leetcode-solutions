// https://leetcode.com/problems/check-distances-between-same-letters/description/

/**
 * @param {string} s
 * @param {number[]} distance
 * @return {boolean}
 */
var checkDistances = function (s, distance) {
  for (let i = 0; i < s.length; i++) {
    if (distance[s.charCodeAt(i) - 97] !== -1) {
      if (s.indexOf(s[i], i + 1) - i - 1 !== distance[s.charCodeAt(i) - 97])
        return false;
      distance[s.charCodeAt(i) - 97] = -1;
    }
  }

  return true;
};
