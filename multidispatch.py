from multipledispatch import dispatch

@dispatch(int, int)
def product(first, second):
    print( first * second)

@dispatch(int,int, int)
def product(first, second, third):
    print( first * second * third)


@dispatch(float, float, float)
def product(first, second, third):
    print( first * second * third)  

product(2,3)
product(2,3,4)
product(1.5,2.5,3.0)



