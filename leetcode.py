# 给定一个字母串，依此打印所有的的字母排序
'''
    eg:输入abc,
       输出：[abc,acb,bac,bca,cab,cba]
'''
def s(string):
    l = []
    l_s = len(string)
    n = 1
    for i in range(1,l_s+1):
        n = n*i
    for j in range(n):
        s = ''
        for i in range(l_s):
            s = s+string[(j+i)%l_s]
        l.append(s)
    print(l)
if __name__ == "__main__":
    s('abce')

