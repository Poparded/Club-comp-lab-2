n = 50
m = 40

import time
import pandas as pd
import numpy as np

def task2():
    start_time = time.time()
    data = []  # List to hold the data for DataFrame
    y=0
    a = np.random.randint(1, 100, 50)
    b = np.random.randint(1, 100, 50)
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
    end_time = time.time()
    execution_time = end_time - start_time
    data.append({'Iteration': number, 'a': a, 'b': b,"y" : y, 'Execution Time (Seconds)': execution_time})

    # Create DataFrame
    df = pd.DataFrame(data)
    pd.set_option('display.max_rows', 500)

    # Export to CSV
    df.to_csv('cleaned_data_task2.csv', index=False)
    #print(df)  # Optional: Print DataFrame


