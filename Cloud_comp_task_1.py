import time
import pandas as pd

def task1():
    start_time = time.time()
    data = []  # List to hold the data for DataFrame

    # Iterate through values of a and b
    number = 0
    while number <= 100:
        for a in range(1, 10):
            for b in range(1, 10):
                if a + b == 10:
                    number += 1
                    end_time = time.time()
                    execution_time = end_time - start_time
                    data.append({'Iteration': number, 'a': a, 'b': b, 'Execution Time (Seconds)': execution_time})

    # Create DataFrame
    df = pd.DataFrame(data)

    # Export to CSV
    df.to_csv('cleaned_data.csv', index=False)
    print(df)  # Optional: Print DataFrame

