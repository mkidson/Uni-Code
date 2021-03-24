# reads through a text file and inserts a print statement at certain places
# KDSMIL001
# 25 April 2019

def file_read(filename):
    x = open(filename, "r")
    return x

def file_write(filename):
    x = open(filename, "w")
    return x

def get_input():
    x = input()
    return x

def add_trace(filename):

    file = file_read(filename)    
    file_list = file.readlines()
    file.close()

    file_list.insert(0, '"""DEBUG"""\n')
    for line in file_list:
        if line[:3] == 'def':
            x = line.find('(')
            func_name = line[4:x]
            file_list.insert(file_list.index(line)+1, '    """DEBUG""";print(\'{}\')\n'.format(func_name))

    file1 = file_write(filename)
    for line in file_list:
        file1.write(line)
    file1.close()
    
    return

def remove_trace(filename):

    file = file_read(filename)    
    file_list = file.readlines()
    file.close()

    for line in file_list:
        if line == '"""DEBUG"""\n':
              file_list.pop(0)

        elif '    """DEBUG""";' in line:
            file_list.pop(file_list.index(line))

    file1 = file_write(filename)
    for line in file_list:
        file1.write(line)
    file1.close()
    
    return


def main():
    print("***** Program Trace Utility *****")
    print("Enter the name of the program file: ", end='')
    filename = get_input()
    file = file_read(filename)
    line1 = file.readline(13)
    if line1 == '"""DEBUG"""\n':
        remove_trace(filename)
    else:
        add_trace(filename)
        
if __name__ == '__main__':
    main()