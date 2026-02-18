import time

def algorithmOne(n):
    for i in range(n):
        for j in range(n):
            x = i + j

def benchmark(trials, runs):
    n = 1000
    for i in range(trials): # Trial

        times = []
        for j in range(runs): # Repeat identical trials
            input = n*i
            startTime = time.perf_counter()
            algorithmOne(input) # Increaseing input, 
            stopTime = time.perf_counter()

            times.append(stopTime - startTime)

        print(f"Trial: {i + 1} -- input: {input} -- Average performance: {sum(times)/len(times)} seconds")

benchmark(5, 5)