###  Multiprocessing with ProcessPoolExecutor

import time
from concurrent.futures import ProcessPoolExecutor

def square_number(number):
    time.sleep(2)
    return f'Square : {number**2}'

numbers = [1,2,3,4,5,6,7,8,9,11,2,3,12,14]

if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, numbers)
        
    for i in results:
        print(i)