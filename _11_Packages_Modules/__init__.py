# chr()*   Return the string representing a character.
# for va in range(65,123):
#     val=chr(va)
#     if 'A'<=val<='Z' or 'a'<=val<='z':
#         print(val,end=' = ')
#         print(ord(val),end=', ') #ord function in python


#
#########frozen set in python #############
# v=[1,2,3,4,5,1,2,3]
# val=frozenset(v)
# print('output od frozenset =',val)
# ###############asciii function in python#################
#
# va=ascii('gopi kidd')
#
# print(va)
##############bin() function in python############

# va=11
# out=bin(va)
# print(out)


###############lambda with map() #####################

# val=[1,2,3,4,5,6]
#
# result=list(map(lambda x :x**x ,val))
# print(result)

############lambda with filter()###########
# val=[1,2,3,4,5,6,7,8,9]
#
# result=set(filter(lambda x:x%2==0,val))
#
# print(result)
###########lambda with reduce() ##############
# from functools import reduce
#
# li=[10,20,30,40,50]
#
# result=(reduce(lambda x ,y:x+y,li))
#
# print(result)
###############fibnocci serice############
# rang=int(input("enter the range value"))
# fib1=0
# fib2=1
# fib3=fib1+fib2
# for i in range(0,rang):
#     fib1=fib2+fib1
#     fib2=fib3
#     fib3=
#     print(fib3 , end= ' ')
#
#######shorted() in python ###########
# li=[1,2,6,7,8,4,3,9]
# li.sort(reverse=True)#this short function directly short the same variable
# print(li)
# l=sorted(li)#this sorted function short the given value and assign one new variable
# print(l)
############  zip() in python #############
# key=[1,2,3,4,5]
# value=['gopi','surya','sakara','prabu','kamali']
# for i, (value,key) in enumerate(zip(value,key)):
#     print(i,value,key)
#
########zip() normal in python ###########
# val=[1,2,3,45,5]
# val1=['gopi','surya','sakara','prabu']
# result=zip(val,val1)
# print(list(result))

########all() and any () in python #################
# in_put=[1,2,10,4,5,0,8]
# result =any(in_put)  #any () return any one of  the value will be true it return true all the value false it will return false
# print(result)
# result1=all(in_put) #all () return all the value true that only return true otherwise return false
# print(result1)

############iter () in python ###########
# li=['apple','orange','banana','jackfruit']
# x=iter(li)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x)) #it will return stopiteration error


# ##############eval() in python #############
# a=eval('print(5)')
# val=eval("5*10")
# v=eval("5+10+15")
# print(val)
# print(v)

# factorial() renamed as fact
# from math import *
# print(factorial(5))
#
# exec('print(fact(6))', {'fact': factorial})
# exec('print(val)')
# x=isinstance(12,(int))
# print(x)
# y=isinstance(10.55,(float))
#
# print(y)#The isinstance() function returns True if the specified object is of the specified type, otherwise False.
# class demo():
#     name='Gopi'
#     age=24
# class demo1(demo):
#     native='salem'
# x=issubclass(demo1,demo)
# print(x)#The issubclass() function returns True if the specified
# # object is a subclass of the specified object, otherwise False.
################abs() in python#######
# num=abs(-7.5)
# num1=abs(33)
# num2=abs(True)
# print(num)
# print(num1)
# print(num2) # The abs () function returns the absolute value of the specified number.)
# def sum1(li):
#     out=0
#     for i in li:
#         out+=i
#     print(out)
#
# l=(1,2,3,4,)
# sum1(l)

# di1={'a':1,'b':2,'c':3}
# di2={'a':1,'d':3,'c':3}
# di3={}
# for key in di1.keys():
#     if key in di2.keys():
#         di3+=di1[key]
# print(di3)
