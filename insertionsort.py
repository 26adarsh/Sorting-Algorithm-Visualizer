import time

def insertion_sort(data, drawData, timeTick):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            drawData(data, ['#DAF7A6' if x == j + 1 else "#900C3F" for x in range(len(data))])
            time.sleep(timeTick)
        data[j + 1] = key
        drawData(data, ['#DAF7A6' if x == i else "#900C3F" for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['#DAF7A6' for x in range(len(data))])
