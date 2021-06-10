    data=np.zeros((2,N))
    i=0
    for line in lines:
        line = line.strip()
        columns = line.split(',')
        data[0][i] = float(columns[0])
        data[1][i] = float(columns[1])
        i += 1
    f.close()