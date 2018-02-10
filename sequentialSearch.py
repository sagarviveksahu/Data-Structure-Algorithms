def seqSearch(dataList,value):
    found = False
    for i in range(len(dataList)):
        if dataList[i] == value:
            found = True
            break
    return found

a = [1,68,97,3,675,9,54]
print(seqSearch(a,3))