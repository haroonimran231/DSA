import numpy as np

# Function to check if two matrices are equal
def are_matrices_equal(A, B):
    return np.array_equal(A, B)

# Standard matrix multiplication
def standard_matrix_multiplication(A, B):
    return np.dot(A, B)

# Strassen's matrix multiplication algorithm
def strassen_multiplication(A, B):
    n = len(A)
    
    if n == 1:
        return A * B
    
    # Split matrices into quadrants
    mid = n // 2
    A11, A12 = A[:mid, :mid], A[:mid, mid:]
    A21, A22 = A[mid:, :mid], A[mid:, mid:]
    B11, B12 = B[:mid, :mid], B[:mid, mid:]
    B21, B22 = B[mid:, :mid], B[mid:, mid:]

    # Compute Strassen's 7 products
    P1 = strassen_multiplication(A11 + A22, B11 + B22)
    P2 = strassen_multiplication(A21 + A22, B11)
    P3 = strassen_multiplication(A11, B12 - B22)
    P4 = strassen_multiplication(A22, B21 - B11)
    P5 = strassen_multiplication(A11 + A12, B22)
    P6 = strassen_multiplication(A21 - A11, B11 + B12)
    P7 = strassen_multiplication(A12 - A22, B21 + B22)

    # Combine results into the final matrix
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 + P3 - P2 + P6

    # Stack quadrants into a full matrix
    top = np.hstack((C11, C12))
    bottom = np.hstack((C21, C22))
    return np.vstack((top, bottom))

### Exercise 2: Random matrix generation

# Function to generate random n x n matrices
def generate_random_matrix(n):
    return np.random.randint(0, 10, (n, n))

### Exercise 3: Compare execution times

import time

def compare_execution_times():
    sizes = [2, 4, 8, 16, 32, 64]
    for n in sizes:
        A = generate_random_matrix(n)
        B = generate_random_matrix(n)

        # Time standard multiplication
        start_time = time.time()
        result_standard = standard_matrix_multiplication(A, B)
        standard_time = time.time() - start_time

        # Time Strassen's multiplication
        start_time = time.time()
        result_strassen = strassen_multiplication(A, B)
        strassen_time = time.time() - start_time

        # Verify if results are equal
        assert are_matrices_equal(result_standard, result_strassen), f"Results differ for n={n}"

        print(f"Matrix size {n}x{n} -> Standard Time: {standard_time:.6f}s, Strassen Time: {strassen_time:.6f}s")

# Run the comparison
compare_execution_times()
