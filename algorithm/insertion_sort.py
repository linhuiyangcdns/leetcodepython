def insertion_sort(list1):
    for i in range(1,len(list1)):
        for j in range(i,0,-1):
            if list1[j] < list1[j-1]:
                list1[j],list1[j-1] = list1[j-1],list1[j]
    return list1

if __name__ == '__main__':
    li = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(insertion_sort(li))