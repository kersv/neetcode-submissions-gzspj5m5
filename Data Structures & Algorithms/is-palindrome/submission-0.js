class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const m = s.toLowerCase().replace(/[^a-z0-9]/g, '');
        // 2 pointers starting at 0 and end of string
        let leftPoint = 0
        let rightPoint = m.length - 1

        // loop through until leftpointer is greater than rightpointer 
        while(leftPoint <= rightPoint){
            // check if current position is a character otherwise move pointer
            if (m[leftPoint] !== m[rightPoint]){
                console.log(m[leftPoint], m[rightPoint])
                return false
            }
            // move pointers
            leftPoint++
            rightPoint--

        }
        return true
    }
}
