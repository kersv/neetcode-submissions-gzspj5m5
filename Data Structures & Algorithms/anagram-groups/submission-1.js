class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {

        const res = {}

        for(let i = 0; i < strs.length; i++){
            const key = strs[i].split('').sort().join('')
            if(!res[key]){
                res[key] = []
            }
            res[key].push(strs[i])
            
        }

        return Object.values(res)

    }
}
