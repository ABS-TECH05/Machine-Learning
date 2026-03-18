'''
Real-World Example: Multiprocessing for CPU-bound Tasks
Scenario: Factorial Calculation
Factorial calculations, especially for large numbers, 
involve significant computational work. Multiprocessing 
can be used to distribute the workload across multiple 
CPU cores, improving performance.

'''

import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

# Function to compute factorials of a given numbers
def fact(n):
    print(f'Factorial of a number {n}: ')
    result = math.factorial(n)
    print(f"Factorial of {n} is {result}")
    return result

if __name__ == '__main__':
    n = [5000, 6000, 7000, 8000]
    start_time = time.time()
    
    ## create a pool worker processes
    with multiprocessing.Pool() as pool:
        results = pool.map(fact, n)
        
    end_time = time.time()
    
    print(f'Result ; {results}')
    print(f'Time taken : {end_time - start_time} seconds')