def getin(day):
    data = ""
    with open("./data/day"+str(day)+".in", 'r') as f:
        data = f.read()
        f.close()
    return data


def n_of_sub_str_k_of_l(str, k):
    '''
    number of substrings of length k of a string of length l
    '''
    return 1+len(str)-k


def day01_1():
    print("computing day01 challange 1")
    data = getin(1)
    data = data.split('\n')
    # converting strings to ints
    data = [int(data[i]) for i in range(len(data))]
    # print(data)
    count = 0
    for i in range(1, len(data)):
        if data[i]>data[i-1]:
            count = count + 1
    print(count)


def day01_2():
    print("computing day01 challange 2")
    data = getin(1)
    data = data.split('\n')
    # converting strings to ints
    data = [int(data[i]) for i in range(len(data))]
    # print(data)
    wl = 3 #window len
    windows = [data[i]+data[i+1]+data[i+2] for i in range(n_of_sub_str_k_of_l(data,wl))]
    # print(windows)
    count = 0
    for i in range(1, len(windows)):
        if windows[i]>windows[i-1]:
            count = count + 1
    print(count)

if __name__ == "__main__":
    day01_2()