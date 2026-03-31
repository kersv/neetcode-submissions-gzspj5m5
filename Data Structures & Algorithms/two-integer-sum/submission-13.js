class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const idxMap = {}

        for(let i = 0; i < nums.length; i++){
            let diff = target - nums[i] 
            if(diff in idxMap) {
                return [i,idxMap[diff]]
            }
            idxMap[nums[i]] = i
            
        }
    }
}
