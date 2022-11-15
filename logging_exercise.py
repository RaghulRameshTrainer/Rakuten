import logging

LOG_FORMAT='%(levelname)s : %(asctime)s  - %(message)s'
logging.basicConfig(filename='output_calc.log',level=logging.DEBUG,format=LOG_FORMAT,filemode='w')
logger=logging.getLogger()

def addition(x,y):
    "Addition function"
    return x+y

def subract(x,y):
    "Subraction function"
    return x-y

def multiplication(x,y):
    "Multiplication function"
    return x*y

def division(x,y):
    "Division function"
    return x/y

a=10
b=20

add_result=addition(a,b)
logger.info(f'Addition of {a} and {b} is {add_result}')
sub_result=subract(a,b)
logger.info(f'Subraction of {a} and {b} is {sub_result}')
mul_result=multiplication(a,b)
logger.info(f'Multiplication of {a} and {b} is {mul_result}')
div_result=division(a,b)
logger.info(f'Division of {a} and {b} is {div_result}')