#查找算法
# 顺序查找（list不一定有序，可以无序）
def find(arr,val):
    l = len(arr)
    for i in range(l):
        if arr[i]==val:
            return i
    return ''
# 顺序查找，由两边向中间查找
def find_2(arr,val):
    l = 0
    r = len(arr)-1
    while l < r:
        if arr[r] == val:
            return r
        if arr[l] == val:
            return l
        r -= 1
        l += 1
    if r==l:
        if arr[r]==val:
            return r
    return ''
# 顺序查找，有中间向两边查找
def mid_2(arr,val):
    l = len(arr)
    mid = int(l/2)
    mid_r = mid+1
    mid_l = mid
    while mid_l > -1 and mid_r < len(arr):
        if mid_l > -1:
            if arr[mid_l] == val:
                return mid_l
            else:
                mid_l -= 1
        if mid_r < l:
            if arr[mid_r] == val:
                return mid_r
            else:
                mid_r += 1
    return ''

# bin_search(二分查找)(list必须有序)
def bin_search(arr,val,l,r):
    mid = int(r/2+l/2)
    if l > r:
        print("arr error the num is not in arr")
        return ''
    if arr[mid] == val:
        return mid
    return bin_search(arr,val,l,mid-1) if arr[mid] > val else bin_search(arr,val,mid+1,r)
if __name__ == "__main__":
    arr = [i for i in range(1,100000000)]
    res = bin_search(arr,int(10000000/2/2/2/2/2/2),0,len(arr))
    print(res)
    # print(arr[res])
    