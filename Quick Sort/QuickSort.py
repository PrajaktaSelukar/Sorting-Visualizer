import time

def partition(data, head, tail, drawData, timeTick):
    pivot = data[tail]
    #left side of border has all elements lesser than pivot
    #right side of border has all elements greater than or equal to pivot
    border = head
    
    drawData(data, getColorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)
    
    for j in range(head, tail):
        if data[j] < pivot:
            drawData(data, getColorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)
    
            data[j], data[border] = data[border], data[j]
            border += 1
        
        drawData(data, getColorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)
            
    #swap pivot with border value
    drawData(data, getColorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)
    
    data[border], data[tail] = data[tail], data[border]
    
    return border        

def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIndex = partition(data, head, tail, drawData, timeTick)

        #Left partition
        quick_sort(data, head, partitionIndex-1, drawData, timeTick)

        #Right partition
        quick_sort(data, partitionIndex+1, tail, drawData, timeTick)
        
def getColorArray(datalen, head, tail, border, currIndex, isSwapping=False):
    colorArray = []
    for i in range(datalen):
        #base coloring
        if i >= head and i <= tail:
            colorArray.append('gray')
        else:
            colorArray.append('white')
            
        if i == tail:
            colorArray[i] = 'blue'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIndex:
            colorArray[i] = 'yellow'
        
        if isSwapping:
            if i == border or i == currIndex:
                colorArray[i] = 'green'

    return colorArray                                     