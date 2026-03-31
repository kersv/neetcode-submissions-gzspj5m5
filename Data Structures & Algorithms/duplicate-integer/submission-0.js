class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // check if nums array is empty return false
        if (nums.length === 0) return false
        // nested for loop  to check value at i and every other value after return true if any matches
        for (let i = 0; i < nums.length-1; i++){
            for (let j = i+1; j < nums.length; j++){
                if(nums[i] === nums[j]){
                    return true
                }
            }
        }
        // end of loop return false
        return false
    }
}
