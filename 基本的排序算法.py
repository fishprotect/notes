# 冒泡排序 
# 要点时：每一次遍历，都把最小的或者最大的提取出来,可以放置在首位，也可以放置在末尾
'''
    注：重点是交换
'''
def sort_m(arr):
    l = len(arr)
    for i in range(l):
        for j in range(l-i):
            if arr[j] > arr[l-i-1]:
                arr[j],arr[l-i-1] = arr[l-i-1],arr[j]
    return arr
# 选择排序，选择排序和冒泡排序有相似的地方
# 要点，选择最大的或者最小的
'''
    注：选择排序就是优化的冒泡排序
    重点时：选出最小值，然后与特定位置交换
'''
def select_sort(arr):
    l = len(arr)
    for i in range(l):
        min = arr[i]
        count = i
        for j in range(i+1,l):
            if arr[j] < min:
                min = arr[j]
                count = j
        arr[i],arr[count] = arr[count],arr[i]
    return arr
# 插入排序：
def insert_sort(arr):
    l = len(arr)
    new_l = [arr[0]]

    for i in range(1,l):
        l_n = len(new_l)
        for j in range(l_n):
            if arr[i] < new_l[0]:
                print(new_l[0])
                new_l.insert(0,arr[i])
                break
            elif arr[i] > new_l[j]:
                new_l.insert(j-1,arr[i])
                break
            elif arr[i] > new_l[l_n-1]:
                new_l.append(arr[i])
                break
            elif arr[i] == new_l[j]:
                new_l.insert(j,arr[i])
    return new_l
# 快速排序 
'''
    注：
    1：分为两步，第一步分开
    2：迭代分开
    知道分为单个list
    1：合并
'''
def master_sort(arr):
    # 判断是否为
    l = len(arr)
    if l<=1:
        return arr
    arr1 = []
    arr2 = []
    for i in arr:
        if i < arr[0]:
            arr1.append(i)
        elif i > arr[0]:
            arr2.append(i)
    arr1.append(arr[0])

    return master_sort(arr1)+master_sort(arr2)
# 归并分治
'''
    注：分为分治+归并
    merge:用于合并,merge函数中的两个数组均为有序的
    gui_sort:用于分治
'''
def merge_arr(arr1,arr2):
    count1 = 0
    count2 = 0
    while 1:
        l2 = len(arr2)
        l1 = len(arr1)
        if count1 == l1:
            break
        if arr1[count1] <= arr2[0]:
            arr2.insert(0,arr1[count1])
            count1 += 1
        elif arr1[count1] >= arr2[l2-1]:
            arr2.append(arr1[count1])
            count1 += 1
        elif arr1[count1] > arr2[count2]:
            count2 += 1
        elif arr1[count1] <= arr2[count2]:
            arr2.insert(count2,arr1[count1])
            count1 += 1


    return arr2

        
def gui_sort(arr):
    l = len(arr)
    if l == 1:
        return arr
    elif l == 2:
        if arr[0] > arr[1]:
            arr[0],arr[1] = arr[1],arr[0]
        return arr
    elif l > 2:
        mid = int(l/2)
        arr1 = arr[:mid]
        arr2 = arr[mid:]
    return merge_arr(gui_sort(arr1),gui_sort(arr2))

 

if __name__ == "__main__":
    import random
    arr = [i for i in range(60)]
    arr1 = [0,1,3,5,7,9,15]
    arr2 = [2,4,6,8,12]
    x = merge_arr(arr1,arr2)
    print(x)
    # random.shuffle(arr)
    # print(arr)
    # x =  gui_sort(arr)
    # print(x)