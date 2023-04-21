class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        
        word_to_letter = {}
        letter_to_word = {}


        for i in range(len(pattern)):
            print(i)
            word = s[i]
            letter = pattern[i]
            
            print(word, letter, "anu")
            if word not in word_to_letter and letter not in letter_to_word:
                letter_to_word[letter] = word
                word_to_letter[word] = letter

            elif word in word_to_letter and letter in letter_to_word:
                if word_to_letter[word]!=letter or letter_to_word[letter] != word:
                    return False
            else:
                return False

        return True