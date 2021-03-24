# checks if an inputted "pattern" matches a word but more complex
# KDSMIL001
# 24 April 2019

def match(pattern, word):
    if word=='' and pattern=='':
        return True
    elif pattern=='':
        return True
    elif word=='':
        return False
    elif word[0]==pattern[0] or pattern[0]=='?':
        return match(pattern[1:], word[1:])
    elif pattern[0]=='*':
        return match(pattern[1:], word) or match(pattern, word[1:])
    else:
        return False

