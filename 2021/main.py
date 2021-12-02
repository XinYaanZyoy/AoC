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

def day3_1(day,flag):
    print("computing day 3 challange 1")
    data = getin(day,flag)


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
    downin(day,cookie)
    eval("day"+str(day)+"_"+str(challange)+"(day,flag)")