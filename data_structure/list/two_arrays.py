class Solution:
    x = 5
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:

        return "".join(word1) == "".join(word2) 

word1 = ["a", "bc", "de", "f"]
word2 = ["ab", "c", "d", "ef"]

concat_array = Solution()
print(concat_array.arrayStringsAreEqual(word1=word1, word2=word2))