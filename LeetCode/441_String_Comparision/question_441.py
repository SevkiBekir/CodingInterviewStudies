class Solution:
    def prepareCompressionList(self, chars: list[str]) -> dict[str, int]:
        compression_list = []
        previous_letter = ""
        current_list = None
        for letter in chars:
            if letter == previous_letter:
                current_list[1] +=1

            else:
                if current_list:
                    compression_list.append(current_list)

                current_list = [letter,1]
                previous_letter = letter

        compression_list.append(current_list)

        return compression_list
 

    def compress(self, chars: list[str]) -> int:
        input_list = chars.copy()
        compression_list = self.prepareCompressionList(input_list)
        chars.clear()

        for letter_list in compression_list:
            letter = letter_list[0]
            counter = letter_list[1]

            chars.append(letter)
            counter_str = str(counter)
            if counter > 9:
                for digit in counter_str:
                    chars.append(digit)
            elif len(input_list) == 1 or counter == 1: 
                continue
            else:
                chars.append(counter_str)

        return len(chars)

        
        

if __name__ == "__main__":
    solution = Solution()
    result = solution.compress(["a","a","b","b","c","c","c"])
    print(f"result: {result}")