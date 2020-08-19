import time

def bubble_sort(data, drawData, ti):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                drawData(data, ['green' if x==j or x==j+1 else 'red' for x in range(len(data))])
                time.sleep(0.2)
    drawData(data, ['green' for x in range(len(data))])    #to color green to all cells after sorting      