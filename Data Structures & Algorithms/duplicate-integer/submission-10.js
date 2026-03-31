class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let hashmap = {}

        for(let i = 0; i < nums.length; i++){
            hashmap[nums[i]] = hashmap[nums[i]] ? hashmap[nums[i]] + 1 : 1
        }

        for(let key in hashmap){
            if(hashmap[key] > 1){
                return true
            }
        }
        return false

    }
}
