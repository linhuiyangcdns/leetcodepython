def quick_sort(start,end,list1):
    low = start
    high = end
    if low >= high:
        return
    mid = list1[low]

    while low < high:
        while low < high and list1[high] >= mid:
            high -=1
        list1[low] = list1[high]

        while low < high and list1[low] <= mid:
            low += 1
        list1[high] = list1[low]
    list1[low] = mid
    # 此时low和high重合，将重合索引的位置放入mid

    quick_sort(start,low-1,list1)
    quick_sort(low + 1, end, list1)
    return list1







if __name__ == '__main__':
    li = [54,226,93,17,77,31,44,55,20]
    quick_sort(0,len(li)-1,li)
    print(li)