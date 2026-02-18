import time

def algorithmOne(n):
    for i in range(n):
        for j in range(n):
            x = i + j

n = 100

startTime = time.perf_counter()
algorithmOne(n)
stopTime = time.perf_counter()

totalTime = stopTime - startTime
print(totalTime)