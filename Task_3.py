import numpy as np
import time
import pandas as pd







def task3():
    data = []  # List to hold the data for DataFrame

    start_time = time.perf_counter()
    number= 0
    total_time= 0
    A1 = np.loadtxt('./Matrix_data/matrix_A1.csv', delimiter=',')
    A2 = np.loadtxt('./Matrix_data/matrix_A2.csv', delimiter=',')
    B1 = np.loadtxt('./Matrix_data/matrix_B1.csv', delimiter=',')
    B2 = np.loadtxt('./Matrix_data/matrix_B2.csv', delimiter=',')

    # Matrix multiplication
    Z1 = np.multiply(A1, B1)
    Z2 = np.multiply(A2, B2)
    Z = Z1 + Z2

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_time += execution_time

    number += 1
    # Append results to data list
    data.append({
        'Iteration': number,  # Assuming a single iteration since no loop is present
        'Execution Time (Seconds)': execution_time,
        "Total Time": total_time

        })

    # Create DataFrame and save to CSV
    df = pd.DataFrame(data)
    pd.set_option('display.max_rows', 500)
    pd.set_option('display.max_columns', 500)
    df.to_csv('cleaned_data_task3.csv', index=False)
    pd.set_option("display.precision", 9)
    np.savetxt('Matrix_data/matrix_Z.csv', Z, delimiter=',')



