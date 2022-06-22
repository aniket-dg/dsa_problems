class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        curr = 1
        # preorder = preorder.split(",")
        for item in preorder.split(","):
            if curr == 0:
                return False
            if item == "#":
                curr -= 1
            
            else:
                curr += 1
        return curr == 0