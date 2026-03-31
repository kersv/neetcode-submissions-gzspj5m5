class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {

    //check if same length return false if not equal
    if (s.length !== t.length) return false
    //sort the two strings 
    const sortS = s.split('').sort().join('')
    const sortT = t.split('').sort().join('')
    // return true if both sorted strings equal
    return sortS === sortT
    }
}
