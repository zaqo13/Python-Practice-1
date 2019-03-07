# # def even_no(i):
# """"INput: i, positive no, ans= even/odd"""
# i= int(input())
# # print(i)
# # print('with return')
# rem= i%2
# if rem==0:
#     print('even no')
# else:
#     print('odd no')
#
# def ed( i ):
#     """
#     Input: i, a positive int
#     Returns True if i is even, otherwise False
#     """
#     # rem = int(input(i))
#     # print('',rem)
#     # rem = i % 2
#     return i%2 == 0
# ed(12)

#
# def is_even_with_return( i ):
#     """
#     Input: i, a positive int
#     Returns True if i is even, otherwise False
#     """
#     print('with return')
#     remainder = i % 2
#     return remainder == 0
#
# # i=4  ?
# # z=is_even_with_return()   ?
# # is_even_with_return(3)    ?
# print(is_even_with_return(4) )



# a =  int(input())
# print('',a)
# guess=guess + 1
# if a==guess:


# def f(x):
#     x=x+1
#     print('in f(x): x=',x)
#     return (x)
# x=3
# z=f(x)
# print('x',x)

# def fun1():
#     print('inside fun1')
#
# def fun2(y):
#     print('inside fun2',y)
#     # y +=1
#     return (y)
#
# def fun3(z):
#     print('inside fun3')
#     return z()
# print (fun1())    # taks no parameter
# print(fun2(2))    # take one parameter
# print(5+fun2(3))
# print(fun3(fun1))  # try to implement such type (one_parmeter+one_function)
#  # take one parameter and another function


# def f(y):
#     x = 1
#     x +=1
#     print('y')
# x=5
# f(x)
# print(x)

# def f(y):
#     x=1
#     x+=1
#     print(x)
# x=5
# f(x)
# print(x)


# def g(y):
#     print('im in the code of function',y)
#     # x=x+1
#     print(x+1)
#     return (x)
# x=5
# # g(x)
# # print('im global',x)
# print('direct passing the 'g(3))

#
# def h(y):
#     x +=1   #inside a function, can access a vaiable defind outside
#     print('im in the scope',x)  #and inside a fun, cannot modify a vaiable defined outside
# x=5
# h(x)
# print('im in the global',x)
# # this will give an error of 'UnboundLocalError'

# def h(y):
#     y +=1
#     print(y)
# y=5
# h(y)

# def g(x):
#     def h():
#         x= 'abc'
#         print('im in the scope of h',x)
#     x=x+1
#     print('im in the scope of g =',x)
#     h()
#     return x
# x=3
# print('this is global value of x=',x)
# z=g(x)
# print('Due to ',z)


for i in range(20):
    z= i%2
    print(z)
