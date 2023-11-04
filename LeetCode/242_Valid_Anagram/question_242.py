class Solution:
    def prepareLetterDict(self, s: str) -> dict:
        letter_dict = {}

        for letter in s:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1

        return letter_dict

    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = self.prepareLetterDict(s)
        t_dict = self.prepareLetterDict(t)

        if s_dict == t_dict:
            return True
        
        return False



if __name__ == '__main__':
    isAnagram = Solution().isAnagram("anagram", "nagaram")
    print(f'isAnagram = {isAnagram}')
    isAnagram = Solution().isAnagram("rat", "car")
    print(f'isAnagram = {isAnagram}')