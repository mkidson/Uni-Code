# checks if a string is a palindrome, recursively
# KDSMIL001
# 20 April 2019

def is_pal(sentence):
    if len(sentence) == 1 or len(sentence) == 0:
        return True

    if sentence[0] != sentence[-1]:
        return False

    elif is_pal(sentence[1:-1]):
        return True
    
    else:
        return False


def main():
    x = input("Enter a string:\n")
    
    if is_pal(x):
        print("Palindrome!")
    else:
        print("Not a palindrome!")


if __name__ == '__main__':
    main()