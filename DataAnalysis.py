datacnt = [0] * 81
dataori = [i for i in range(81)]

def BasicAnalysis(ori_data):
    # Basic analysis of the data
    # ori_data: original data
    # Return: None
    # Author: KittenCN
    global datacnt, dataori
    for row in ori_data:
        for item in row:
            datacnt[item] += 1
    datacnt, dataori = sortcnt(datacnt, dataori)
    lastcnt = -1
    for i in range(81):
        if dataori[i] == 0:
            continue
        if lastcnt != datacnt[i]:
            print()
            print("{}: {}".format(datacnt[i], dataori[i]), end = " ")
            lastcnt = datacnt[i]
        elif lastcnt == datacnt[i]:
            print(dataori[i], end = " ")
    
def sortcnt(datacnt, dataori):
    for i in range(81):
        for j in range(i + 1, 81):
            if datacnt[i] < datacnt[j]:
                datacnt[i], datacnt[j] = datacnt[j], datacnt[i]
                dataori[i], dataori[j] = dataori[j], dataori[i]
    return datacnt, dataori

def getdata():
    strdata = input("Shrinkage ratio (split by ',' ): ").split(',')
    data = [int(i) for i in strdata]
    ori_data = []
    for i in range(81):
        if dataori[i] == 0:
            continue
        if datacnt[i] in data:
            ori_data.append(dataori[i])
    bool_data = [False] * len(ori_data)
    return ori_data, bool_data

def dfs(ori_data, bool_data, getnums, dep, ans, cur):
    if dep == getnums:
        ans.append(cur.copy())
        return
    for i in ori_data:
        if bool_data[ori_data.index(i)] or i <= cur[dep - 1]:
            continue
        bool_data[ori_data.index(i)] = True
        cur[dep] = i
        dfs(ori_data,bool_data, getnums, dep + 1, ans, cur)
        bool_data[ori_data.index(i)] = False
    return ans
    

def shrink(ori_data, bool_data):
    getnums = int(input("How many numbers do you want to get? (-1 means over) "))
    while getnums != -1:
        ans = dfs(ori_data,bool_data, getnums, 0, [], [0] * getnums)
        print("There are {} ways to get {} numbers.".format(len(ans), getnums))
        for i in range(len(ans)):
            print(ans[i])
        getnums = int(input("How many numbers do you want to get? (-1 means over) "))


if __name__ == "__main__":
    n = int(input("how many data do you want to generate? "))
    ori_data = []
    for i in range(n):
        tmp_data = input("please input the data #{}: ".format(i + 1)).strip().split(' ')
        tmp_data = [int(item) for item in tmp_data]
        ori_data.append(tmp_data)
    BasicAnalysis(ori_data)
    print()
    ori_data, bool_data = getdata()
    print()
    shrink(ori_data, bool_data)
