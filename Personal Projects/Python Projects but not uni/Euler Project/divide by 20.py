# Computes the smallest number divisible by integers 1 - 20
# Miles Kidson
# 6 April 2019

def main():
    t = 20
    lst = []
    while t != 0:
        for i in range(1, 21):
            if t % i == 0:
                lst.append(i)

        if len(lst) == 20:
            print(t)
            t = 0
    
        else:
            t += 20
            lst = []

if __name__ == '__main__':
    main()