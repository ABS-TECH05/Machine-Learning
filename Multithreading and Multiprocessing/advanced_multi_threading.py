### Multithreading With Thread Pool Executor

import time
from concurrent.futures import ThreadPoolExecutor

def print_number(number):
    time.sleep(1)
    return f'Number : {number}'

numbers = [1,2,3,4,5,6,7,8,9,0,1,2,3]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)
    
for i in results:
    print(i)