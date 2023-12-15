import numpy as np
import time

def task3():
    start_time = time.time()
    log_file = "Task3.txt"  # Name of the log file

    with open(log_file, "w") as file:
        number = 0
        while number <= 100:
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
            file.write(f"Result of Z1 and Z2 is equal to:\n{Z}\n")

            number += 1

    end_time = time.time()
    execution_time = end_time - start_time

    # Writing execution time to file
    with open(log_file, "a") as file:  # Appending to the file
        file.write(f"Execution time: {execution_time} Seconds\n")

    print(f"Execution time: {execution_time} Seconds")

