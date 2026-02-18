import time
import matplotlib.pyplot as plt

def algorithmOne(n):
    for i in range(n):
        for j in range(n):
            x = i + j

def benchmark(trials, runs):
    n = 1000
    inputs = []
    averages = []
    for i in range(trials): # Trial

        input = n*i
        times = []
        for j in range(runs): # Repeat identical trials
            startTime = time.perf_counter()
            algorithmOne(input) # Increaseing input, 
            stopTime = time.perf_counter()

            times.append(stopTime - startTime)
        
        average = sum(times)/len(times)
        print(f"Trial: {i + 1} -- input: {input} -- Average performance: {average} seconds")

        inputs.append(input)    
        averages.append(average)

    plt.plot(inputs, averages)
    plt.xlabel("Input size")
    plt.ylabel("Recorded time")
    plt.title("Algorithm Runtime")
    plt.show()

benchmark(10, 3)