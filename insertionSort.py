size = int(input())
arr = input().split(" ")
moving = " "
sorted = False

def show(s, uns):
    string = ""
    for i in s:
        string += i + " "
    string += ", "
    for i in uns:
        string += i + " "
    print(string)


def insertionSort(arr):
    sorted = [arr[0]]
    unsorted = arr[1:]
    
    for i in range(len(unsorted)):
        
        show(sorted, unsorted)
        #print(int(unsorted[0]) > int(sorted[-1]))
        if(len(unsorted) > 0):
            if(int(unsorted[0]) > int(sorted[-1])):
                sorted.append(unsorted[0])
                unsorted = unsorted[1:]
            else:
                for j in range(len(sorted)):
                    if(len(unsorted) > 0):
                        if int(unsorted[0]) < int(sorted[j]):
                            sorted.insert(j, unsorted[0])
                            unsorted = unsorted[1:]
                    show(sorted, unsorted)

insertionSort(arr)

