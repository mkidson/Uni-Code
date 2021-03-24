# checks if an inputted "pattern" matches a word
# KDSMIL001
# 20 April 2019


def match(pattern, word):
    if len(pattern) == 0 and len(word) == 0:
        return True
    
    elif len(pattern) != len(word):
        return False

    if pattern[0] == '?' and match(pattern[1::], word[1::]):
        return True

    elif pattern[0] == word[0] and match(pattern[1::], word[1::]):
        return True

    else:
        return False


def main():
    x = input("Enter a pattern:\n")
    y = input("Enter a word\n")
    
    print(match(x, y))


if __name__ == '__main__':
    main()