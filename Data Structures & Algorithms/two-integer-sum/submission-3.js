class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {

        // for(let i = 0; i < nums.length -1; i++){
        //     for(let j = i+1; j < nums.length; j++){
        //         if(nums[i] + nums[j] === target){
        //             return [i,j]
        //         }
        //     }
        // }

        const map = new Map()

        for(let i = 0; i < nums.length; i++){
            // get value of current 
            const num = nums[i]
            // get difference 
            const diff = target - num
            // save index of difference if exist
            const diffIdx = map.get(diff)
            // if difference exist return the current index, diffIdx
            if(map.has(diff) === true){
                if (i < diffIdx) return [i, diffIdx] 
                else return [diffIdx, i]
            }
            map.set(nums[i], i)
        }
    }
}
