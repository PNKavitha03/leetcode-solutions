class Solution:
    def checkIfPangram(self, sentence):
        return len(set(sentence)) == 26

sentence = "thequickbrownfoxjumpsoverthelazydog"
obj = Solution()
print(obj.checkIfPangram(sentence))
