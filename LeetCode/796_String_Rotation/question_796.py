class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True
        
        s_len = len(s)
        for i in range(s_len):
            s = s[-1] + s[:-1]
            if s == goal:
                return True
            
        return False


        

if __name__ == "__main__":
    solution = Solution()
    result = solution.rotateString("abcde", "cdeab")
   
