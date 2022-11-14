import time

def calc_time(func):  # func=cube_it
    def wrapper(*args):   # *agrs= nums , **kwargs={}
        start=time.time()
        r=func(*args)
        end=time.time()
        print(func.__name__ + " took : "+ str((end-start)*1000) + ' milli seconds')
        return r
    return wrapper

@calc_time
def square_it(nums):
    result=[]
    for n in nums:
        result.append(n**2)
    return result

@calc_time
def cube_it(nums):
    result=[]
    for n in nums:
        result.append(n ** 3)
    return result

data=range(1,1000001)
square_it(data)
cube_it(data)