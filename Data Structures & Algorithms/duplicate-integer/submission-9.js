class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        if(nums.length == 0){
            return false
        }
        nums.sort((a,b) => a-b)
        for(let i = 0; i < nums.length; i++){
            let j = i+1;
            if(nums[i] == nums[j]){
                return true
            }
        }
        return false 
    }
}
