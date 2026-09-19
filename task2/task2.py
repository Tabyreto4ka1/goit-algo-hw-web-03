from multiprocessing import cpu_count, Pool
from time import perf_counter

def factorize(*numbers):            #Функція яка створює процеси і створює список списків для чисел
    start=perf_counter()
    with Pool(processes=cpu_count()) as pool:
        numbers_to_return=pool.map(action_without_processes,numbers)

    print(perf_counter()-start,"-Час виконання з процесами")
    return numbers_to_return



def factorize_without_processes(*numbers):      #Така сама як factorize але без процесів    
    start=perf_counter()
    numbers_to_return=[]
    for i in numbers:
        numbers_to_return.append(action_without_processes(i))

    print(perf_counter()-start,"-Час виконання без процесів")
    return numbers_to_return

def action_without_processes(number):               
    start_count=1
    numbers_remainder=[]
    while start_count!=number+1:
        if number%start_count==0:
            numbers_remainder.append(start_count)
            start_count+=1
        else:
            start_count+=1
    return numbers_remainder

if __name__=="__main__":

  
    
    
    a, b, c, d  = factorize(128, 255, 99999, 10651060)

    

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    a, b, c, d  = factorize_without_processes(128, 255, 99999, 10651060)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]