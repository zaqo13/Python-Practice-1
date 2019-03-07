# #########
# ##Q.1, range is given, no is divided by 7 but not divisible by 5
# ########
# l=[]
# for i in range(2000,3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
# print('divisible by 7 but not multiple of 5', '/' .join(l) )
# print('divisible by 7 but not multiple of 5','/'.join(l))

# ##########
# ##Q.2, factorial of number enter by console
# ##########
# def fact(x):
#     if x==0 or x==1:
#         return 1
#     a=x*fact(x-1)
#     return a
# x=int(input('enter the no'))
# print(fact(x))

# ############
# ##Q.3 conver input console into tuple and list
############
# v=input('Enter the no')
# print('Type of console input is',v,type(v))
# l=v.split(",")
# t=tuple(l)
# print(l,type(l))
# print('type of l[1] is',type(l[1]))
# print(t,type(t))
# print('Type of t[1] is',type(t[1]))

# ##########
# ##Q.4, dict{}, d[i]=i*i, To find suare of ggiven nos. and store them in dict()
# ##########
# n=int(input('enter the nos'))
# d=dict()
# for i in range(1,n+1):
#     a=i*i
#     d[i]=a
#     print('%i square is %a'%(i,a))
# print('Pair of nos. & its square is',d)

##########
##Q5 L1, simple class withtwo methods
##########
# class ioString(object):
#     def __init__(self):
#         self.s=" "
#     def getString(self):
#         self.s=input('Enter the string here\n')
#     def printString(self):
#         print(self.s.upper())
# strobj=ioString()
# strobj.getString()
# strobj.printString()

##########
##Q.6 L3,formula based: two variable constant, one is supplied by user console
##########
# import math
# c=50
# h=30
# value=[]
# iteams=[x for x in input('the values for d is').split(',')] #input console list seperated with comma
# # print(type(iteams))
# print('the formula is sqrt(2*c*(d)/h)')
# for d in iteams:
#     value.append(str(int((round(math.sqrt(2*c*float(d)/h))))))
# print(' the ans is ', ','.join(value))

##########
##Q.7, sort the text seperated by comma
##########
# text=[x for x in input('enter the text here\n').split(',')]
# text.sort()
# print('sorted text',text)
# text.reverse() #use this to make reverse sort(i.e. accending/decending)
# print('reverse sorted text',text)

##########
##Q.8, input from console, multiple lines of characters,then make them captilize and print them
#########
# value=[]
# while True:
#     t=input('')
#     if t:
#         value.append(t.upper())
#     else:
#         break
#
# print('Capitalize text is:\n','\t'.join(value),type(value))
# # or
# # for sent in value:
#     # print('capitalize text is ',sent, type(sent))

##########
##Q.9, accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
##########
# s=input('Enter the text here')
# words=[word for word in s.split(' ')]
# words1=(sorted(set(words)))
# print(' '.join(words1),type(words))

##########
##Q.10, input==sequence of comma separated 4 digit binary numbers
##      cond==input divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
##########
# value_b=[]
# value_i=[]
# inb=[x for x in input().split(',')]
# print('Ans= (input % 5 ==0) ')
# for p in inb:
#     intp=int(p,2)
#     if intp % 5==0:
#         value_i.append(intp)
#         value_b.append(bin(intp))
# print('the ans in binary is',value_b)
# print('the ans in decimal is',value_i)
# print('the ans using join',''.join(str(value_i)))
# for val in value_i:
#     a=bin(val)
#     b=int(a,2)
#     print('ans using for loop',a,b)

##########
##Q.11, o/p==all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
##########
# val=[]
# for i in range (1000,3001):
#     s=str(i)
#     if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
#         val.append(s)
# print(','.join(val))
## print('values are',val)

##########
##Q.12, accepts a sentence and calculate the number of letters, digits and spaces
##########

# sp=0
# s=input("Enter the text here")
# d={'Alpha':0, 'Numbers':0}
# for x in s:
#     if x.isdigit():
#         d['Alpha']+=1
#     elif x.isalpha():
#         d['Numbers']+=1
#     elif x.isspace():
#         sp+=1 #sp=sp+1
#     else:
#         pass
# print('Total Numbers',d['Numbers'])
# print('Total alphabates',d['Alpha'])
# print('Total spaces', sp)
# print(d)

##########
##Q.13, a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a
#### introducing try,assert,finally,function...etc
##########
#
# def fun(i):
#     try:
#         i=int(i)
#         assert (i > 0), 'Given no. is negative'
#         if i:
#             a = i
#             aa = int('%s%s' % (a, a))
#             aaa = int('%s%s%s' % (a, a, a))
#             aaaa = int('%s%s%s%s' % (a, a, a, a))
#             v = a + aa + aaa + aaaa
#             print('The answer is',v)
#     finally:
#         print('Thank you :)')
# s=fun(input("Enter the no here"))

##########
##Q.14, Use a list comprehension to find odd number in a list.
#### introducing- List comprehension...etc
##########
# v=input('enter the no seperated by comma')
# s=[x for x in v.split(',') if int(x)%2!=0]
# print('Here is odd numbers',s)

##########
##Q.14, a program that computes the net amount of a bank account based a transaction log from console input
# eg. d 200
#     w 100
# here, d is for deposit and w is for withdrawal
#########
#
# netamt=0
# trans_count=0
# print('Enter the transaction details here one by one')
# while True:
#     s=input('')
#     if not s:
#         trans_count+=1
#
#         break
#     v = s.split(' ')
#     opr = v[0]
#     amt = int(v[1])
#     if opr == 'w':
#         netamt -= amt
#     elif opr == 'd':
#         netamt += amt
#     else:
#         pass
# print('Your balance is', netamt)

################
###Topic:- Class(oop)
#################

# class MyClass(object):
#     instance_count = 0
#     def __init__(self, value):
#         self.__value = value
#         MyClass.instance_count += 1
#         print("instance No {} created".format(MyClass.instance_count))
#         # print('inst no %d created'%MyClass.instance_count)
#     def aMethod(self, aValue):
#         self.__value *= aValue
#     def __str__(self):
#         return "A MyClass instance with value: " + str(self.__value)
#     def __del__(self):
#         MyClass.instance_count -= 1
# myinst=MyClass(43)
# myinst.aMethod(10)
# print(myinst)
# print(MyClass.instance_count)
# inst = MyClass(44)
# print(MyClass.instance_count)
# del(inst)
# print(MyClass.instance_count)

###########
### Area of Circle
##########

#
# class Circle1:
#     def __init__(self, radius):
#         self.radius = radius
#     def setRadius(self,newValue):
#         if newValue >= 0:
#             self.radius = newValue
#         else: raise ValueError("Value must be positive")
#
#     def area(self):
#         return 3.14159 * (self.radius ** 2)
# c2=Circle1(5)
# print(c2.radius)
# print(c2.area())
# c2.setRadius(-5)
# print(c2.area())
# class Circle2:
#      def __init__(self, radius):
#          self.__radius = radius
#
#      def __setRadius(self, newValue):
#          if newValue >= 0:
#              self.__radius = newValue
#          else: raise ValueError("Value must be positive")
#
#      radius = property(None, __setRadius)
#
#      @property
#
#      def area(self):
#          return 3.14159 * (self.__radius ** 2)


# c3=Circle2(5)
# print(c3.area)
# c3.radius=-10
# print(c3.area)

############
### Bank Proj.
###########
# class empl():
#     emplCount=0
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         empl.emplCount +=1
#     def disEmplCount(self):
#         print('The Employee count is {}'.format(empl.emplCount))
#     def disEmplInfo(self):
#         print("name:"+self.name,'\nsalary:'+str(self.salary))
#
# emp1=empl('sagar',5000)
# emp1.disEmplCount()
# emp1.disEmplInfo()


#######To be continued...
