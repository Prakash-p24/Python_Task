# from abc import ABC, abstractmethod 
# class one(ABC):
#     @abstractmethod
#     def add(self):
#         pass
# class two(one):
#     def add(self,a,b):
#         return a + b
# a=two()
   
# #
# import abc

# class AbstractClass(abc.ABC):
#     @abc.abstractmethod
#     def abstract_method(self, param1, param2):
#         pass

# class DerivedClass(AbstractClass):
#     # This will cause an error because it doesn't match the required signature
#     def abstract_method(self):
#         print("This implementation will fail to work properly.")

# # Instantiating the derived class
# # try:
# #     derived_instance = DerivedClass()
# # except TypeError as e:
# #     print(f"Error: {e}")
# a=DerivedClass()
# print(a.abstract_method())

# class one:
#     a="prkash"
    
#     def get(self):
#         return self.a
#     def set(self,value):
#         self.a=value
#         return self.a



# print(set("pandi"))
# print(one.get)
    
# class Cat:

#     # Attributes
#     # name = 'Mittens'
#     # color = 'black'
#     # def __str__(self):
#     #   return f'{self.name}'
#     def __init__(self,name):
#         self.name = name
#     # # Methods
#     # def meow(self):
#     #     print('Meow!')
    
    
#     def n(self):
#        return self.name
        

# obj = Cat("hi")
# # obj2 = Cat()
# # # obj.meow()
# # obj.name = "dog"
# b=n
# print(b)
# obj2.meow()
# obj2.name("dog")
# print(obj.name)

# class test:
#     # def __init__(self, name):
#     #   self.name = name
#     name = "prakash"


    
# a=test()
# print(a.name)

# def decorator_name(func):
    
#         result = func(a,b)
        
#         return result

# @decorator_name
# def add(a, b):
#     return a + b

# print(add(5, 3))

# def hai(func):
#     def wrapper(*args,**kwargs):
#         print('hi')
#         result=func(*args,**kwargs)
#         print(result)
#         print("finished")
#     return wrapper

# @hai
# def add(a,b):
#     return a+b
# add(2,3)

# def hai(cls):
#     def sound(self):
#         print(f"{self.name} is singing")
#     cls.one=sound
#     return cls

# @hai
# class hi:
#     def __init__(self,name):
#         self.name=name

# a=hi("prakash")
# a.one()

# class LoggerDecorator:
#     def __init__(self, func):
#         """The __init__ method is called when the function/class is decorated."""
#         self.func = func
#         # Optional: use functools.wraps to preserve metadata
#         # functools.wraps(func)(self) 

#     def __call__(self, *args, **kwargs):
#         # """The __call__ method is executed when the decorated function is called."""
#         # print(f"Calling {self.func.__name__} with args: {args}, kwargs: {kwargs}")
#         result = self.func(*args, **kwargs)
#         print(f"{self.func.__name__} returned: {result}")
#         return result

# @LoggerDecorator
# def add(a, b):
#     return a + b

# print(add(2, 3))
# Output:
# Calling add with args: (2, 3), kwargs: {}
# add returned: 5
# 5


# def __add__(a,b):
#     print(a+b)
# __add__(2,3)

# def hai(func):
    
#     result=func()
#     print(result)
        
   

# @hai
# def add():
#     print( "hi")
# add()

# def hai():
#     # print ("prakash")
#     return
# print(hai())
# class A:
#     def show(self):
#         print("In Class A")

# class B(A):
#     def show(self):
#         print("In Class B")

# # Class C inherits from A first, then B
# class C(A):
#     pass

# c = C()
# c.show() # Output: In Class A

# # View the MRO
# print(C.mro())
# Output: [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>]
# import random

# answer = random.randint(0, 1)
# n = input("Guess: 0 or 1? ")

# breakpoint() # Program execution pauses here

# if int(n) == answer:
#     print("Correct!")
# else:
#     print(f"Incorrect. The answer was {answer}.")

# class one:
#     def __init__(self,name):
#         self.__name = name
   
#     def display(self):
#         return self.__name

# a=one("prakash")

# print(a.display)

# class one:
#     def __init__(self,name):
#         self.__name = name
   
#     @property
#     def change(self):
#         return self.__name
# a=one("prakash")

# print(a.change())

# class a:
#     name = "prakash"
#     age = ""

#     # def __init__(self,name):
#     #     self.name=name
#     @classmethod
#     def show(cls):
#        cls.dob =2006
    
#     @classmethod
#     def display(cls):
#         return cls.dob
        

# d=a()

# a.name="pandi"

# print(a.show())
# print(a.display())
# print(a.age)
# print(d.display())

# assert 10 <110,"false"
# f = open("C:\\Users\\Mitrahsoft35\\Downloads\\UI_design4.txt")
# print(f.read())
# print("hi")

# d = open("C:\\Users\\Mitrahsoft35\\Downloads\\UI_design4.txt")
# print(d.read())

# d1 = open("C:\\Users\\Mitrahsoft35\\Downloads\\UI_design4.txt")
# print(d1.read())

# d2 = open("C:\\Users\\Mitrahsoft35\\Downloads\\UI_design4.txt")
# print(d1.read())

# def one():
#     print(a)

# a="hi"
# one()
# a={1,2,3,7,8,9}
# a.pop()
# print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)


# f=open("C:\\Users\\Mitrahsoft35\\Downloads\\UI_design4.txt","a+")
# c=f.read()
# print(c)
f=open("prakash.txt","x")
    
