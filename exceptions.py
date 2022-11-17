import sys
"""
Four Clauses:
=============
try
except
else
finally
"""

try:
    with open('days.txt') as fo:
        print(fo.read())
    res=10/5
    print(f"division of 10 by 2 is : {res}")
    add=5+6
    print(f"Sum of 5 and 6 is :{add}")
    #print(emp[0])
    age=int(input("\n\nEnter your age:"))
    if age<0 or age>100:
        raise ValueError("Age should be between 0-100")
    print("Age is :", age)
except FileNotFoundError as e:
    print("ISSUE WITH THE FILE.",e)
    sys.exit()
except ZeroDivisionError as e:
    print("Division Error.",e)
except TypeError as e:
    print("Received Type Error.",e)
except NameError as e:
    print("Name Error .",e)
except Exception as e:
    print("Caught new exception.",e)
else:
    print("ELSE: No Exception, Hence else runs!")
finally:
    print("FINALLY: Run always irrespective of the exception!")


print ("-----------------NEXT LINE -----------------------")