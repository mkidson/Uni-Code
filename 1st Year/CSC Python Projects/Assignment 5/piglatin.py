# Module containing piglatin functions
# KDSMIL001
# 25 March 2019

def to_pig_latin(sentence):
    """Returns the piglatin version of the original sentence"""
    sentence_split = sentence.split(" ")
    new_sentence = ''
    for i in sentence_split:
        if i[0] == 'a' or i[0] == 'e' or i[0] == 'i' or i[0] == 'o' or i[0] == 'u':
            i += "way"
        else:
            i += "a"
            for c in range(len(i)):
                if i[c] ==  'a' or i[c] == 'e' or i[c] == 'i' or i[c] == 'o' or i[c] == 'u':
                    i = i[c:len(i)+1] + i[0:c] + "ay"
                    break
                else:
                    continue
        new_sentence += i + ' '
    return new_sentence


def to_english(sentence):
    """Returns the english version of the original sentence"""
    sentence_split = sentence.split(" ")
    new_sentence = ''
    for i in sentence_split:
        i = i[::-1]
        if i[0:3] == 'yaw':
            i = i[3:len(i)+1]
        else:
            i = i[2:len(i)+1]
            for c in range(len(i)):
                if i[c] ==  'a':
                    i = i[c+1:len(i)+1] + i[0:c]
                    break
                else:
                    continue
        new_sentence += i[::-1] + ' '
    return new_sentence

