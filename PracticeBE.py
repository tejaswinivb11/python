#python basics
import itertools
from collections import deque
import sys
import math
import random
#[ ,end =" "] to print in the same line
#else block in loops is executed only when the break statement is not used 

#iter() and next() : _iter__(): The iter() method is called for the initialization of an iterator. This returns an iterator object
#__next__(): The next method returns the next value for the iterable.
# for loop internally uses the iter() to iterate over an object
# for loop when you need to iterate over a sequence of values and access the index of each value or when you need to iterate over the sequence and modify the values.
#iter example
def ite():
    li = [1,3,4,5]
    ie = iter(li)
    print(next(ie))
    print(next(ie))
    
#Dunder or magic methods in python:  Magic methods in python are special methods that are invoked when we run any ordinary python code. To differentiate them with normal functions, they have surrounding double underscores.
#commonly used for operator overloading[ex: '+' operator used for both the concatination and the addtion operation]. 
#***these methods are used to give the functionality to the user defind objects***
#Destructors are called when an object gets destroyed:__del__()
def magic_meth():
    # a=b=10
    # c=a.__add__(b)
    # print(c)
    print(dir(int))
class MyClass:
   # def __new__(cls):
        # print("Creating a new MyClass object...")
        # return super().__new__(cls)

    def __init__(self,name:str) -> None:
        self.name = name
        print(self.name)


    #__repr__ method in Python defines how an object is presented as a string.{} used this
    def __repr__(self):    
        return "huh{}sbfube".format(self.name)
#looping techniques on data types 
#enumatare: enumerate() returns a tuple containing a count, the position index and corresponding value can be retrieved at the same
#items(): to get key and value at a time
#zip():To loop over two or more sequences at the same time, 
#reversed()
# sorted() 
    def enm():
        li=[1,2,3,4,5,6,6]
        for i,j in enumerate(li):
            print(i,"fgfg",j)  

# module “itertools“. 
    # 1. module “itertools“. 
    # 2. chain(iter1, iter2..)
            
def iter_tool()->None:
    li= [2,3,4,5]  
    print(list(itertools.accumulate(li)))

#set and frozenset:sets are mutable where as the the frozen set are immutable,unique elements and it always prints in the assending order
def sets()->None:
    se=set([12,3,4,6,4])
    sf=frozenset([2,3,4,5,6,1,1])
    print(len(se))#as set cannot contain the duplicate elements the len function does not count the duplicate elements 
    se.add(8)
    se.add((3,6,7))
    print(se)
    print(sf)
    se.discard(5)#does not rises the exception
    se.remove(4)#rises the exception 
    s = set('hello')
    b= set('bvcxzo')
    print(s^b)# | & - ^
    
    print(sum(range(1,7,2)))#range function 
    #packing and unpacking : accessing the sequence of elememnts and assissing it to different variables
    #packing : can be usedd in the function when we dont known how many arguments to be passed to the function
    #unpacking: ex: assing a list as function argument
    dic={'1':'name','2':'tyty'}
    for i,j in dic.copy().items():
        if i == 1:
            del dic[i]

#match statements [switch statement]
def checker(ch):
    match ch:
        case 23:
            print(90)
        case _:
            print("done")
#   arguments have 2types : 1) standard arguments
            #2)positional: where the arguments must be passesd in the same order they are mentioned in the function defination.[positional only arguments are marked using only '/']
#            3)keyword: Keyword arguments are arguments that are passed to a function by their name. Keyword-only arguments are defined after the *
#           def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       4)Arbitrary Argument Lists:These arguments will be wrapped up in a tuple
        #[Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments,]
#default argumnet : The default value is evaluated only once.
def fun(i,l=[]):#the list can be initilized to none to make it work normally
    l.append(i)
    return l

#keyword argument
#default argument 
def fu(val,i=10,j=29):
    print(val,i,j)
#print(fu(val ='t',j=90))
#[*arg] : recives the tuple as an argument. [**args] :recives the dictionaries as an argument
#lammbda: Lambda functions can be used wherever function objects are required
def lam(n):
    return lambda x:x+n
#passing arguments to the objects 
# g=lam(45)
# print(g(45)) 

#queues using collection function 'deque'
def que():
    queue = deque([1,2,3,4])
    queue.append(5)
    print(queue.popleft())

#List Comprehensions
li = [x**2 for x in range(10)]

#filter, reduce and map

#recurssion and tail recurssion: tail recurssion is where the recurssion is the last program and there is no  other function after it.
def recu(low,high,arr,key)->int:
    mid=(low+high)//2
    if arr[mid] == key:
        #rint(arr[mid])
        print("found")
        return mid+1
    if key<arr[mid]:
        return recu(low,mid-1,arr,key)
    return recu(mid+1,high,arr,key)
#__init__.py : file is a special file in Python that is used to initialize a package.

#classes and objects in python 
#self: its customary in python, Python to use self as the first parameter in instance methods.
#__init__():is a constructor
#__str__():object should be represented as a string.
#Instance variables are for data, unique to each instance and class variables,whose value is assigned inside a constructor or using the methods
#eveery class is by default invoked by the object class
class dog(object):
    def __init__(self) -> None:
        self.name = "nev"
        print("")
    @staticmethod
    def fun(name)-> str:
         return name + name
#inheritence:5 types
#super()
#private variale and methods in python: __d and __d()


#code1
def st(n,k):
        sr = sys.stdin.readline()
        ow = sys.stdout
        sn = reversed(sr)
        ne = list(sn)
        ow.write(ne[k])
        nk=sys.stdin.readline()
        nks=nk.split()#return the string list
        n=int(nks[0])
        k=int(nks[1])
        st(n,k)
#non locan and the global key word

#a callback function is a function that is passed as an argument to another function or the functions that will be called in the later point of time
# closure to create a function that takes a function as an argument and returns a new function that is the composition of the two functions.
#   clouser which is majorly related to the function similar to the nested function the inner function can be accessed out sed the scope of the enclosing function 
#passing arguments to the inner function in python 
def outer(x,y):
    def inner(z):
        print(x+y+z)
    return inner
#pretty inportant as we use this in decotrators as well 
    # ou =outer(10,11)
    # print(ou(5))

#--n and n-- difference

#fuctions are the first class objects in python 
    # ->Treating function as objects[here it will not call the function rather it uses the object of the function]
    # ->passing function as a argument[the paramenter to the functions will be assigned insde the another function ]
def add(a,b):
    ow=sys.stdout
    c=a+b
    ow.write(str(c))

def tr(fun):
    return fun(10,50)

    # ->returing functiion from anoter function same as clouser example
    # ->You can store them in data structures such as hash tables, lists,

#decorators :here we add functionality to the method were as in method overriding we create a complete new functionality
    #we can assign the function to a vaiable, it becomes a function as well  becaue everything in python is a object
    #this is one shuch concept that can be usedd to justify that python is a funcional language as well
    #  @  annotations aare used to add decorators to the functions
    # we use the inner functions or the closures in decorators because the wrapping function or clousers can remember the staate even after the enclosing function has returned
def deco(func):
    def inner(a,b):
        if a<b:
            a,b=b,a
        return func(a,b)
    return inner

def dct(func):
    def innner():
        c=func()
        return c*2
    return innner
#annotations being used
@dct
def divc():
    return 2

#decorators being assinged to the function which needded to be modified
# div=deco(div)
# div(5,10)

# chaining decorators means decorating a function with multiple decorators.



def prj1():
    low = int(input("enter the lower limit:"))
    upp = int(input("enter the upper limit:"))
    x=random.randint(low,upp)

    li=['dff','rtr','ryr']
    g=random.choice(li)
    print(x,g)
    
if __name__ == '__main__': 
    prj1()