# Finds the longest collatz sequence starting from a number under 1000000
# Miles Kidson
# 27 June 2019

def collatz(start):
    finals = []

    while start >= 1:
        if start == 1:
            finals.append(1)
            break
            
        elif start % 2 == 0:
            finals.append(int(start))
            start = start/2
    
        elif start % 2 == 1:
            finals.append(int(start))
            start = (start*3)+1

    return finals

def main():
    length = 0
    longest = 0
    for i in range(1000000):
        if len(collatz(i)) > length:
            longest = i
            length = len(collatz(i))
            print(longest)
        else:
            continue
        
    print(longest)

if __name__ == "__main__":
    main()