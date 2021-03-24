# Prac test 3. contains a function that returns a list of indices of words that are palindromes
# KDSMIL001
# 29 April 2019

def getvalues(words):

    result = []
    for word in words:
        word_low = word.lower()
        if word_low == word_low[::-1]:
            result.append(int(words.index(word)))

    return result

def main():
    data = input().split(' ')
    print('Result:', getvalues(data))

if __name__ == '__main__':
    main()

