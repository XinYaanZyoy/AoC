import requests as req
import sys


# ___LIB___

def downin(day,cookie):
    headers = {'session': cookie}
    url = f"https://adventofcode.com/2021/day/{day}/input"
    session = req.Session()
    res = session.get(url,cookies=headers)
    with open(f"./data/day{day}.in",'w') as f:
        f.write(res.text)
        f.close()


def getin(day,flag):
    '''
    flag=0 for tst
    flag=1 for in
    '''
    data = ""
    if flag == 1:
        with open(f"./data/day{day}.in", 'r') as f:
            data = f.read()
            f.close()
        return data
    if flag == 0:
        with open(f"./data/day{day}.tst", 'r') as f:
            data = f.read()
            f.close()
        return data


def getin1(day,flag):
    data = getin(day,flag)
    data = data.split('\n')
    data = [data[i] for i in range(len(data)) if data[i] != ""]
    data = [int(data[i]) for i in range(len(data))]
    return data


# ___DAYS___
def day3_2(day,flag):
    print("computing day 3 challange 2")
    data = getin(day,flag)
    data = data.split('\n')
    data = [data[i] for i in range(len(data)) if data[i] != ""]
    # print(data)
    def bita(data,j,r):
        if r==0:
            count=0
            for digit in data:
                count = count + int(digit[j])
            # ORDER MATTERS!!
            if count < len(data)/2:
                count = 0
            if count == len(data)/2:
                count = 1
            if count > len(data)/2:
                count = 1
            return count
        if r==1:
            count=0
            for digit in data:
                count = count + int(digit[j])
            if count < len(data)/2:
                count = 1
            if count == len(data)/2:
                count = 0
            if count > len(data)/2:
                count = 0
            return count
    data_copy = data
    for j in range(len(data[0])):
        print(data_copy)
        data_tmp = []
        bit = bita(data_copy,j,0)
        for digit in data_copy:
            if int(digit[j]) == bit:
                data_tmp.append(digit)
        data_copy = data_tmp
        if len(data_copy) == 1:
            break
    o2_bin = data_copy[0]
    data_copy = data
    for j in range(len(data[0])):
        data_tmp = []
        bit = bita(data_copy,j,1)
        for digit in data_copy:
            if int(digit[j]) == bit:
                data_tmp.append(digit)
        data_copy = data_tmp
        if len(data_copy) == 1:
            break
    co2_bin = data_copy[0]
    print(o2_bin, co2_bin)
    o2_dec = [int(o2_bin[i])*(2**(len(o2_bin)-1-i)) for i in range(len(o2_bin))]
    co2_dec = [int(co2_bin[i])*(2**(len(co2_bin)-1-i)) for i in range(len(co2_bin))]
    o2 = 0
    for digit in o2_dec:
        o2 = o2 + digit
    co2 = 0
    for digit in co2_dec:
        co2 = co2 + digit
    print(o2,co2, o2*co2)


def day3_1(day,flag):
    print("computing day 3 challange 1")
    data = getin(day,flag)
    data = data.split('\n')
    data = [data[i] for i in range(len(data)) if data[i] != ""]
    # print(data)
    count=[0]*len(data[0])
    # print(count)
    for j in range(len(data[0])):
        for i in range(len(data)):
            count[j] = count[j] + int(data[i][j])
        if count[j] > len(data)/2:
            count[j] = 1
        else:
            count[j] = 0
    gamma_bin = count
    epsilon_bin = [0 if i else 1 for i in gamma_bin]
    print(gamma_bin, epsilon_bin)
    gamma_dec = [gamma_bin[i]*(2**(len(gamma_bin)-1-i)) for i in range(len(gamma_bin))]
    epsilon_dec = [epsilon_bin[i]*(2**(len(epsilon_bin)-1-i)) for i in range(len(epsilon_bin))]
    print(gamma_dec, epsilon_dec)
    gamma = 0
    for digit in gamma_dec:
        gamma = gamma + digit
    print(gamma)
    epsilon = 0 
    for digit in epsilon_dec:
        epsilon = epsilon + digit
    print(epsilon)
    print(gamma*epsilon)

def day2_2(day,flag):
    print("computing day 2 challange 2")
    data = getin(day,flag)
    data = data.split('\n')
    data = [data[i] for i in range(len(data)) if data[i] != ""]
    data = [data[i].split() for i in range(len(data))]
    # print(data)
    count_h=0
    count_d=0
    aim=0
    for i in range(len(data)):
        if data[i][0] == "down":
            aim = aim + int(data[i][1])
        if data[i][0] == "up":
            aim = aim - int(data[i][1])
        if data[i][0] == "forward":
            count_h = count_h + int(data[i][1])
            count_d = count_d + aim*int(data[i][1])
    print(count_h, count_d, count_h*count_d)


def day2_1(day,flag):
    print("computing day 2 challange 1")
    data = getin(day,flag)
    data = data.split('\n')
    data = [data[i] for i in range(len(data)) if data[i] != ""]
    data = [data[i].split() for i in range(len(data))]
    # print(data)
    count_h=0
    count_d=0
    for i in range(len(data)):
        if data[i][0] == "forward":
            count_h = count_h + int(data[i][1])
        if data[i][0] == "down":
            count_d = count_d + int(data[i][1])
        if data[i][0] == "up":
            count_d = count_d - int(data[i][1])
    print(count_h, count_d, count_h*count_d)


def day1_2(day,flag):
    print("computing day 1 challange 2")
    data = getin1(day,flag)
    # print(data)
    wl = 3 #window len
    windows = [data[i]+data[i+1]+data[i+2] for i in range(1+len(data)-wl)]
    # print(windows)
    count = 0
    for i in range(1, len(windows)):
        if windows[i]>windows[i-1]:
            count = count + 1
    print(count)


def day1_1(day,flag):
    print("computing day 1 challange 1")
    data = getin1(day,flag)
    # print(data)
    count = 0
    for i in range(1, len(data)):
        if data[i]>data[i-1]:
            count = count + 1
    print(count)


# ___INIT___


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("NEED 5 ARGS!!! [file, cookie, flag(0=tst, 1=in)], day, challenge")
        exit(0)
    cookie, flag, day, challange = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    # downin(day,cookie)
    eval("day"+str(day)+"_"+str(challange)+"(day,flag)")