class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        // BRUTE FORCE
        // // check if nums array is empty return false
        // if (nums.length === 0) return false
        // // nested for loop  to check value at i and every other value after return true if any matches
        // for (let i = 0; i < nums.length-1; i++){
        //     for (let j = i+1; j < nums.length; j++){
        //         if(nums[i] === nums[j]){
        //             return true
        //         }
        //     }
        // }
        // // end of loop return false
        // return false

        // hashmap
        // edge case if lengt is 0 return false
        if (nums.length === 0) return false
        // create map
        const map = new Map();
        // check for value if exist return true else add 1
        for(const num of nums){
            if(map.has(num)){
                return true
            }
            else{
                map.set(num, 1)
            }
        }
        // when loop finish return false
        return false

    }
}
