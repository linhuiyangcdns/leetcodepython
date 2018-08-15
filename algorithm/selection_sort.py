def selection_sort(list1):
    lenth = len(list1)
    for i in range(lenth - 1):
        min_index = i
        for j in range(i, lenth):
            if list1[j] < list1[min_index]:
                min_index = j
        if min_index != i:
            list1[i],list1[min_index] = list1[min_index],list1[i]
    return list1



if __name__ == '__main__':
    a = selection_sort([54,226,93,17,77,31,44,55,20])
    print(a)