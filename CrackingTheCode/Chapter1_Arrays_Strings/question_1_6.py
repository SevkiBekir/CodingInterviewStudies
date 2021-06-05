def compress(text):
    result = text[0] + str(len(text))
    return result


def compressString(text):
    resultText = ""

    countedText = ""
    for char in text:

        if countedText == "" or char in countedText:
            # added the char
            countedText += char
        else:
            # not the same
            # first compress it
            resultText +=compress(countedText)
            # added the current char
            countedText = char


    # last char to add
    resultText += compress(countedText)

    if len(resultText) > len(text):
        resultText = text

    return resultText

if __name__ == '__main__':
    text = "aabcccccaaa"
    result = compressString(text)
    print(result)

    text = "compressed"
    result = compressString(text)
    print(result)