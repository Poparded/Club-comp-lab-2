n = 50
m = 40

import time
import pandas as pd

def task1():
    start_time = time.time()
    data = []  # List to hold the data for DataFrame
    x=0
    suma=0
    sumb=0
    # Iterate through values of a and b
    number = 0
    for a in range(1, 100):
        for b in range(1, 100):
            for c in range(1, n):
                suma += (((a ** 4) + (b ** 2)) ** 3)
            for d in range(1, m):
                sumb += (((a ** 2) + (b ** 1)) ** 2)
            number += 1
            end_time = time.time()
            execution_time = end_time - start_time
            data.append({'Iteration': number, 'a': a, 'b': b,"x" : x, 'Execution Time (Seconds)': execution_time})

    # Create DataFrame
    df = pd.DataFrame(data)
    pd.set_option('display.max_rows', 500)

    # Export to CSV
    df.to_csv('cleaned_data.csv', index=False)
    #print(df)  # Optional: Print DataFrame




