class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i,item in enumerate(image):
            item = [1 if not i else 0 for i in item[::-1]]
            image[i] = item
        return image
            