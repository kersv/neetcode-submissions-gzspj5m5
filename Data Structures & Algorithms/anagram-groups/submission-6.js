class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const mapS = {}

        for(let word of strs){
            const key = word.split('').sort().join('')
            if(!mapS[key]){
                mapS[key] = []
            }
            mapS[key].push(word)
        }

        return Object.values(mapS)
    }
}
