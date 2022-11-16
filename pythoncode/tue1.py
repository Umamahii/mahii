import timeit
# code snippet to be executed only once
mysetup = "from math import sqrt"
# code snippet whose execution time is to be measured
mycode = '''
def example():
    mylist = [1,2,3,4]
    for x in range(100):
        mylist.append(sqrt(x))
'''
# timeit statement
print (timeit.timeit(setup = mysetup,
                     stmt = mycode,
                     number = 100000))