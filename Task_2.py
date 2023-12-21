n = 50
m = 40

import time
import pandas as pd
import numpy as np

def task2():
    start_time = time.perf_counter()
    total_time = 0
    data = []  # List to hold the data for DataFrame
    y=0

    a = np.loadtxt('./Task2_AB/random_integers_a.csv', delimiter=',')
    b = np.loadtxt('./Task2_AB/random_integers_b.csv', delimiter=',')
    suma=0
    sumb=0
    # Iterate through values of a and b
    number = 0
    for c in range(1, n):
        suma = (((a[c] ** 4) + (b[c] ** 2)) ** 3)
    for d in range(1, m):
        sumb = (((a[d] ** 2) - (b[d] ** 1)) ** 2)
    number += 1
    y = suma + sumb
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time
    data.append({
        'Iteration': number,  # Assuming a single iteration since no loop is present
        'Execution Time (Seconds)': execution_time,
        "Total Time": total_time

    })

    # Create DataFrame
    df = pd.DataFrame(data)
    pd.set_option('display.max_rows', 500)
    pd.set_option("display.precision", 9)

    # Export to CSV
    df.to_csv('cleaned_data_task2.csv', index=False)
    #print(df)  # Optional: Print DataFrame
