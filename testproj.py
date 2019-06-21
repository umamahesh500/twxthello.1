#MATRIX MULTILICATION
from numpy import *
a1 = [[9,2,3],
       [4,5,6]]
a2=[[7,8],
     [9,10],
     [11,12]]
arr=[[0,0],
        [0,0]]
for i in range(2):
    for j in range(2):
        for k in range(3):
            arr[i][j] += a1[i][k]*a2[k][j]

for r in arr:
     print(r)

# #IMMUTABLE OBJECT
# def update(x):
#     print('Value of x ',x)
#     print('Memory Address of x before update',id(x))
#     x=8
#     print('Value of x after update',x)
#     print('Memory Address of x after update',id(x))
#
# a=10
# print('Value of a ',a)
# print('Memory Address of a before update',id(a))
# update(a)
# print('Value of a ',a)
# print('Memory Address of a after update',id(a))
#
# #MUTABLE OBJECT
# def update(x):
#     print('inside function, before update',spam)
#     print('Memory address of list inside function, before update',id(spam))
#     spam[1]=-3
#     print('inside function, after update',spam)
#     print('Memory address of list inside function, after update',id(spam))
#
#
# spam=[1,2,3]
# print('Items in list',spam)
# print('Memory address of list',id(spam))
# update(spam)
# print('Items in updated list',spam)
# print('Memory Address of updated list',id(spam))
#POSITION,KEYWORD,DEFAULT,VARIABLE LENGTH
# def add(a,*b):
#     print(a)
#     print(b)
#     c=0
#     for i in b:
#         c=c+i
#     print(c+a)
#
# add(5,6,34,78)
#KEYWORD VARIABLE LENGTH ARGUMENTS
# def persondetails(name,**data):
#     print(name)
#     print(data)
#     for i,j in data.items():
#         print(i,j)
#
# persondetails('mahesh',age=24,city='kurnool',mob=9087)
#FIBONACCI SERIES
# def fibonacci(n):
#     a=0
#     b=1
#     if(n==1):
#         print(a)
#     elif(n>1):
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             if(c>100):
#                 return
#             else:
#                 print(c)
#
#     else:
#         print("invalid:please check the enterd value")
#
# fibonacci(100)
#PASS LIST TO FUNCTION

# def count(lst):
#     e=0
#     o=0
#     for i in lst:
#         if i%2==0:
#             e+=1
#         else:
#             o+=1
#     return e,o
#
# lst=[10,20,21,22,23,34,45,66,78,89,91]
#
# e,o=count(lst)
# print("EVEN:{} and ODD={}".format(e,o))
# i=int(input("enter value"))
# f=1
# while i>0:
#     f=f*i
#     i-=1
# print(f)
#RECURSION
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# result = fact(6)
# print(result)
#DECORATORS
# def div(a,b):
#     print(a/b)
#
# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#             return func(a,b)
#     return inner
# div= smart_div(div)
# div(2,4)
# from calc import *
# def main():
# a=9
# b=17
# c= add(a,b)
# d=sub(a,b)
# e=mul(a,b)
# print("add={},sub={},mul={}".format(c,d,e))
# print(__name__)
#
#
# main()
# x=int(input("enter the number"))
# i=1
#
# if i<=x  :
#     for a in range(1,x):
#
#         if x%a==0:
#             i+=1
#
#
#
# if i>2:
#         print("not prime")
#
# else:
#         print("prime")

# num = 9
# for i in range(2, (num // 2)):
#     if num % i == 0:
#         print("Not Prime")
#         break
# else:
#     print("Prime")
# class student:
#
#     school='telusko'
#     def __init__(self,m1,m2,m3):
#         self.m1=m1
#         self.m2=m2
#         self.m3=m3
#     def avg(self):
#         return (self.m1+self.m2+self.m3)/3
#
#     @classmethod
#     def getschool(cls):
#         return cls.school
#     @staticmethod
#     def info():
#         print("This is the school name")
#
# s1=student(12,13,14)
# s2=student(34,45,46)
#
# print(s2.avg())
# print(student.getschool())
# student.info()
# class student:
#     def __init__(self,name,rollno):
#         self.name = name
#         self.rollno=rollno
#         self.lap=self.laptop()
#     def show(self):
#         print(self.name,self.rollno)
#         self.lap.show()
#     class laptop:
#         def __init__(self):
#             self.brand='h.p'
#             self.cpu='i5'
#             self.ram =8
#
#         def show(self):
#             print(self.brand,self.cpu,self.ram)
#
#
# s1=student('naveen',2)
# s1.show()
# class Pycharm:
#     def execute(self):
#         print('compiling')
#         print('running')
#
# class editor:
#     def execute(self):
#         print("spell check")
#         print('compiling')
#         print('running')
#
#
# class laptop:
#     def code(self,ide):
#         ide.execute()
#
#
#
# ide=editor()
# lap1=laptop()
# lap1.code(ide)
# def topten():
#
#     n=1
#     while n<=3:
#
#
#         yield n
#         n+=1
#
#
# values=topten()
# for i in values:
#     print(i)
# import mysql.connector
# mydb=mysql.connector.connect(host="local host",user="root",psswd="Mahesh@123")