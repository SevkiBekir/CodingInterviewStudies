def isSubstring(s1,s2):
    concatS2 = s2 + s2
    if s1 in concatS2:
        return True

    return False


if __name__ == '__main__':
    str1 = "waterbottle"
    str2 = "erbottlewat"
    print(isSubstring(str1,str2))