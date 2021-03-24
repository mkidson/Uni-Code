# checks if an inputted "pattern" matches a word, but more complex
# KDSMIL001
# 20 April 2019


def match(pattern, word):
    if word=='' and pattern=='':
        return True
    elif pattern=='':
        return False
    elif pattern[0]=='*':
        return match(pattern[1:], word)
    elif word=='':
        return False
    elif word[0]==pattern[0] or pattern[0]=='?':
        return match(pattern[1:], word[1:])
    elif pattern[0]=='*':
        return match(pattern[1:], word) or match(pattern, word[1:])
    else:
        return False


def main():
    x = input("Enter a pattern:\n")
    y = input("Enter a word\n")
    
    print(match(x, y))


if __name__ == '__main__':
    main()