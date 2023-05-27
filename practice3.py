print("\nBasic Math operations")
print(2+3)                                       
print(2-3)                                         
print(2*3)                                       
print(2/3)                                       
print(2//3)                         
print(2%3)                                      
print(2**3)                                      
print(type(2/3))  
print(round(3.7))           
print(abs(-20)) 

print(bin(5)) 
print(int('0b101',2))

normal_variable = 10
print(normal_variable)

a,b,c = 1,2,3
print("\na: ",a, ", b :",b)

_normal_variable = 20
print(_normal_variable)

PI = 3.14
print("\n'__variable is known as a dundar in python")

iq = 200
user_age = iq/5   

some = 5
some +=2
print("\nAugmented operation value :", some)

long_str = '''Im Parth
0 0
 _
'''
print(long_str)

print ('It\'s a beautiful day')
print('\tIts a beautiful day')

name = 'meet'
age = 18
print("Welcome " + name + ". You are "+ str(age) + " years old.")   
print("Welcome ", name , ". You are ", str(age) , " years old.")

print(f"Welcome {name}. You are {age} years old.")                      
print("Welcome {}. You are {} years old.".format(name,age))
print("Welcome {1}. You are {0} years old.".format(name,age))
print("Welcome {_name}. You are {_age} years old.".format(_name="m",_age=18))

strin = '01234567'
print(strin[0])
print(strin[0:])
print(strin[:5])
print(strin[0:4])
print(strin[0:8:1])
print(strin[0:8:2])
print(strin[-1]) 
print(strin[-2])
print(strin[::-1])

strin = '01234567'
strin = strin+ '8'
print(strin)

print(bool(0))
print(bool('True'))        
print(bool(True))

year = input("\nEnter your birth year :")
age = 2023 - int(year) 
print(f"Your current age is {age}")

u_name = input("\nEnter the username :")
password = input("Enter the password :")
print(f"Welcome {u_name}, your password :{len(password)* '*'} is {len(password)} letters long")

print('Working with lists')
li = [1,2,3]
li2 = ['a','b','c']
li3 = [1, 2.5, 'c', True]   
print(li)

li[1] = 2.5
print('\nNew list')
print(li)

cart = ['apple','banana','carrot']
new_cart = cart
new_cart[0] = 'orange'
print(cart)
cart = ['apple','banana','carrot']
new_cart2 = cart[:]
new_cart2[0] = 'orange'
print(cart)

eg = [1,2,3,4,5]
eg2 = eg.append(100)
print(eg)
print("eg2 : ",eg2)

eg = [1,2,3,4,5]
eg.append(100)          
eg2 = eg[:]
print("eg2", eg2)
eg.append([100,200])  
print(eg)

eg.extend([200,201]) 
print("eg", eg)

eg.pop()
print("eg :", eg)
eg.pop(0)
print("eg :", eg)
p = eg.pop(2) 
print("eg :", eg , ", Pop value :", p)
eg.remove(5) 
print("eg :", eg)
eg.clear() 
print(eg)
eg = ['a','b','c','d','e','d']
print("index of 'd' is :",str(eg.index('d')))
print("count of 'd' is :", str(eg.count('d')))
print("Is 'd' present in the list 'eg' : ", 'd' in eg)
print("Is 'a' present in 'hello world' ", 'a' in 'hello world')


eg = ['z', 'a', 'v', 's', 'p']
print("'sort' is inPlace :", eg.sort())   
print(eg)
eg2 = ['z', 'a', 'v', 's', 'p']
print("'sorted' is not inPlace :",sorted(eg2))
print("Original :", eg2)
print(eg2.reverse())  
print("REversed :",eg2) 
sorted([5,2,1])
sorted([7,4,9] + [12,7,32])
sorted([1,4,7] + [4,9,12] + [33,76,99])
print(sorted)

from heapq import merge
a = [1, 4, 7]
b = [4, 9, 12]
c = [33, 76, 99]
it = merge(a, b, c)  
result = list(it)  
print(result)  

from heapq import merge
from itertools import islice
a = [1, 4, 7]
b = [4, 9, 12]
c = [33, 76, 99]
it = merge(a, b, c)  
result1 = list(islice(it, 3))  
sult2 = list(islice(it, None))  
print(result1)  
print(sult2)

s = 'he'
t = 'llo'
u = s + t
w = 'hello'
print(u, w)
print(u == w)
print(id(u), id(w))
print(u is w)
import sys
u = sys.intern('hello')
v = sys.intern(s + t)
print(u is v)
print(id(u), id(v))

basket = ['a','x','b','c','d','e','d']
basket.sort()
basket.reverse()
print("Reversing again :", basket[::-1]) 
print("Recersed list   :", basket)

print("\nRange")
print(range(1,100))
print("\n", list(range(100)))
print("\n", list(range(5,100)))

print("\nRange functionality")
for number in range(5,8):
  print(number)
print("Range with stepovers")
for number in range(1,10,3):
  print(number)
print("If we don't really need variable")
for _ in range(5,8):
  print(_)
print("Creating lists using range")
for _ in range(0,2):
  print(list(range(10)))

sentence = '-'
print(sentence.join(['hi','my','name','is','meet']))  
print(' '.join(['hi','my','name','is','meet']))

a,b,c,d,*other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)
print(other)
print(d)

import bisect
cuts = [20, 40, 60, 80]
grades = 'EDCBA'
print(grades[bisect.bisect(cuts, 50)])
result = [grades[bisect.bisect(cuts, x)] for x in [10, 30, 50, 80, 100]]
print(result)


dictionary = {
  'a': [1,2,3],
  123: 'hello integer',          
  123.0:'hello float',  
  123.12:'hello double',
  False: True
}
print(dictionary)
print(dictionary['a'])
print(dictionary.get('a',"default_value"))
print(dictionary[123])        
print(dictionary[123.0]) 

dictionary2 = dict(a=[1,2,3], b="asd")   
print(dictionary2)
print(dictionary2['b'])

print("\nList with dictionary")
my_list = [
  {
  'a': [1,2,3],
  'b': 'hello',
  'c': True
  },
  {
  'a': [4,5,6],
  'b': 'world',
  'c': False
  }
]
print(my_list[1]['a'])

print(dictionary.setdefault("b","b set from default"))
print(dictionary)

dictionary = {
  'a': [1,2,3],
  123: 'hello',
  False: True
}
print("\nIterating the dictionary simply")
for item in dictionary:        
  print(item) 
print("\nIterating the dictionary by keys")
for item in dictionary.keys():
  print(item)    
print("\nIterating the dictionary by items")
for item in dictionary.items():
  print(item)   
  key,value = item 
  print(key, " : ", value)
print("\nIterating the dictionary by items")
for key,value in dictionary.items(): 
  print(key, " : ", value)  
print("\nIterating the dictionary by values")
for item in dictionary.values():
  print(item) 

my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for item in my_list:
  sum+=item
print("Total sum of all items = ",str(sum))
print("\nEnumerate example")
for item in enumerate("Hellooo"):
  print(item)                   
print("Main purpose -> to get the index from 0")
for index, item in enumerate("Hellooo"):
  print(f'{index} -> {item}')            
print("Main purpose -> to get the index from custom index")
for index, item in enumerate("Hellooo", start=1):
  print(f'{index} -> {item}')    

i=0
while i<2:
  print("i : ", str(i))
  i+=1
else:
  print("done with all the work")  
i=0
while i<50:
  print("\ni : ", str(i))
  break     
else:
  print("done with all the work") 

my_set = {1,2,3,4,5}
print("my_set : ", my_set) 
my_set = {1,5,3,4,5,5,2,5,5,5}
print("my_set : ", my_set)

my_list = [9,4,5,4,4,3,2,2,1]
my_list_set = set(my_list)
my_list_back = list(my_list_set)
print("\nList converted to set :", my_list_set)
print("\nlist converted to set :",my_list_back)

exe_list = [1,5,3,1,6,9,6,4,6,2,5,8,4,2,4,7,8,9,4,2,1,6]
for item in exe_list:
      print(f'element: {item} : count: {exe_list.count(item)}')
exe_list = [1,5,3,1,6,9,6,4,6,2,5,8,4,2,4,7,8,9,4,2,1,6]
exe_set_list = list(set(exe_list))
for item in exe_set_list:
      print(f'element: {item} : count: {exe_list.count(item)}')
print("\nLength of my_list(set) :", len(my_list_set))
print("Check an item '4' in my_list_set:",4 in my_list_set)
my_set = {9,4,5,4,4,2,2,1}
new_set = my_set.copy()
my_set.clear()
print("\nOriginal(my_set) after clearing : ", my_set)
print("new(new_set) after clearing : ", new_set)


my_set = {1,2,3}
your_set = {4,5,6,7,8,9,10}
print("Disjoint(is there anything common. are they not overlapped?) : ", my_set.isdisjoint(your_set))
print("True: They are not overlapped(they are dis-joint)")
print("\nUnion : ", my_set.union(your_set))
print("Union(another method) : ", my_set|your_set)
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
print("\nis x subset of y? :", my_set.issubset(your_set))
print("is x superset of y? :", my_set.issuperset(your_set))
print("is y superset of x? :", your_set.issuperset(my_set))
basket = ['a','x','b','c','d','e','d']
basket.sort()
basket.reverse()
print("Reversing again :", basket[::-1]) 
print("Original list   :", basket)

print("\nRange")
print(range(1,100))
print("\n", list(range(100)))
print("\n", list(range(5,100)))

sentence = '!'
print(sentence.join(['hi','my','name','is','meet']))
print(' '.join(['hi','my','name','is','meet']))

a,b,c,d,*other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)
print(other)
print(d)

basket = ["Banana", "Apples", "Oranges", "Blueberries"];
print(basket.remove('Banana'))
print(basket)
print(basket.pop())
print(basket)
print(basket.append("Kiwi"))
print(basket)
print(basket.insert(0,"Apples"))
print(basket)
print(basket.count("Apples"))
print(basket.clear())
print(basket)

print((5 + 4) * 10 / 2)
print(((5 + 4) * 10) / 2)
print((5 + 4) * (10 / 2))
print(5 + (4 * 10) / 2)
print(5 + 4 * 10 // 2)

print("Hello {}, your balance is {}.".format("meet", 50))
print("Hello {0}, your balance is {1}.".format("meet", 50))
print("Hello {name}, your balance is {amount}.".format(name="meet", amount=50))
print("Hello {0}, your balance is {amount}.".format("meet", amount=50))

name='meet'
amount=500
print(f"hello {name}, your balance is {amount}")
name = 'meet'
amount = 500
print(f"Hello {name}, your balance is {amount}.")

x,xx = "Hello",""
y,yy = 20,0
print(f"x:{bool(x)}, xx:{bool(xx)},\ny:{bool(y)}, yy:{bool(yy)}")

username = "meet"
password = '123'

if username and password:
  print("\nusername,password do exists")
else:
  print("\nusername,password don't exists")
username = "meet"
password = '111'
print("Current password :", bool(password))
if username and password:
  print("\nusername,password do exists")
else:
  print("\nusername,password don't exists")

print(True is True)
print('1' is '1')
print([] is []) 
print(10 is 10)
print([1,2,3] is [1,2,3])

a = [1,2]
b = [1,2]
memory = "Same memory" if a is b else "Different memory"
print("\nMemory location : ", memory)
print("\n'=='-> compares content")
print(True == True)
print('1' == '1')
print([] == []) 
print(10 == 10.0)
print([1,2,3] == [1,2,3])

print("\nFor loop")
for item in "Hi Duh!":    
  print(item)
for item in reversed("Hi Duh!"):
      print(item)
for item in [1,2,3]:    
  print(item)
for item in {1,2,3}:    
  print(item)   
for item in (1,2,3):    
  print(item)

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
for row in picture: 
  for pixel in row:
    if not pixel: 
      print(" ",end='')
    else:
      print("*",end='')
  print("\n")    

some_list = ['a','b','c','b','d','m','n','n']
duplicates = []
for item in some_list:
  if some_list.count(item) > 1:
    if item not in duplicates:
      duplicates.append(item)
print(duplicates)


def highest_even(li):
    highest = 0
    for item in li:
        if item % 2 == 0 and item > highest:
            highest = item
    print("\nHighest Even:", highest)

highest_even([10, 2, 5, 3, 79, 4, 80])


class PlayerCharacter:
    membership = True
    def __init__(self, name):  
        self.name = name
        print("\nMembership :", self.membership)
        print("Membership :", PlayerCharacter.membership)
    @classmethod
    def classMethod(cls, num1, num2):  
        return cls("Uttam")
    @staticmethod
    def staticMethod(num1, num2):
        return num1 + num2
    def run(self):  
        print(f"\n{self.name} is Running")  
player1 = PlayerCharacter("Parth")
player2 = PlayerCharacter("Zeal")
print("Player 1 :", player1.name)
print("Player 2 Membership:", player2.membership)
print("Player Membership :", PlayerCharacter.membership)
player2.run()
print("\n", player2.run()) 
player3 = PlayerCharacter.classMethod(2, 3)
print(
    "\nCalling class method and getting new player object with 'cls' method and getting name :",
    player3.name)
print("\nCalling static method :", PlayerCharacter.staticMethod(2, 3))


class Dog():
    _animal_type = 'Dog'
    def __init__(self, breed, speed):
        self._breed = breed
        self._speed = speed
    def run(self):
        print(f"\n'{self._breed}' dog is running at {self._speed} km/hr")
dog1 = Dog("joshua", 12)    
print("Dog1 animal type : ", dog1._animal_type)
dog1.run()

print("\nCreating our own decorators")
def my_decorator(func):          
  def wrap_func():
    print("***************")
    func()
    print("***************")  
    return wrap_func                   
@my_decorator
def callll():
  print("MEET RADADIYA") 


print("\nCreating our own decorators with arguments")
def my_decorator(func):
  def wrap_func(greeting,emoji):
    print("***************")
    func(greeting,emoji)
    print("***************")
  return wrap_func
@my_decorator
def call_me(greeting, emoji):
  print(greeting,emoji)
call_me('Hello ', ':)')

print("\nCreating our own decorators with multiple arguments/types")
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("***************")
        print(args, "\n", kwargs)
        func(*args, **kwargs)
        print("***************")
    return wrap_func
@my_decorator
def call_me(greeting, emoji=':)'):
    print(greeting, emoji)


user1 = {
    'name': 'Sorna',
    'valid': True 
}
user2 = {
    'name': 'Sorna',
    'valid': False  
}
def authenticated(fn):
    def wrapper(*args, **kwargs):
        print(args[0]) 
        if args[0]['valid']:
            fn(*args, **kwargs)
        else:
            print("The user is not valid")
    return wrapper
@authenticated
def message_friends(user):
    print('message has been sent')
message_friends(user1)
message_friends(user2)

import time
time.sleep(5)
print("Printing after 5 seconds, counting 1 Mississippi, 2 Mississippi, ... 5 Mississippi")
for i in range(1, 6):
    print(f"{i} Mississippi")
    time.sleep(1)
current_time = time.time()
print("Current time in seconds since the epoch:", current_time)
formatted_time = time.ctime()
print("Current time in a formatted string:", formatted_time)

from time import time
def performance(fn):
  def wrapper(*args, **kwargs):
    t1 = time()
    result = fn(*args,**kwargs)
    t2 = time()
    print(f'Took {(t2-t1)*1000} seconds to complete')
    return result
  return wrapper
@performance
def my_function():
  for i in range(1000):
    i*2
my_function()
@performance
def my_function():
  for i in range(100000):
    i*2
my_function()   

print("\nHow 'range' works")
class MyRangeGen():
    current = 0
    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __iter__(self):
        return self
    def __next__(self):
        if MyRangeGen.current < self.last:
            num = MyRangeGen.current
            MyRangeGen.current += 1
            return num
        raise StopIteration
gen = MyRangeGen(0, 10)
for i in gen:
    print(i)

print("\nHow 'for' works")
def special_iter(iterable):
  iterator = iter(iterable)             
  while True:
    try:
      print(next(iterator))
    except StopIteration:
      break  
special_iter([1,2,3])  

def fib(number):
  a=0
  b=1
  for i in range(number):
    yield a        
    temp=a
    a=b
    b=temp+b
for x in fib(5):
  print(x) 


print("Range : ",range(110))
print("\nLisdt : \n",list(range(100)))
def create_list(num):
  generated_list = []
  for i in range(num):
    generated_list.append(i)
  return generated_list
print("\nGenerated list this way : \n",create_list(100))

print("\nOwn generator (and 'yield' functionality): ")
def generator_function(num):
  for i in range(num):
    yield i
g = generator_function(100)
print (f'G(once) : {g}')
print(f'G(next time) : {next(g)}')
print(f'G(next time) : {next(g)}')

my_list = [1,2,3]
def multiply_by2(listt):
  new_list = []
  for item in listt:
    new_list.append(item*2)
  return new_list
print(f"Multiply by 2 list : {multiply_by2(my_list)}")
print(f"my_list : {my_list}")

my_list = [1,2,3]
def multiply_by2(x):
  return x*2   
print("\nThrough mapping :",list(map(multiply_by2, my_list)))
print("\nThrough mapping :",list(map(lambda x: x*2, my_list)))

my_list = ['surat', 'vadodara', 'ahmedabad']
print(list(map(str.upper, my_list)))

my_list = [1,2,3]
def only_odd(x):
  return x%2!=0      
print("\nThrough filtering :",list(filter(only_odd, my_list))) 

my_list = [1,2,3]
your_list = [10,20,30]
print("\nThrough zipping :",list(zip(my_list,your_list)))

print("\nThrough reduce :")
from functools import reduce
my_list = [1,2,3]
def accumulator(acc,item):
  print(acc, item)
  return acc+item
print(reduce(accumulator, my_list, 0))

from functools import reduce
print("\nUsing lambda function")
my_list = [1, 2, 3]
print(list(map(lambda my_list_item: my_list_item * 2, my_list)))
print(list(filter(lambda my_list_item: my_list_item % 2 == 0, my_list)))
print(reduce(lambda acc, my_list_item: acc + my_list_item, my_list, 0))

print("\nSquare list using labda function")
my_list = [1,2,3]
print(list(map(lambda my_list_item:my_list_item **2, my_list)))

print("\nSorting using 2nd item in tuple in list using lambda function")
a = [(0, 2), (4, 3), (10, -1), (9, 9)]
a.sort(key=lambda item_a: item_a[1])
print(a)
def multiplexers():
    return [lambda n, index=index: index * n for index in range(4)]
print([m(2) for m in multiplexers()])

my_set1 = [char for char in 'Hello']
print(my_set1)
my_set2 = {value for value in range(1,10)}
print(my_set2)
my_set3 = {value*2 for value in range(1,10)}
print(my_set3)
my_set4 = {value**2 for value in range(1,10)}
print(my_set4)
print("\nList and set comprehension")
print(f'{my_set1}\n{my_set2}\n{my_set3}\n{my_set4}')
print("\nDictionary comprehension")
simple_dictionary = {
  'a':2,
  'b':5
}
new_dictionary = { key:value for key,value in simple_dictionary.items() if value%2==0}
print(new_dictionary)

print("\nExample dictionary from list")
my_list = [1,2,3]
new_dictionary = {k:k*2 for k in my_list}
print(new_dictionary)

print("Displaying items that are multiple from a list")
my_list = ['a','b','c','b','d','m','n','n']
duplicates=[]
new_list = set([item for item in my_list if my_list.count(item)>1])
print(new_list)


from itertools import *   
for t in product('ABC', 'DE', 'xyz'):
      print(t)   
for t in permutations('Love'):
      print(t)  
for t in permutations('Love',2): 
      print(t)
for t in combinations('Love',2): 
      print(t)

rows = ['data1', 'data2', 'data3']
row = rows[0]
print("Row:", row)
print("\nCreating our own decorators")
def my_decorator(func):
    def wrap_func():
        print("***************")
        func()
        print("***************")
    return wrap_func
@my_decorator
def callll():
    print("MEET RADADIYA")
callll() 

while True:
  try:
    age = input("\nEnter your age : ")
    print(int(age))
  except ValueError :
    print("Please enter a number!")
    continue
  except TypeError :
    print("Please enter a correct type!")  
    continue
  else:
    print("Thank you !")
    break    
  finally:
    print("Ok, i'm done here")
def sum(num1, num2):
  try:
    return num1+num2
  except (TypeError,ZeroDivisionError) as err:
    print("\nProgram error : ",err)
print(sum(1,'2')) 

import re
string = "this search inside of this text please!"
print(f"Search present : {'search' in string}")
print("\nSearch using pattern")
pattern = re.compile("this")
a = pattern.search(string) 
print("a : ",a)
print("a start index : ", a.start())
print("a end index : ", a.end())
print("\nFind all instances :", pattern.findall(string))
print("\n Simple match : ",pattern.match(string))
print("\n Full match : ",pattern.fullmatch(string))

import re
print("\nEmail validation using patterns")
email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
email = "plathiya2611@gmail.com"
a = email_pattern.search(email)
if a:
    print("Valid email")
else:
    print("Invalid email")

import re
print("\nPassword validation (at least 8 chars, any letters, numbers, $%#@)")
password_pattern = re.compile(r"^(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[$%#@]).{8,}$")
password = "meet123@"
b = password_pattern.search(password)
if b:
    print("Valid password")
else:
    print("Invalid password")


import hashlib
md5_hash = hashlib.md5('The tale of two cities'.encode('utf-8'))
md5_digest = md5_hash.digest()
md5_hexdigest = md5_hash.hexdigest()
print("MD5:")
print("Digest:", md5_digest)
print("Hex Digest:", md5_hexdigest)
sha1_hash = hashlib.sha1('The tale of two cities'.encode('utf-8'))
sha1_digest = sha1_hash.digest()
sha1_hexdigest = sha1_hash.hexdigest()
print("\nSHA1:")
print("Digest:", sha1_digest)
print("Hex Digest:", sha1_hexdigest)
sha256_hash = hashlib.sha256('The tale of two cities'.encode('utf-8'))
sha256_digest = sha256_hash.digest()
sha256_hexdigest = sha256_hash.hexdigest()
print("\nSHA256:")
print("Digest:", sha256_digest)
print("Hex Digest:", sha256_hexdigest)
sha512_hash = hashlib.sha512('The tale of two cities'.encode('utf-8'))
sha512_digest = sha512_hash.digest()
print("\nSHA512:")
print("Digest:", sha512_digest)

import hashlib
b = 'The tale of two cities'.encode('utf-8')
b = hashlib.sha512(b).digest()
b = hashlib.sha512(b).digest()
b = hashlib.sha512(b).digest()
b = hashlib.sha512(b).digest()
print("Final SHA512 Digest:", b)

import hashlib
p = 'The tale of two cities'.encode('utf-8')
hashed_phrase1 = hashlib.pbkdf2_hmac('sha256', p, b'some company phrase', 10000)
hashed_phrase2 = hashlib.pbkdf2_hmac('sha256', p, b'some other phrase', 10000)
print("Hashed Phrase 1:", hashed_phrase1)
print("Hashed Phrase 2:", hashed_phrase2)

s = 'the quick'
t = 'brown fox'
result = repr((s, t))
print(result)

s = 'the '
t = 'quick brown fox'
rr=repr((s,t))
print(rr)

#
x=10
print(f'Convert \'x\' to 8 digits number: {x:08d}')

from collections import Counter
d = {}
d['dragons'] = 0
d = Counter(d)
d['dragons'] += 1
d['dragons'] += 1
print(d)
elements = list(d.elements())
print(elements)

from collections import Counter
c = Counter('red green blue green blue blue'.split())
print(c)
most_common_1 = c.most_common(1)
most_common_2 = c.most_common(2)
elements = list(c.elements())
print(most_common_1)
print(most_common_2)
print(elements)

from statistics import mean, median, mode, stdev, pstdev
data = [50, 52, 53]
mean_value = mean(data)
median_value = median(data)
mode_value = mode(data)
stdev_value = stdev(data)
pstdev_value = pstdev(data)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_value)
print("Standard Deviation:", stdev_value)
print("Population Standard Deviation:", pstdev_value)

s = [10, 20, 30, 40]
t = [50, 60, 70, 80]
u = s + t
print(u)
concatenated_slice = u[:2] + u[-2:]
print(concatenated_slice)
dir_list = dir(list)
print(dir_list)
s = 'abrakadabra'
index_k = s.index('k')
count_b = s.count('b')
print(index_k)
print(count_b)
s = [10, 5, 29, 4]
s.sort()
print(s)
s = [10, 5, 29, 4]
sorted_s = sorted(s)
print(sorted_s)
print(s)
sorted_cat = sorted('cat')
print(sorted_cat)

square_func = lambda x: x ** 2
result1 = square_func(5)
result2 = 2 + square_func(3) + 5
f = lambda x, y: x ** 2 + y
result3 = f(2, 3)
print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)

x, y = 2, 3
f = lambda: x ** y
result = f()
print("Result:", result)

from functools import partial
def sum(x, y):
    print(x + y)
x = 2
sum_partial = partial(sum, x)
y = 3
sum_partial(y)

x = 15
result = 6 < x < 20
print(result)

from random import *
seed(8473940)
result1 = random()
result2 = random()
result3 = random()
seed(8473940)
result4 = random()
result5 = random()
result6 = random()
uniform_result = uniform(1000, 1100)
triangular_result1 = triangular(1000, 1100)
triangular_result2 = triangular(1000, 1100)
triangular_result3 = triangular(1000, 1100)
gauss_result = gauss(100, 15)
expovariate_result = expovariate(1/5)
print("Random 1:", result1)
print("Random 2:", result2)
print("Random 3:", result3)
print("Random 4:", result4)
print("Random 5:", result5)
print("Random 6:", result6)
print("Uniform:", uniform_result)
print("Triangular 1:", triangular_result1)
print("Triangular 2:", triangular_result2)
print("Triangular 3:", triangular_result3)
print("Gaussian:", gauss_result)
print("Exponential:", expovariate_result)

import random
outcomes = [...]  
random.shuffle(outcomes)
print(outcomes)

from random import sample
your_ticket_no = 25
lower_limit = 1
upper_limit = 100
declared_list = sorted(sample(range(lower_limit, upper_limit + 1), k=5))
if your_ticket_no in declared_list:
    print('Congratulations! You won!')
else:
    print('Better luck next time!')


from collections import Counter
from random import choice
population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
print(Counter(population))
random_choices = [choice(population) for x in range(6)]
print(Counter(random_choices))

from random import choices
from collections import Counter
population = ['red'] * 18 + ['black'] * 18 + ['green'] * 2
random_choices = choices(population, k=6)
print(Counter(random_choices))

from random import choices, sample
from collections import Counter
population = ['red', 'black', 'green']
weights = [18, 18, 2]
random_choices = choices(population, weights, k=6)
print(Counter(random_choices))
deck = Counter(tens=16, low=36)
print(deck)
deck = list(deck.elements())
deal = sample(deck, 20)
print(deal)
print(Counter(deal))


from random import sample
from collections import Counter
deck = Counter(tens=16, low=36)
deck = list(deck.elements())
deal = sample(deck, k=52)
remaining_cards = deal[20:]
print(Counter(remaining_cards))

#from random import choices
#trial = lambda: choices(['heads', 'tails'], cum_weights=[0.60, 1.00], k=7).count('heads') >= 5
#result = trial()
#print(result)
#count_true = sum([True] * 2)
#print(count_true)
#total_trials = 1000
#success_count = sum(trial() for x in range(total_trials))
#success_ratio = success_count / total_trials
#print(success_ratio)

from random import sample
from statistics import median
total_numbers = 10000
result1 = total_numbers // 4
result2 = total_numbers * 3 // 4
result3 = sample(range(total_numbers), k=5)
result4 = median(sample(range(total_numbers), k=5))
print(result1)
print(result2)
print(result3)
print(result4)

from random import sample
total_numbers = 10000
result = sample(range(total_numbers), k=5)[2]
print(result)


import random
total_numbers = 10  
random_sample = random.sample(range(total_numbers), k=5)
third_element = random_sample[2]
print(third_element)

from statistics import mean, stdev
from random import choices
timings = [7.18, 8.59, 12.24, 7.39, 8.19, 8.69, 6.98, 8.31, 9.06, 7.06, 7.67, 10.02, 6.68, 9.07]
mean_timings = mean(timings)
stdev_timings = stdev(timings)
def bootstrap(data):
    return choices(data, k=len(data))
bootstrapped_timings = bootstrap(timings)
mean_bootstrapped = mean(bootstrapped_timings)
trial = lambda: mean(bootstrap(timings))
total_numbers = 10000
means = sorted(trial() for _ in range(total_numbers))
num_means = len(means)
first_20_means = means[:20]
last_20_means = means[-20:]
mean_500 = means[500]
mean_last_500 = means[-500]
print("Mean of timings:", mean_timings)
print("Standard deviation of timings:", stdev_timings)
print("Mean of bootstrapped timings:", mean_bootstrapped)
print("Number of means:", num_means)
print("First 20 means:", first_20_means)
print("Last 20 means:", last_20_means)
print("Mean at index 500:", mean_500)
print("Mean at index -500:", mean_last_500)

from statistics import mean
from random import shuffle
drug_results = [7.1, 8.5, 6.4, 7.7, 8.2, 7.6, 8.4, 5.1, 8.1, 7.4, 6.9, 8.4]
placebo_results = [8.2, 6.1, 7.1, 7.1, 4.9, 7.4, 8.1, 7.1, 6.2, 7.0, 6.6, 6.3]
len_drug_results = len(drug_results)
len_placebo_results = len(placebo_results)
mean_drug = mean(drug_results)
mean_placebo = mean(placebo_results)
obs_diff = mean_drug - mean_placebo
combination = drug_results + placebo_results
nd = len_drug_results
shuffle(combination)
shuffled_drug_results = combination[:nd]
shuffled_placebo_results = combination[nd:]
print("Number of drug results:", len_drug_results)
print("Number of placebo results:", len_placebo_results)
print("Mean of drug results:", mean_drug)
print("Mean of placebo results:", mean_placebo)
print("Observed difference:", obs_diff)
print("Shuffled drug results:", shuffled_drug_results)
print("Shuffled placebo results:", shuffled_placebo_results)

from collections import defaultdict
from pprint import pprint
names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank']
d = defaultdict(list)
for name in names:
    feature = name[0]
    d[feature].append(name)
pprint(dict(d))
d = defaultdict(list)
for name in names:
    feature = len(name)
    d[feature].append(name)
pprint(dict(d))

from pprint import pprint
names = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve', 'Frank']
sorted_names = sorted(names, key=len)
pprint(sorted_names)

result1 = list(zip('abcde', 'fghijk'))
print(result1)
from itertools import zip_longest
result2 = list(zip_longest('abcde', 'fghijk'))
print(result2)
result3 = list(zip_longest('abcde', 'fghijk', fillvalue='x'))
print(result3)
m = [[10, 20],
     [30, 40],
     [50, 60]]
print(m)

from pprint import pprint
result = list(zip([10, 20], [30, 40], [50, 60]))
pprint(result, width=20)

from pprint import pprint
m = [[10, 20],
     [30, 40],
     [50, 60]]
result = list(zip(*m))
pprint(result, width=20)

it = iter('abcde')
print(it)
result = list(it)
print(result)

import glob
files = glob.glob('*.txt')
print(files)

print("TheRaymondWay\N{trade mark sign}")

s = 'L' + chr(246) + 'wis'
t = 'L' + chr(111) + chr(776) + 'wis'
print(s, t)
print(s == t)

s = 'L' + chr(246) + 'wis'
t = 'L' + chr(111) + chr(776) + 'wis'
result_s = [ord(s) for s in s]
result_t = [ord(t) for t in t]
print(result_s)
print(result_t)

a = 5
b = 5
print('same') if a == 5 and b == 5 else print('different')

a = 5
b = 5
print('same') if a == b == 5 else print('different')

fruits = ['apples', 'bananas', 'grapes', 'tomatos']
for index in range(len(fruits)):
    print (fruits[index])

for fruit in fruits:
    print(fruit)

fruits = ['apples', 'bananas', 'grapes', 'tomatos']
for index in range(len(fruits)-1,-1,-1):
    print (fruits[index])
    
for fruit in reversed(fruits):
    print(fruit)

fruits = ['apples', 'bananas', 'grapes', 'tomatos']
for index in range(len(fruits)):
    print (f'{index} -> {fruits[index]}')
    
for index,fruit in enumerate(fruits):
    print (f'{index} -> {fruit}')


fruits = ['apples', 'bananas', 'grapes', 'tomatos']
vegetables = ['carrot', 'spinach', 'cucumber']
smaller_size = min(len(fruits), len(vegetables))
for index in range(smaller_size):
    print (f'{fruits[index]} -> {vegetables[index]}') 
    
for fruit,vegetable in zip(fruits,vegetables):      
    print (f'{fruit} -> {vegetable}')

vegetables =['Potato','Capsicum','Brinjal','Tomato','Green peas']
fruits = ['apples','ginger' ,'bananas', 'grapes', 'tomatos']
from itertools import zip_longest
for fruit,vegetable in zip_longest(fruits,vegetables, fillvalue='None'):
    print(f'{fruit} -> {vegetable}')

_fruits = ['apples','ginger' ,'bananas', 'grapes', 'tomatos']
for fruit in sorted(_fruits, reverse=True):
    print(_fruits)

lengths = ['asd', 'dsgerg', 'rgsdgsdrwd', 'e', 'fw', 'reg', 'z']
print(sorted(lengths, key=len))

users = ['parth', 'helly', 'nidhi', 'bhoomit']
found = False;
find_name = 'nidhi'
for user in users:
    if user == find_name:
        found = True
        print("Found!")
        break
if not found:
    print("Not found!")

users = ['parth', 'helly', 'nidhi', 'bhoomit']
find_name = 'nidhi'
for user in users:
    if user == find_name:
        print("Found!")
        break
else:
    print("Not Found!")

users = ['parth', 'helly', 'nidhi', 'bhoomit']
find_name = 'nidhi'
print(f'User Found! at index: {users.index(find_name)}') if find_name in users else print("Not Found!")

my_dict = {'cat': 'milk', 'bee': 'honey', 'dog': 'bone'}
keys_to_delete = []
for key in my_dict:
    if key.startswith('b'):
        keys_to_delete.append(key)
for key in keys_to_delete:
    del my_dict[key]
print(my_dict)

my_dict = {'cat':'milk', 'bee':'honey', 'dog':'bone'}
for key in list(my_dict):                             
    if key.startswith('b'):
        del my_dict[key]
print(my_dict)

my_dict = {'cat':'milk', 'bee':'honey', 'dog':'bone'}
for key in my_dict: 
    print(f'{key} -> {my_dict[key]}')                      

my_dict = {'cat':'milk', 'bee':'honey', 'dog':'bone'}
for key, value in my_dict.items():                   
    print(f'{key} --> {value}')

users = ['parth', 'helly', 'nidhi', 'bhoomit']
fruits = ['apples','ginger' ,'bananas']               
my_dict = dict(zip(users,fruits))                      
print(my_dict)

x = {'a':1, 'b':2}
y = {'b':3, 'c':4}
z={**x, **y}
z      
print(z)

users = ['parth', 'helly', 'nidhi', 'bhoomit']
d = {}
for user in users:
    key = len(user)
    if key not in d:
        d[key] = []
    d[key].append(user)
print(d)

users = ['parth', 'helly', 'nidhi', 'bhoomit', 'zeal', 'zeel', 'uttam', 'vaikunth', 'shlok']
d = {}
for user in users:
    key = len(user)
    d.setdefault(key,[]).append(user)       
print(d)

users = ['bhoomit', 'parth', 'helly', 'nidhi', 'zeal', 'uttam', 'vaikunth', 'shlok']
from collections import defaultdict
d = defaultdict(list)
for user in users:
    key = len(user)
    d[key].append(user)
print(d)

eng_to_span = dict(one='uno', two='dos', three='tres')
span_to_eng = dict()
for x, y in eng_to_span.items():
    span_to_eng[y] = x
print(span_to_eng)

eng_to_span = dict(one='uno', two='dos', three='tres')
span_to_eng = {v: k for k, v in eng_to_span.items()}
print(span_to_eng)

e2s = {                         
    'one':['uno'],
    'free':['libre','gratis']
}
print(e2s)

from collections import defaultdict
from pprint import pprint
e2s = {
    'one': ['uno'],
    'two': ['dos'],
    'three': ['tres']
}
s2e = defaultdict(list)
for k, listt in e2s.items():
    for v in listt:
        s2e[v].append(k)
pprint(s2e, width=40)

def fun(username, password, is_premium_user):
    pass
show = fun('Parth', "2sf6h", True)
print(show)
show1 = fun(username="Parth", password="2sf6h", is_premium_user=True)
print(show1)

my_tuple = 'hi','how','are','you'   
print(my_tuple)
p = my_tuple[0]
q = my_tuple[1]
r = my_tuple[2]
s = my_tuple[3]

p,q,r,s = my_tuple

my_list = ['hi','how','are','you']
s = my_list[0]
for item in my_list[1:]:
    s += ", " + item
print(s)

s = ', '.join(my_list)
print(s)

my_list = ['hi','how','are','you']
del[my_list[0]]
my_list.pop()
my_list.insert(0,"yo!")
print(my_list)

from collections import deque
my_new_list = deque(['hi','how','are','you'])      
del[my_new_list[0]]
my_new_list.pop()
my_new_list.insert(0,"yo!")
print(my_new_list)
my_new_list[0]
[*my_new_list]         

import threading
lock = threading.Lock()
lock.acquire()
try:
    print('Critical Section 1')
    print('Critical Section 2')
finally:  
    lock.release()


with lock:                                         
    print('Critical Section 1')
    print('Critical Section 2')

from collections import Counter
my_list = ["list_item" for x in range(10)]
print(my_list)
print(Counter(my_list))

my_list = ["list_item"] * 10
print(my_list)
print(Counter(my_list))

sum([0.1]*10)
print(sum([0.1]*10) == 1)

from math import fsum
fsum([0.1]*10)
print(fsum([0.1]*10) == 1)

from collections import defaultdict
d = defaultdict(list)
d['p'].append('parthiv')
d['z'].append('zeal')
d['p'].append('parth')

print(d)

from pprint import pprint
pprint(d, width=40)

m=[
    [10,20],
    [30,40],
    [50,60]
]

for row in m:
    for column in row:
        print(f'{column}', end=", ")

print([x for row in m for x in row])


s = 'abadffghi'
result1 = list(zip(s, s, s))
print(result1)
s = 'abadffghi'
it = iter(s)
result2 = list(zip(it, it, it))
print(result2)
for part in zip([iter('abadffghi')] * 3):
    print(part)
di = dict({'a': 1, 'b': 2})
di.setdefault('c', 3)
result3 = list(zip(['abc', 'def', 'ghi']))
print(result3)
result4 = list(zip(*['abc', 'def', 'ghi']))
print(result4)
for part in zip(*[iter('abadffghi')] * 3):
    di = dict()
    result5 = "".join([di.setdefault(char, char) for char in part if char not in di])
    print(result5)

set={7,3,4,5}