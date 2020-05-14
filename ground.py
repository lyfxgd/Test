# # 斐波那契
# a = 0
# b = 1
# fbLength = 10
# for i in range(fbLength):
#     print(a,end=' ')
#     a, b = b , a + b
# ---------------------------
# # for loop
# aaa = [1,2,3,4,5,6,7,8,9,0]
# for i in range(len(aaa)):
#     print(aaa[i],end=' ')
# print() #换个行
# for i in aaa:
#     print(i,end=' ')
# --------------------------
# # 迭代器
# aaa = [1,2,3,4,5,6]
# aaaIter = iter(aaa)
# print(aaaIter)
# print(next(aaaIter))
# print(aaaIter)
# print(next(aaaIter))
# for i in aaaIter:
#     print(i)
# print(aaaIter)
# print(next(aaaIter)) # StopIteration
# --------------------------
# # 斐波那契by生成器
# # 使用了yield的函数都是生成器，生成器返回一个迭代器。调用生成器函数时，会在yield处停止，保存现有状态，并且输出yield的值，直到再次使用next()调用迭代器
# import sys


# def fib(n: int):
#     a, b, count = 0, 1, 0
#     while count < n:
#         yield a
#         a, b = b, a + b
#         count += 1


# f = fib(10)
# while True:
#     try:
#         print(next(f), end=' ')
#     except StopIteration:
#         sys.exit()
# -----------------------------
# #PEP8
# #           parameter type  return value type
# #                      |        |
# def print_hello(name: str) -> str:
# #        |           |
# #  variable_name   space
#     #inline comment
#     """
#     Greeting Function

#     Parameters:
#         name(str): The name of the person

#     Returns:
#         The cool message
#     """
#     print('hello, ' + name)

# print_hello('SGCC')
# print
# ----------------------------
# #lanmda
# def sorter(item:dict) -> any:
#     return item['name']
# parameters = [
#     {'name': 'Li', 'age': 28},
#     {'name': 'Yifan', 'age': 15},
#     {'name': 'Aba', 'age': 13},
# ]
# parameters.sort(key= lambda item: len(item['name']), reverse=True)
# print('reverse sort by name length:\n', parameters)
# parameters.sort(key= lambda item: len(item['name']))
# print('sort by name length:\n', parameters)
# parameters.sort(key= lambda item: item['age'])
# print('sort by age:\n', parameters)
# parameters.sort(key=sorter)
# print('sort by name:\n ', parameters)
# ----------------------------
# # Class
# #  Pascel Casing(每个单词的首字母都要大写)
# #        |
# class Presenter():
#     def __init__(self, name):
#         # Constructor
#         print('In the Cons')
#         self.name = name
# # 最佳实践：采用设置属性的方式，将字段命名为双下划线，避免对字段直接操作
# #  并且记住，一旦你创建了属性，那就要一直使用它，就算你知道__name对应的是name属性，也不要访问__name字段
# #  @property修饰了name属性，其实质是一个与属性同名的getter方法，但是通过装饰器，可以通过访问字段一样的形式来使用该方法
# #  @name.setter同样修饰了name带value参数的方法，一样可以通过设置字段一样的方式来使用该方法。
#     @property
#     def name(self):
#         print('In the getter')
#         return self.__name

#     @name.setter
#     def name(self, value):
#         print('In the setter')
#         self.__name = value

#     def say_hello(self):
#         # method
#         print('Hello, ' + self.name)

# print('1.')
# presenter = Presenter('Li Yifan')
# print('2.')
# presenter.name = "Li Er fan"
# print('3.')
# presenter.say_hello()

# # Python中一切都是public，不存在私有。通过下划线来建议开发者。
# # _一个下划线表示“你必须确保你知道这是什么，你再使用它”
# # __两个下划线表示“无论如何，千万不要用”
# --------------------------------------
# # 继承
# class Person():
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name

#     @property
#     def name(self):
#         return self.__name

#     @name.setter
#     def name(self, value):
#         self.__name = value

#     def say_hello(self):
#         print('Hello, ', self.name)

# class Student(Person):
#     def __init__(self, name, school):
#         super().__init__(name)
#         self.school = school

#     def __str__(self):
#         return super().__str__()

#     @property
#     def school(self):
#         return self.__school

#     @school.setter
#     def school(self, value):
#         self.__school = value

#     def sing_school_song(self):
#         print('Hi, ', self.school)
    
#     def say_hello(self):
#         super().say_hello()
#         print('I\'m so tired')


# s = Student('Li Yifan', 'XJTU')
# s.say_hello()
# s.sing_school_song()

# print(f'Is this a student? {isinstance(s, Student)}')
# print(f'Is this a Person? {isinstance(s, Person)}')
# print(f'is student a person? {issubclass(Student, Person)}')

# print(s)
#--------------------------------------
#file system
from pathlib import Path

cwd = Path.cwd()
print(cwd)

new_file = Path.joinpath(cwd,'new_file.txt')
print(new_file)

print(f'Is this new file exists? {new_file.exists()}')

parent = cwd.parent

print(f'Is {parent} a dir? {parent.is_dir()}')

print(f'Is {parent} a file? {parent.is_file()}')

for child in parent.iterdir():
    if child.is_dir():
        print(child)

demo_file = cwd.joinpath(cwd, 'ground.py')

print(demo_file.name)

print(demo_file.suffix)

print(demo_file.parent.name)

print(demo_file.stat())