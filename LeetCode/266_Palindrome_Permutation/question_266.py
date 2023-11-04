
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        palindrome_dict = {}

        while start <= end:
            if s[start] in palindrome_dict:
                palindrome_dict[s[start]] += 1
            else:
                palindrome_dict[s[start]] = 1

            if s[end] in palindrome_dict:
                palindrome_dict[s[end]] += 1
            else:
                palindrome_dict[s[end]] = 1

            start += 1
            end -= 1

        odd_count = 0
        for key, value in palindrome_dict.items():
            if value % 2 == 1:
                odd_count += 1

        if odd_count > 1:
            return False
        
        return True



if __name__ == '__main__':
    result = Solution().canPermutePalindrome("code")
    print(f'result = {result}')
    result = Solution().canPermutePalindrome("aab")
    print(f'result = {result}')
    result = Solution().canPermutePalindrome("carerac")
    print(f'result = {result}')
