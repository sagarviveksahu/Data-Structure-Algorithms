def binarySearch(dataList,value):
    mid = len(dataList)//2
    found = False
    start = 0
    end = len(dataList)
    while start < end and not found:
        mid = (start + end) // 2
        print(dataList[mid])
        if value == dataList[mid]:
            found = True
        else:
            if value < dataList[mid]:
                end = mid
            else:
                start = mid + 1
    return found

a = [1,6,9,31,67,90,154,234,250,346,423,565,634,647,787]
print(binarySearch(a,423))
