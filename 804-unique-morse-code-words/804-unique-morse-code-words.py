class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    
        res = set()
        for word in words:
            temp = ""
            for i in word:
                temp += code[ord(i)-ord('a')]
            res.add(temp)
        ans = len(res&res)
        res = set()
        return ans
