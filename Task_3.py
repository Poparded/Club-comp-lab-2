import numpy as np
import time
import pandas as pd


def task3():
        number = 0
        data = []  # List to hold the data for DataFrame

        while number <= 100:
            start_time = time.time()

            # Generating random 2D matrices
            A1 = np.random.randint(1, 100, (250, 250))
            A2 = np.random.randint(1, 100, (250, 250))
            B1 = np.random.randint(1, 100, (250, 250))
            B2 = np.random.randint(1, 100, (250, 250))

            # Matrix multiplication
            Z1 = np.multiply(A1, B1)
            Z2 = np.multiply(A2, B2)
            Z = Z1 + Z2

            # Writing results to file

            number += 1
            end_time = time.time()
            execution_time = end_time - start_time
            print(Z)
            data.append({'Iteration': number, 'a': Z1, 'b': Z2, "x": Z, 'Execution Time (Seconds)': execution_time})
        df = pd.DataFrame(data)
        pd.set_option('display.max_rows', 500)
# Writing execution time to file



