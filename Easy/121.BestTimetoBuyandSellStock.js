//https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

var maxProfit = function (prices) {
  let [max, min] = [0, 0];
  for (let i = 0; i < prices.length; i++) {
	if (prices[i] < prices[min]) min = i;
	if (prices[i] - prices[min] > max) max = prices[i] - prices[min];
  }
  return max;
};

const testCases = [
  [[7, 1, 5, 3, 6, 4], 5],
  [[7, 6, 4, 3, 1], 0],
];

for (const test of testCases) {
  console.log(maxProfit(test[0]), "expected value = ", test[1]);
}
