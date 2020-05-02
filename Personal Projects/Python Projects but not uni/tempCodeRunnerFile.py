for i in range(1,21):
    while num % i == 0 and num < 300:
        print(num)
        print(i)
        num += 1
    num = 1
    