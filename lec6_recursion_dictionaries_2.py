###########
##Multiplication- Iterative soln
###########
def mult_iter(a,b):
    result=0
    while b>0:
        # print(b)
        result +=a
        # print('result is',result)

        b -=1
    return result
a=4
b=5
new=mult_iter(a,b)
# print(new)

###########
##Multiplication Recursive soln
###########
def mult_rec(a,b):
    if b==1:
        new1=a
        # print('if block',new1)
        return new1
    else:
        new=a + mult_rec(a, b - 1)
        # print(new)
        return new
new=mult_rec(4,5)
# print('recursive soln',new)

#############
##the tower of hanoi
#############
def printmove(fr, to):
     print('mov from '+str(fr) +' to ' +str(to))
def towers(n, fr, to,spare):
    if n==1:
        printmove(fr,to)
    else:
        towers(n-1,fr,spare,to)
        towers(1,fr,to,spare)
        towers(n-1,spare,to,fr)

#print(towers(3,'A','B','C'))


###########
##Fibonacci series
###########
def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
a=fib(5)
print(a)


def fibo(x):
    if x==1 or x==0:
        return 1
    else:
        return fibo(x-1)+ fibo(x-2)

print(fibo(5))
