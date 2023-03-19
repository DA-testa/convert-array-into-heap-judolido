# python3


def build_heap(data):
    swaps = []
    SortedD = sorted(data)
    SortedLn = len(SortedD)
    
    def isMinHeap():
        for i in range(0, len(data)-3):
            if data[i] > data[i+1] and data[i] > data[i+2]:
                return False

        return True

    def parent(minIndex):
        if minIndex > 2:
            if minIndex % 2 == 0:
                parIndex = int((minIndex - 2) / 2)
            else:
                parIndex = int((minIndex - 1) / 2)
        else:
            return 0
        
        return parIndex

    def swap(parIndex, minIndex):
        swaps.append([parIndex, minIndex])

        temp = data[minIndex]
        data[minIndex] = data[parIndex]
        data[parIndex] = temp

    count = 0
    while not isMinHeap():
        minValue = SortedD[count]
        minIndex = data.index(minValue)

        parIndex = parent(minIndex)

        while data[parIndex] > data[minIndex]:
            swap(parIndex, minIndex)
            
            minIndex = data.index(minValue)
            parIndex = parent(minIndex)

        count+=1
        if(count>SortedLn-1):
            break

    return swaps


def main():

    switch = input()
    if "F" in switch:
        filename = input()
        if filename != "a":
            f = open("./tests/"+filename, "r")
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
            f.close()
    elif "I" in switch:
        n = int(input())
        data = list(map(int, input().split()))

    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
