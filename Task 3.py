import numpy as np
number = 0
# Generating random 2D matrices A1, A2, B1, B2 each with dimensions 250x250
# and elements being positive integers less than 100
while number < 1:
    A1 = np.random.randint(1, 100, (250, 250))
    print(A1)
    A2 = np.random.randint(1, 100, (250, 250))
    print(A2)

    B1 = np.random.randint(1, 100, (250, 250))
    print(B1)

    B2 = np.random.randint(1, 100, (250, 250))
    print(B1)

    Z1 = np.multiply(A1, B1)
    Z2 = np.multiply(A2, B2)
    Z = Z1 + Z2
    #print(Z)
    number += 1
