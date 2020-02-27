# program that takes an input of a word length and outputs the words in a given file with that length and that are anagrams of each other, in pairs in alphabetical order
# KDSMIL001
# 30 April 2019

def file_read(filename):
    x = open(filename, "r")
    return x

def file_write(filename):
    x = open(filename, "w")
    return x

def file_write_new(filename):
    x = open(filename, "w+")
    return x    

def get_input():
    x = input()
    return x

def make_dict(word):
    word_main = {}
    for letter in word:
        if letter in word_main:
            word_main[letter] += 1
        else:
            word_main[letter] = 1
    return word_main

def list_strip(list):
    for i in range(len(list)):
        list[i] = list[i][:-1]
    return list

def smth_list(sequence):
    for i in range(len(sequence)):
        sequence[i] = str(sequence[i])
    
    return sequence

def find_anagrams(filename, length):
    file = file_read(filename)
    file_list1 = file.readlines()
    file.close()

    file_list = list_strip(file_list1)
    final_list = []
    count = 0

    for line in file_list:
        if line != "START":
            count += 0
        else:
            count += 1

        curr_list = []
        if count >= 1:
            if len(line) == length:
                word_main = make_dict(line)
                file_list.pop(file_list.index(line))

                for word in file_list:
                    if len(word) == length:
                        word_curr = make_dict(word)
                    else:
                        continue

                    if word_curr == word_main:
                        if not (line in curr_list):
                            curr_list.append(line)
                        curr_list.append(word)
                        file_list.pop(file_list.index(word))

                curr_list.sort()
                if curr_list:
                    final_list.append(curr_list)

    final_list.sort()
    final_list = smth_list(final_list)
    # print(final_list)
    return final_list


def write_new_file(filename, sequence):
    file = file_write_new(filename)
    for line in sequence:
        # print(line)
        file.writelines(line)
        file.write('\n')
    file.close()

    return

def main():
    print("***** Anagram Set Search *****")
    print("Enter word length:")
    word = int(get_input())
    print("Searching...")
    sequence = find_anagrams("EnglishWords.txt", word)
    print("Enter file name:")
    new_filename = get_input()
    print("Writing results...")
    write_new_file(new_filename, sequence)

if __name__ == '__main__':
    main()
