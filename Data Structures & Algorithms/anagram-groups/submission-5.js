class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const mapS = {}

        for(let i = 0; i < strs.length; i++){

            const key = strs[i].split("").sort().join("")
            if(!mapS[key]){
                mapS[key] = []
            }
            mapS[key].push(strs[i])
        }
        return Object.values(mapS)
    }
}
