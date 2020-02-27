# Randomly selects a response from a list of responses
# KDSMIL001
# 3 April 2019

import random

def welcome():
    print("Welcome to the automated technical support system.")
    print("Please describe your problem:")

def get_input():
    return input().lower()

def main():
    welcome()
    query = get_input()

    responses = ['Have you tried it on a different operating system?', 'Did you reboot it?', 'What colour is it?', 'You should consider installing anti-virus software.', 'Contact Telkom.\
', 'I should get that looked at if I were you.']

    while (not query == 'quit'):
        x = random.randint(0, 5)
        print(responses[x])

        query = get_input()


if __name__ == '__main__':
    main()