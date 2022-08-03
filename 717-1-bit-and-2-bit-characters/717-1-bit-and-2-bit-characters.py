class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        flag = False
        i = 0
        while i < len(bits):
            if i == len(bits)-1:
                flag = True
            if bits[i] == 1:
                i += 1
            i += 1
        return flag
            