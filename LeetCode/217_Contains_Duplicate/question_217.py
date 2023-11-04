class Solution:
    def prepareRepeatDict(self, nums: list[int]) -> any:
        repeat_dict = {}

        for num in nums:
            if num in repeat_dict:
                return True
            else:
                repeat_dict[num] = 1

        return False

    def containsDuplicate(self, nums: list[int]) -> bool:
        result = self.prepareRepeatDict(nums)
        return result



if __name__ == '__main__':
    solution = Solution()
    solution.containsDuplicate([1,2,3,1])
    solution.containsDuplicate([1,2,3,4])
    solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])