import requests
import sys


# ___LIB___

def downin(day):
    headers = {'session': cookie}
    url = f"https://adventofcode.com/2021/day/{day}/input"
    session = requests.Session()
    resp = session.get(url,cookies=headers)
    in_file = open(f'day{day:02}.txt','w')
    in_file.write(resp.text)
    in_file.close()


def getin(day,flag):
    '''
    flag=0 for tst
    flag=1 for in
    '''
    data = ""
    if flag == 1:
        with open("./data/day"+str(day)+".in", 'r') as f:
            data = f.read()
            f.close()
        return data
    if flag == 0:
        with open("./data/day"+str(day)+".tst", 'r') as f:
            data = f.read()
            f.close()
        return data


def getin1(day,flag):
    data = getin(day,flag)
    data = data.split('\n')
    # converting strings to ints
    data = [int(data[i]) for i in range(len(data))]
    return data


# ___DAYS___


def day2_2():
    print("computing day 2 challange 2")
    data = getin1(day,flag)
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


def day2_1():
    print("computing day 2 challange 1")
    data = getin1(day,flag)
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
    windows = [data[i]+data[i+1]+data[i+2] for i in range(1+len(str)-k)]
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
        print("NEED 5 ARGS!!! [file, cookie, day, challenge, flag(0=tst, 1=in)]")
        exit(0)
    cookie, day, challange, flag = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    # downin(day)
    eval("day"+str(day)+"_"+str(challange)+"(day,flag)")