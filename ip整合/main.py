#coding=utf-8

#去掉\n换行符存储到数组中
def read_file():
    f = open(u'徐州.txt','r')
    iplist = f.read().split('\n')#截断去掉 \n
    if iplist[-1] == '':
        iplist.pop()
    return iplist

#列表读取测试代码
#iplist = read_file()
#print (iplist)
#print (len(iplist))


#将-全部转换为正常格式ip
def formate():  #格式化去掉-
    arr = [] #存新的数据
    iplist = read_file()
    for l in iplist:
        if l.find('-')==-1:
            arr.append(l)
        else:
            s = l.split('.') #去掉.的ip数组
            t = s[3].split('-')
        #    print t
            head = (int)(t[0])#-头
            font = (int)(t[1])#-尾
            for i in range(head,font+1):
#                str_ip.append(s[0]+'.'+s[1]+'.'+s[2]+'.'+str(i))
                arr.append(s[0]+'.'+s[1]+'.'+s[2]+'.'+str(i))
    return arr

#列表-拆分测试代码
#L = formate()
#print ("拆分后的ip集合")
#print (L)

#合并ip
def combine():
    iplist = formate()
    newIp = []  #新的ip段
#    print (len(iplist))
    while len(iplist):
        buffer = [] #前三位相同网段的缓存池

        t = iplist[0] #抽出一个用来比较
        s1 = t.split('.')

        #找到相同网段下的

        for l in iplist:
            s2 = l.split('.')
            if s1[0]==s2[0] and s1[1]==s2[1] and s1[2]==s2[2]:
                buffer.append(l)
    #            iplist.remove(l) 这里切不可用remove 因为会导致iplist 变短 循环出错
#        print (buffer)

        #把iplist中删去作为buffer的一部分
        s1 = buffer[0].split('.')
        i = 0
        while i < len(iplist):
            s2 = iplist[i].split('.')
            if s1[0]==s2[0] and s1[1]==s2[1] and s1[2]==s2[2]:
                iplist.pop(i)
                i-=1
            i+=1


    #    print (iplist)


        #处理buffer到newIp
        #这里把buffer中最后一位提取出来 做好排序 用来归并
        num = []
        t_ip = [] #存处理好的单个ip段
        #将最后数字存起来
        t = buffer[0].split('.')
        for b in buffer:
            t = b.split('.')
            num.append((int)(t[3])) #排序
        num.sort()
#        print (num)


#   整理ip
        while len(num):
            j = 0
            lnum = (int)(num[0])#第一个字符用来合并 左右字符
            rnum = lnum
            for inum in num:
                if rnum == (int)(inum):
                    j = j + 1
                elif rnum == (int)(inum) - 1:
                    rnum = (int)(inum)
                    j = j + 1
                else:
                    pass
            t_ip = []
            t_ip.append(t[0]+'.'+t[1]+'.'+t[2]+'.'+str(lnum)+'-'+str(rnum))
#            print (t_ip)
            newIp.append(t_ip)

            j = j - 1
            while j>=0:
                num.pop(j)
                j = j - 1

    return newIp

def write_file():
    fo = open('result.txt','w')
    L = combine()
    for l in L:
        s = ''.join(l)
        s = s + '\n'
        fo.write(s)
    fo.close()



write_file()
