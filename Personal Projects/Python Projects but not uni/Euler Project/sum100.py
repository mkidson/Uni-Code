# calculates the first ten digits of the sum of big numbers
# Miles Kidson
# 14-05-19

def file_read(filename):
    x = open(filename, "r")
    return x

def main():

    f = file_read("Python Projects but not uni\\Euler Project\\grid.txt")
    file_list = f.readlines()
    f.close()

    tot = 0
    for line in file_list:
        line = line[:-1]
        x = int(line)
        print(x)
        tot += x

    print(tot)
    tot2 = str(tot)[:10]
    print(tot2)

if __name__ == "__main__":
    main()