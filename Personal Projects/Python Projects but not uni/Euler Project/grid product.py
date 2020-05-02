# calculates the greatest product of 4 adjacent numbers in a grid
# Miles Kidson
# 07-05-19

def to_int(list):
    new_list = []
    for num in list:
        x = int(num)
        new_list.append(x)
    
    return new_list

def hori(list):
    final = 0
    for item in list:
        # print(item)
        for i in range(len(item)-3):
            curr_tot = item[i]*item[i+1]*item[i+2]*item[i+3]
            if curr_tot > final:
                    final = curr_tot
    
    return final

def vert(list):
    final =  0
    for c in range(len(list)-3):
        # print(list[c])
        for i in range(len(list[c])):
            curr_tot = list[c][i]*list[c+1][i]*list[c+2][i]*list[c+3][i]
            if curr_tot > final:
                final = curr_tot

    return final
        
def diagonal_right(list):
    final = 0
    for i in range(len(list)-3):
        for c in range(len(list[i])-3):
            curr_tot = list[i][c]*list[i+1][c+1]*list[i+2][c+2]*list[i+3][c+3]
            if curr_tot > final:
                final = curr_tot

    return final

def diagonal_left(list):
    final = 0
    for i in range(4, len(list)):
        for c in range(len(list[i])-3):
            curr_tot = list[i][c]*list[i-1][c+1]*list[i-2][c+2]*list[i-3][c+3]
            if curr_tot > final:
                final = curr_tot

    return final

def list_trim(list):
    for i in range(len(list)):
        list[i] = list[i][:-1]
        list[i] = list[i].split(' ')
        list[i] = to_int(list[i])
    
    return list

def main():
    file = open("Python Projects but not uni\\Euler Project\\grid.txt", 'r')
    file_list = file.readlines()
    file.close()

    file_list = list_trim(file_list)

    print(max(hori(file_list), vert(file_list), diagonal_left(file_list), diagonal_right(file_list)))

if __name__ == '__main__':
    main()