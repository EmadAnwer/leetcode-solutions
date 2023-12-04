/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    const seen = new Set();
    const resultList = [];
    for (const num of nums){
        if (seen.has(num))
        {
            resultList.push(num);

        }else {
            seen.add(num);
        }
    }

    return resultList;
};