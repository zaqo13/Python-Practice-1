list1,list2=[123,'abc','zara','zaqo',123],[456,'xyz']
# # print('len():',len(list1))
# # print('append():',list1.append(23),list1)
# # print('count():',list1.count(123))
# # print('remove():',list1.remove(123),list1)
# # print('insert():',list1.insert(1,123),list1)
# # print('extend():',list1.extend([15,645,15,645,15,'dfs']),list1)
# print('index():',list1.index(123,-1),list1)
# s=list1.index(123,-1)
# print('index number of 123',s)
# # print('pop():',list1.pop(),list1)
# # print('pop():',list1.pop(2),list1)
# # list1.reverse()
# # print(list1)
# #
# #
# dict={'name':'zaqo','age':7,'class':'first'}
# # dict['school']='narmada'
# # print(dict['age'])
# # print(dict['school'])
# # print('the dict is: %s%s' %(dict,dict))
# # print('len of dict %d' %len(dict))
# # print('equivalent dict: %s' %str(dict))
# # a=dict.copy()
# # print('a is',a)
seq=('college','group','div')
b=dict.fromkeys(seq)
# print(seq)
# print('new dict is: %s'%b)

# # print('updated dic is %s' %dict.fromkeys(seq,100))
# #
# #
# # dict={'name':'zaqo','age':7,'class':'first'}
# # b=('age','sex','location')
# # a=('age')
# # print('Answer: %s'% dict.get('age','ans not found'))
# # a=dict.items()
# # print('dict type when use iteams:',a,type(a))
# # # del dict
# # print('del dict',a)
# # # print('dict.iteams :%s'%dict.items())
# # # print('dict.keys():',dict.keys())
# # # del dict['name']
# # # print(dict)
# # print('all keys if dict:',dict.keys())
# # print('all values of dict:%s'%dict.values())
# #
# # dict={'name':'zaqo','age':7,'class':'first'}
# # dict2={'location':'pune'}
# # print('dict.setdefault():', dict.setdefault('location', 'Not_found'))
# #
# # print('for updating the dict form another dict: ', dict,dict.update(dict2))
# # print('dict.setdefault():', dict.setdefault('location', 'Not_found'))
#
# def changeme(a):
#     '''this is function'''
#     mylist=[1,2,3,4]
#
#     print('inside the function',mylist)
#     return
# mylist=[11,22,33,44]
# changeme(mylist)
# print('outside the function',mylist)
#
# def pritme(str,no):
#     print('inside the fun',str,no,type(str),type(no))
# pritme(13,'sre')

# def vartupe(arg1,*arg2):
#     # print(arg1)
#     print(arg2)
#     for var in arg2:
#         print('insidefor loop',var)
#     return
# vartupe(11,23,45,66)

# def sum(arg1,arg2):
#     total=arg1+arg2
#     print('inside fun',total)
#     return total
# a=sum(10,20)
# print('outside fun a',a)

# total=0
# def sum2(arg1,arg2):
#     total=arg1+arg2
#     print('inside fun',total)
#     return total
# sum2(10,20)
# print('outside fun',total)

# money=200
# def addmoney():
#     global money
#     locals()
#     print(globals())
#     money=money+10
# print('\nsimple money',money)
# addmoney()
# print('asa',a)
# print('outside the fun',money)

# import math
# contains=dir(math)
# print(contains)

# def fibo(p,d):
#     if p in d:
#         return d[p]
#     else:
#         ans= fibo(p-1,d)+fibo(p-2,d)
#         d[p]=ans
#         return ans
# def fib(n,d):
#     p=int(n-1)
#     print('the fib of %d is'%n,fibo(p,d))
# d={1:1,2:2}
# fib(10,d)


# a=4
# print(a)
