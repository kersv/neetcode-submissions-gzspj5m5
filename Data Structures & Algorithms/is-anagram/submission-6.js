class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if(s.length !== t.length){
            return false
        }

        let mapS = {}
        
        for (let i = 0; i < s.length; i++){
            mapS[s[i]] = (mapS[s[i]] || 0) +1
            mapS[t[i]] = (mapS[t[i]] || 0) -1
        }

        for(let key in mapS){
            if (mapS[key] !== 0) return false
        }
        return true
    }
}
