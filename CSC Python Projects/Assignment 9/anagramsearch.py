# searches through a file for anagrams of an inputted word
# KDSMIL001
# 27 April 2019

import os.path

def file_read(filename):
    x = open(filename, "r")
    return x

def get_input():
    x = input("Enter a word: \n")
    return x

def find_anagram(word, filename):
    word_main = {}

    for letter in word:
        if letter in word_main:
            word_main[letter] += 1
        else:
            word_main[letter] = 1

    file = file_read(filename)
    if not file:
        print("Sorry, could not find file 'EnglishWords.txt'")
        return

    count = 0

    anagram_list = []
    for line in file:
        line = line[:-1]
        if line != "START":
            count += 0
        else:
            count += 1
        
        word_curr = {}
        if count >= 1:
            for letter in line:
                if letter in word_curr:
                    word_curr[letter] += 1
                else:
                    word_curr[letter] = 1
            
            
            if word_curr == word_main:
                if word == line:
                    continue
                else:
                    anagram_list.append(line)
    
    if anagram_list:
        print(anagram_list)
    else:
        print("Sorry, anagrams of '{}' could not be found.".format(word))

def main():
    print("***** Anagram Finder *****")
    try:
        if os.path.isfile("EnglishWords.txt"):
            word = get_input()
            find_anagram(word, "EnglishWords.txt")
        else:
            print("Sorry, could not find file 'EnglishWords.txt'.")
    except IOError as errno:
        print("Sorry, could not find file 'EnglishWords.txt'.")
        errno

if __name__ == '__main__':
    main()