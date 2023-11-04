class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s == t: return False
        
        min_len = min(len(s),len(t))

        for i in range(min_len):
            if s[i] == t[i]:
                i += 1
            else:
                break
        next_s = s[i+1:]
        next_t = t[i+1:]
        sub_s = s[i:]
        sub_t = t[i:]

        is_equal_next_suffix = next_s == next_t
        is_t_ends_with_s = sub_s == next_t
        is_s_ends_with_t = next_s == sub_t
        return is_equal_next_suffix or is_t_ends_with_s or is_s_ends_with_t

if __name__ == "__main__":
    solution = Solution()
    result = solution.isOneEditDistance("ab", "acb")
    result = solution.isOneEditDistance("abc", "ac")
    result = solution.isOneEditDistance("acbbcda", "abbdad")
    result = solution.isOneEditDistance("aca", "caca")
    result = solution.isOneEditDistance("123", "1423")
    print(f"result: {result}")