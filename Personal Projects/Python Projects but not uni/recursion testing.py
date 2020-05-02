

def sum_to(a):
    if a == 0:
        return 0

    else:
        return a + sum_to(a-1)




def x_power(x, n):
    if n == 1:
        return x
    
    else:
        return x * x_power(x, n-1)

def hanoi(n, source, spare, dest):
    if n> 0:
        hanoi(n-1, source, dest, spare)
        print("Move disk {} from {} to {}".format(n, source, dest))
        hanoi(n-1, spare, source, dest)

def main():
    hanoi(4, "a", "b", "c")



if __name__ == '__main__':
    main()



