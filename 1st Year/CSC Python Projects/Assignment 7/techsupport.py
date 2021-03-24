# Keeps a dictionary of responses indexed by keywords and searches inputs for indexes in the dictionary
# KDSMIL001
# 3 April 2019

def welcome():
    print("Welcome to the automated technical support system.")
    print("Please describe your problem:")

def get_input():
    return input().lower()

def main():
    welcome()
    query = get_input().split()

    responses = {
        'crashed': 'Are the drivers up to date?',
        'blue': 'Ah, the blue screen of death. And then what happened?',
        'hacked': 'You should consider installing anti-virus software.',
        'bluetooth': 'Have you tried mouthwash?',
        'windows': 'Ah, I think I see your problem. What version?',
        'apple': 'You do mean the computer kind?',
        'spam': 'You should see if your mail client can filter messages.',
        'connection': 'Contact Telkom.'
        }

    while (not 'quit' in query):
        for i in query:
            if i in responses:
                print(responses[i])
                query = get_input().split()
                break
            
            else:
                continue
        
        else:
            print('Curious, tell me more.')
            query = get_input().split()
            continue



if __name__ == '__main__':
    main()