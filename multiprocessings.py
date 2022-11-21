import multiprocessing
from time import sleep

def calc_square(nums):
    for n in nums:
        print('Square:' + str(n*n))
        sleep(1)

def calc_cube(nums):
    for n in nums:
        print('Cube:'+str(n*n*n))
        sleep(1)

if __name__=='__main__':
    data=[1,2,3,4,5]
    p1=multiprocessing.Process(target=calc_square,args=(data,))
    p2=multiprocessing.Process(target=calc_cube,args=(data,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("DONE!")