#十进制转换二进制 string_num 传入的十进制字符串 digit传入二进制位数
def DecToBit(string_num,digit):
    i = 0 #用于计数
    flag = 0 #正数情况
    num = int(string_num)
    if num < 0:
        num = -num
        flag = 1 #标记为负数
    mid = []
    while True:
        if num == 0:
            break
        num,rem = divmod(num,2)
        mid.append(rem)
    while len(mid)<digit:
        mid.append(0)
    if flag == 0:
        return ''.join([str(x) for x in mid[::-1]])#倒序排列
    else:
        return '-'+''.join([str(x) for x in mid[::-1]])

#数据处理 二进制转浮点数
def BitToFloat(string_num):
    if string_num[0] == '0':
        i = string_num[:9] #i 整数部分 前面多少个
        i = int(i)
        d = string_num[9:] #d 小数部分
        i = str(i)
        d = list(d)
        sum = int(i,2)
        n = len(d)
        t = 1
        while t <= n:
            sum = sum + pow(1/2,t) * (int)(d[t-1])
            t = t + 1
        return sum
    else:
        t = 15 #确定需要取反的位置 求补码
        string_num = list(string_num)
        while  t:
            if string_num[t] == '1':
                break;
            t = t - 1
        j = 0
        while j<t:
            if string_num[j] == '1':
                string_num[j] = '0'
            else:
                string_num[j] = '1'
            j = j + 1
        string_num = ''.join(string_num)
        i = string_num[:9] #i 整数部分
        i = int(i)
        d = string_num[9:] #d 小数部分
        i = str(i)
        d = list(d)
        sum = int(i,2)
        n = len(d)
        t = 1
        while t <= n:
            sum = sum + pow(1/2,t) * (int)(d[t-1])
            t = t + 1
        return -sum

#数据处理 第一位为整数的数据处理 值范围 -1 ~ 1 string_num传入二进制字符串
def Datahandel(string_num):
    sum = 0
    if string_num[0] == '0':
        d = string_num[1:] #d 小数部分
        d = list(d)
        n = len(d)
        t = 1
        while t <= n:
            sum = sum + pow(1/2,t) * (int)(d[t-1])
            t = t + 1
        return sum
    else:
        string_num = list(string_num)
        t = len(string_num) - 1
        while  t:
            if string_num[t] == '1':
                break;
            t = t - 1
        j = 0
        while j<t:
            if string_num[j] == '1':
                string_num[j] = '0'
            else:
                string_num[j] = '1'
            j = j + 1
        string_num = ''.join(string_num)
        d = string_num[1:] #d 小数部分
        d = list(d)
        n = len(d)
        t = 1
        while t <= n:
            sum = sum + pow(1/2,t) * (int)(d[t-1])
            t = t + 1
        return -sum
