import time
import pandas as pd

def task1():
    data = []  # List to hold the data for DataFrame
    number = 0
    total_time = 0
    # Start the timer
    start_time = time.perf_counter()

    # Iterate through values of a and b
    for a in range(1, 10):
        for b in range(1, 10):
            x = a + b
            number += 1
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            total_time += execution_time
            data.append({'Iteration': number, 'a': a, 'b': b, "x": x, 'Execution Time (Seconds)': execution_time, 'Total Time': total_time })

    # Create DataFrame
    df = pd.DataFrame(data)
    pd.set_option('display.max_rows', 500)
    pd.set_option("display.precision", 9)

    # Export to CSV
    df.to_csv('cleaned_data_task1.csv', index=False)

task1()
