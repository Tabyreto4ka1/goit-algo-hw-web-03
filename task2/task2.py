from multiprocessing import Process, Queue
from time import perf_counter



def factorize(*numbers):            #Функція яка створює процеси і створює список списків для чисел
    q=Queue()
    numbers_to_return=[]
    processes=[]
    for i in numbers:
        pr=Process(target=action, args=(i,q))
        pr.start()
        processes.append(pr)

    for _ in numbers:
        numbers_to_return.append(q.get())

    for pr in processes:
        pr.join()

    return numbers_to_return

def action(number,q):               #функція яка  знаходить потрібні значення і додає до списку, який ми потім додає до q
    start_count=1
    numbers_remainder=[]
    while start_count!=number+1:
        if number%start_count==0:
            numbers_remainder.append(start_count)
            start_count+=1
        else:
            start_count+=1
    q.put(numbers_remainder)


if __name__=="__main__":

    start= perf_counter()
    

    a, b, c, d  = factorize(128, 255, 99999, 10651060)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    end = perf_counter()
    print(end - start,"- час виконання")