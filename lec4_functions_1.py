#########################
## EXAMPLE: combinations of print and return
## Python Tutor link: http://www.pythontutor.com/
#########################
# def is_even_with_return( i ):
#     """
#     Input: i, a positive int
#     Returns True if i is even, otherwise False
#     """
#     # print('with return')
#     remainder = i % 2
#     return remainder == 0 #the output of comparision is boolean(i.e. True/False)
#                           #so 'return' return the True/False for calling function....
#
# z=int(input('Enter the no. '))
# z=is_even_with_return(3)
# print(z)
# print('is remender == 0, if no. is divided by 2 ? \nAns =',is_even_with_return(z) )


# def is_even_without_return( i ):
#     """
#     Input: i, a positive int
#     Does not return anything
#     """
#     print('without return')
#     remainder = i % 2
#
# is_even_without_return(3)
# print(is_even_without_return(3) )

##############
## Simple is_even function definition
##############

# def is_even( i ):
#     """
#     Input: i, a positive int
#     Returns True if i is even, otherwise False
#     """
#     remainder = i % 2
#     return remainder == 0

# # Use the is_even function later on in the code

# print("All numbers between 0 and 20: even or not")
# for i in range(20):
#     if is_even(i):
#         print(i, "even")
#     else:
#         print(i, "odd")
#
# #########################
# ## EXAMPLE: applying functions to repeat same task many times
# #########################
# def bisection_cuberoot_approx(x, epsilon):
#     """
#     Input: x, an integer
#     Uses bisection to approximate the cube root of x to within epsilon
#     Returns: a float approximating the cube root of x
#     """
#     low = 0.0
#     high = x
#     guess = (high + low)/2.0
#     while abs(guess**3 - x) >= epsilon:
#         if guess**3 < x:
#             low = guess
#         else:
#             high = guess
#         guess = (high + low)/2.0
#     return guess
#
# x = 1
# while x <= 10000:
#     approx = bisection_cuberoot_approx(x, 0.01)
#     print(approx, "is close to cube root of", x)
#     x *= 10
#
#
# #########################
# ## EXAMPLE: functions as arguments
# # #########################
# def func_a():
#     print('inside func_a')
#
# def func_b(y):
#     print('inside func_b')
#     return y
#
# def func_c(z):
#     print('inside func_c')
#     return z()
#
# print(func_a())
# print(5+func_b(2))
# print(func_c(func_a))


#
# #########################
# ## EXAMPLE: returning function objects
# #########################
# def f():
#     def x(a, b):
#         return a+b
#     return x
#
# # the first part, f(), returns a function object
# # then apply that function with parameters 3 and 4
# val = f()(3,4)
# print(val)
#
#
#
# #########################
# ## EXAMPLE: shows accessing variables outside scope
# #########################
# def f(y):
#     x = 1
#     x += 1
#     print(x)
# x = 5
# f(x)
# print(x)

# def g(y):
#     print(x)
#     print(x+1)
# x = 5
# g(x)
# print(x)

# def h(y):
#     pass
#     #x += 1 #leads to an error without line `global x` inside h
# x = 5
# h(x)
# print(x)
#
#
# #########################
# ## EXAMPLE: complicated scope, test yourself!
# #########################

# def f(x):
#    x = x + 1
#    print('in f(x): x =', x)
#    return x
#
# x = 3
# z = f(x)
# print('in main program scope: z =', z)
# print('in main program scope: x =', x)
#
# def g(x):
#     def h(x):
#         x = x+1
#         print("in h(x): x = ", x)
#     x = x + 1
#     print('in g(x): x = ', x)
#     h(x)
#     return x
#
# x = 3
# z = g(x)
# print('in main program scope: x = ', x)
# print('in main program scope: z = ', z)
