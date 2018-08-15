


def binary_search(list1,item):
    low = 0
    high = len(list1) -1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list1[mid]
        if item == guess:
            return list1[mid]
        elif item > guess:
            low = mid + 1
        else:
            high = mid - 1
    return None




if __name__ == '__main__':
    print(binary_search([1,2,3,4,5,6,7,8],-1))
