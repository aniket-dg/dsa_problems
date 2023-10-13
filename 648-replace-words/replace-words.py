class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = sorted(dictionary)
        def find_root(word):
            for root in dictionary:
                if word.startswith(root):
                    return root
            return word

        modified_sentence = [find_root(word) for word in sentence.split()]
        return " ".join(modified_sentence)