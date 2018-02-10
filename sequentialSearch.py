def seqSearch(dataList,value):
    found = False
    for i in range(len(dataList)):
        if dataList[i] == value:
            found = True
            break
    return found

