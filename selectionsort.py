import time

def selection_sort(data, drawData, timeTick):
    for i in range(len(data) - 1):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_idx]:
                min_idx = j
            drawData(data, ['#FF5733' if x == j or x == min_idx else "#2874A6" for x in range(len(data))])
            time.sleep(timeTick)
        data[i], data[min_idx] = data[min_idx], data[i]
        drawData(data, ['#FF5733' if x == i or x == min_idx else "#2874A6" for x in range(len(data))])
        time.sleep(timeTick)
    drawData(data, ['#FF5733' for x in range(len(data))])
