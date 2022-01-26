def quickSort(numbers, left_index, right_index): #First and last index when calling from UI
    if left_index < right_index:
        pivot = partition(numbers, left_index, right_index) #Get the pivot for the numbers being checked
        quickSort(numbers, left_index, pivot - 1)
        quickSort(numbers, pivot + 1 ,right_index)

def partition(numbers, left_index, right_index):
    i = left_index
    j = right_index - 1
    pivot = numbers[right_index]
    while i <= j:
        if numbers[i] <= pivot:
            i +=1
        elif numbers[i] > pivot and numbers[j] <= pivot:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        elif numbers[i] > pivot and numbers[j] > pivot:
            j -= 1
    numbers[i], numbers[right_index] = numbers[right_index], numbers[i]
    return(i)

def mergeSort(numbers):
    if len(numbers) > 1:
        left_side = numbers[0:(len(numbers)//2)]
        right_side = numbers[(len(numbers)//2):]

        mergeSort(left_side)
        mergeSort(right_side)

        left_index = 0
        right_index = 0
        merge_index = 0

        while len(left_side) > left_index and len(right_side) > right_index:
            if left_side[left_index] > right_side[right_index]:
                numbers[merge_index] = right_side[right_index]
                right_index += 1
            else:
                numbers[merge_index] = left_side[left_index]
                left_index += 1
            merge_index += 1

        while len(left_side) > left_index:
            numbers[merge_index] = left_side[left_index]
            left_index += 1
            merge_index += 1

        while len(right_side) > right_index:
            numbers[merge_index] = right_side[right_index]
            right_index += 1
            merge_index += 1
        
        print(numbers)

def heapSort(numbers):
    pass

def bubbleSort(numbers):
    for index in range (0, len(numbers)-1):
        for second_index in range (index+1, len(numbers)):
            if numbers[index] > numbers[second_index]:
                numbers[index], numbers[second_index] = numbers[second_index], numbers[index]

def insertionSort(numbers):
    to_sort = range(1, len(numbers))
    for index in to_sort:
        while numbers[index-1] > numbers[index] and index > 0:
            numbers[index-1], numbers[index] = numbers[index], numbers[index-1]
            index -= 1

def selectionSort(numbers):
    minimum = 0
    for index in range(1, len(numbers)):
        if numbers[minimum] > numbers[index]:
            minimum = index
    numbers[0], numbers[minimum] = numbers[minimum], numbers[0]
    for index in range(1, len(numbers)):
        minimumm=index
        for second_index in range(index+1, len(numbers)):
            if numbers[minimumm] > numbers[second_index]:
                minimumm = second_index
        numbers[index], numbers[minimumm] = numbers[minimumm], numbers[index]

def treeSort(numbers):
    pass

numbers = [22,11,88,66,55,77,33,44,55,67,65,102,-4,66,88,-10]
numberst = [3,2,5,7,4]
#quickSort(numbers, 0, len(numbers) - 1)
#mergeSort(numbers)
#insertionSort(numberst)
#bubbleSort(numberst)
selectionSort(numberst)
print(numberst)
