print("\nBasic Math operations")
print(2+3)                                       # 5
print(2-3)                                       # -1  
print(2*3)                                       # 6
print(2/3)                                       # 0.66
print(2//3)                         #0
print(2%3)                                       # 2
print(2**3)                                      # 8 

print("\nChecking the data type")
print(type(2/3))


# $Some Math functions
print("\nSome math functions")
print(round(3.7))                                 
print(abs(-20))                                   


# $Binary
print("\nConverting to the binary representation and back")
print(bin(5)) #'0b'->represents that it is a binary format
print(int('0b101',2))


# $Variables -> also called binding values
# $use snake_case convention
print("\nUsing variables")
normal_variable = 10
print(normal_variable)

# $Another effective way to assign variables
a,b,c = 1,2,3
print("\na: ",a, ", b :",b)

print("\n'_' in the beginning generally signifies it's a private variable in python")
_normal_variable = 20
print(_normal_variable)


# $Constants -> general convention in CAPITALS
PI = 3.14
print("\n'__variable is known as a dundar in python")
# $so it's not a good practice to have '__' in variable naming convention



# $Expression and Statements
iq = 200
user_age = iq/5   
#'iq/5'            -> is a expression                  #'user_age = iq/5' -> is a statement



# $Augmented assignment operators
some = 5
some +=2
print("\nAugmented operation value :", some)



# $Let's try 'long string' AS DOC STRING
long_str = '''Im Parth
0 0
 _
'''
print("\nThis is the example of a long string")
print(long_str)
# $It can be used to print paragraphs,etc


# $Escape characters
print('\nTrying out the escape characters')
print ('It\'s a beautiful day')
print('\tIts a beautiful day')


# $Formatted Strings
print('\nTrying out formatted strings.')
name = 'Parth'
age = 24
print("Welcome " + name + ". You are "+ str(age) + " years old.")       #print like this
print("Welcome ", name , ". You are ", str(age) , " years old.")        #also can print like this
# $print needs strings, so convert everything in it to strings

print(f"Welcome {name}. You are {age} years old.")                      #also can print like this
print("Welcome {}. You are {} years old.".format(name,age))
print("Welcome {1}. You are {0} years old.".format(name,age))
print("Welcome {_name}. You are {_age} years old.".format(_name="P",_age=25))



# $String manipulation
# $string[start:stop:stepover]
print('\nManipulating Strings')
strin = '01234567'
print(strin[0])
print(strin[0:])
print(strin[:5])
print(strin[0:4])
print(strin[0:8:1])
print(strin[0:8:2])
print(strin[-1]) #index starts from last -1->0 from last
#print(strin.reverse()) ->string cannot be reversed but list can be like this
print(strin[-2])
print(strin[::-1]) #to reverse the string


# $Immutability
strin = '01234567'
#strin[0] = '8'  ->we cannot alter the string characters since string is 'immutable' just as a 'touple'
#we can replace the whole string but not particular characters, once assigned is assigned 
strin = strin+ '8'
print(strin)


# $Boolean
print('\nWorking with booleans')
print(bool(0))
print(bool('True'))         #if casting is possible, interpreter will definately be able to cast it
print(bool(True))

#python has shor-circuting operator 'and' i.e., if the first value is true, it'll check the other value, but if the first value is false, the result has to be false and hence does not check the second value, however, if the first value(default/casted) is true and so is the second value, print statement will print the default value of the second object rather than True or False
True and True
True and False
False and True
bool('hello')   #stuff len>1 is True
bool('')
'' and 'hello' 
'asd' and 'hello' 


# $Most common type conversion error
year = input("\nEnter your birth year :")
age = 2020 - int(year) #this is the part where error occurs most of the time 
print(f"Your current age is {age}")
              


# $Exercise password asterisk
u_name = input("\nEnter the username :")
password = input("Enter the password :")

print(f"Welcome {u_name}, your password :{len(password)* '*'} is {len(password)} letters long")



#Chapter 2 : working with lists 1
# $Working with lists
print('Working with lists')
li = [1,2,3]
li2 = ['a','b','c']
li3 = [1, 2.5, 'c', True]   #it can also hold values of multiple categories
print(li)

# $Unlike strings, list in not immutable i.e, it is mutable (we can change the sub element of the list)

li[1] = 2.5
print('\nNew list')
print(li)

# $Copying list problem
# $it can only done through list slicing
print("\nList copying problem")
cart = ['apple','banana','carrot']
new_cart = cart
new_cart[0] = 'orange'
print(cart)
print('This changed the original cart as it was assigned to it directly instead of slicing and copying, so the original list reference was assigned to the new variable')

print('\n\nThe correct way is by slicing the list or using the copy method')
cart = ['apple','banana','carrot']
new_cart2 = cart[:]
#new_cart2 = cart.copy()      #or by using inbuilt list method
new_cart2[0] = 'orange'
print(cart)



# $appending to a list returns no ValueError
print('\nAppending the list problem')
eg = [1,2,3,4,5]
eg2 = eg.append(100)
print(eg)
print("eg2 : ",eg2) #this will contain None

# $first we need to append seperately as append inPlace=True(according to some methods), just changes the list, does not return anything, similarly 'insert' does inPlace=True i.e., just modifies whatever is in the memory
eg = [1,2,3,4,5]
eg.append(100)          #we can only append one item at a time
eg2 = eg[:]
print("eg2", eg2)

eg.append([100,200])  #this appends a list as single element inside original list
print(eg)

#so to append multiple values, we can use 'extend' and items as a list
eg.extend([200,201]) #takes iterable list as input unlike append
print("eg", eg)



# $Remove(by value) and pop(by index/last element)
eg.pop()
print("eg :", eg)
eg.pop(0)
print("eg :", eg)
p = eg.pop(2) #takes 'index' and returns whatever you just removed
print("eg :", eg , ", Pop value :", p)

eg.remove(5) #takes 'value' and removes it, this also works inPlace=True
print("eg :", eg)

eg.clear() #clears everything from the list
print(eg)

eg = ['a','b','c','d','e','d']
print("index of 'd' is :",str(eg.index('d')))
print("count of 'd' is :", str(eg.count('d')))
print("Is 'd' present in the list 'eg' : ", 'd' in eg)
print("Is 'a' present in 'hello world' ", 'a' in 'hello world')


# $Sorting the lists
print("\nSorting by 2 ways")
eg = ['z', 'a', 'v', 's', 'p']
print("'sort' is inPlace :", eg.sort())   #returns None as inplace=true for this method
print(eg)

eg2 = ['z', 'a', 'v', 's', 'p']
print("'sorted' is not inPlace :",sorted(eg2))

print("\nReversing the list")
print("Original :", eg2)
print(eg2.reverse())  #inplace=True
print("REversed :",eg2)

sorted([5,2,1])
sorted([7,4,9] + [12,7,32])
sorted([1,4,7] + [4,9,12] + [33,76,99])   #sub lists are already sorted, use a better data structure


# $a better approach for sorting long sorted sublists is using merge
from heapq import merge
a = [1,4,7] 
b = [4,9,12] 
c = [33,76,99]
it = merge(a,b,c)      #gives a generator object, an iterable object, a generator is a kind of iterator that runs on demand
list(it)
next(it)               #if you multiple sorted long lists and you need to get first few elements, prefer using merge
next(it)       


# $islice 
# $seems as regular slicing but can also consumes an iterable object and yields an iterable object to save memory along with regular lists
from itertools import islice
islice('abcdef',3)            
list(islice('abcdef',3))        #0,stop
list(islice('abcdef',None,3))   #0,stop
list(islice('abcdef',2,4))      #start,stop
list(islice('abcdef',2,6,2))    #start,stop,step

a = [1,4,7] 
b = [4,9,12] 
c = [33,76,99]
it = merge(a,b,c)
list(islice(it,3))    #suppose you have google qeury responses to show, millions of results, use 'merge' with 'islice' to process only generators and showing content with islice as per as page limit and stuff...
list(islice(it,None)) #returns complete list

# $intern values
# $assign same memory location(& only one) to all strings that are same(lookwise)
s = 'he'
t = 'llo'
u = s+t
w = 'hello'

u,w
u==w              #check the value at the variable reference point
id(u),id(w)       #different references, consumed double memory for single object
u is w            #compares actual reference addresses

import sys
u = sys.intern('hello')
v = sys.intern(s+t)
u is v
id(u),id(v)       #now we did not create redundant data memory, but used reference names to a single memory location
# usecase, don't allow redundant usernames

''''done till here 21 nov 22'''

#Chapter 3 : working with lists 2
# $More with lists
basket = ['a','x','b','c','d','e','d']
basket.sort()
basket.reverse()
print("Reversing again :", basket[::-1]) #inplace=False with to slicing
print("Recersed list   :", basket)

# $Creating list with range
# range is an generator
print("\nRange")
print(range(1,100))
print("\n", list(range(100)))
print("\n", list(range(5,100)))

# $Range in loops
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


# $join
print("\nJoin operation")
sentence = '-'
print(sentence.join(['hi','my','name','is','Parth']))   #does not add before first and after last
print(' '.join(['hi','my','name','is','Parth']))

# $split, default split is by white space
'Hello there, how are you'.split()

# $List unpacking
print("\nList unpacking")
a,b,c,d,*other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)
print(other)
print(d)

import bisect
cuts = [20,40,60,80]
grades = 'EDCBA'
grades[bisect.bisect(cuts,50)]
[grades[bisect.bisect(cuts,x)] for x in [10,30,50,80,100]]


# $Chapter 4 : Dictionary
# $Dictionary -> key,value pairs
# $The keys can be all those objects that are immutable, like strings, booleans but not lists
#keys need to be unique, if not, the last key will override all the other previous keys
print("\nDictionary")
dictionary = {
  'a': [1,2,3],
  123: 'hello integer',           #First key of all same keys will be selected as key and last updated value as the value for the first key
  123.0:'hello float',  
  123.12:'hello double',
  False: True
}
print(dictionary)
print(dictionary['a'])
print(dictionary.get('a',"default_value"))
print(dictionary[123])        #prints float value (if a similar float present)
print(dictionary[123.0])      #prints float value

# $Another way to create a dictionary
dictionary2 = dict(a=[1,2,3], b="asd")    #a,b are taken as key in form as strings
print(dictionary2)
print(dictionary2['b'])

# $Creating list with dictionary
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



# $Eliminate error if key not present in the dictionary
#print(my_list['age'])->this will give error and stop the program after this
dictionary = {
  'a': [1,2,3],
  123: 'hello integer',
}
print(dictionary['age'])          #call by key directly returns 'KeyError' error
print("Returns 'None' in absence of key \"age\": ", dictionary.get('age'))  #call by it's method returns None
print("Returns default if key not present else returns the actual value: \n",dictionary.get('age','default_Age'))

#The setdefault() method returns the value of the item with the specified key.
#If the key does not exist, insert the key, with the specified value
print(dictionary.setdefault("b","b set from default"))
print(dictionary)

# $Or else you can check for a key another way
print("Check for the presence of key 'a' :", 'a' in dictionary)                                     #checks only in keys by default always(simple dictionary object)
print("Check for the presence of value 'hello' :", 'hello' in dictionary)         
print("Check for the presence of value 'hello integer' :", 'hello integer' in dictionary)           #does not check in values by default
print("Check for the presence of key 'a' :", 'a' in dictionary.keys())                              #specify search criteria
print("Check for the presence of value 'hello' :", 'hello' in dictionary.values())
print("Check for the presence of value 'hello integer' :", 'hello integer' in dictionary.values())  #specify search criteria

print(type(dictionary))
print(type(dictionary.items()))
print("Get whole dictionary items in a list(couple):", dictionary.items())
print("Check for the presence of any item(key/value) 'hello integer' :", 'hello integer' in dictionary.items()) #->gives us false. can't do this

dictionary3 = dictionary.copy()
print("dictionary after copying : ", dictionary3)
dictionary.clear()
print("dictionary after clearing : ", dictionary)
print("Pop key value pair :", dictionary3.pop('a'))
print("dictionary3 : ",dictionary3)


# $Update a Value
print("Updating key(123) :", dictionary3.update({123:'hell'})) #inplace=True
# $inserting via update method
print("Updating key(123) :", dictionary3.update({'zebra':'black'})) #inplace=True
print("dictionary3 : ", dictionary3 )


# $Iterating dictionary
dictionary = {
  'a': [1,2,3],
  123: 'hello',
  False: True
}

print("\nIterating the dictionary simply")
for item in dictionary:         #as always, simple dictionary object is linked only with keys
  print(item) #prints the 'keys'

print("\nIterating the dictionary by keys")
for item in dictionary.keys():
  print(item) #prints the 'keys'   

print("\nIterating the dictionary by items")
for item in dictionary.items():
  print(item) #prints the tuple of couples  
  key,value = item #gets value from tuple
  print(key, " : ", value)

print("\nIterating the dictionary by items")
for key,value in dictionary.items(): #gets value from tuple directly
  print(key, " : ", value)  

print("\nIterating the dictionary by values")
for item in dictionary.values():
  print(item) #prints the 'values'    


# $Default dict -> Slight modification of dict except it never raises a 'KeyError'
# $It provides a default value for the key that does not exists.
from collections import defaultdict
#uses: Grouping, accumulation, reversing one-to-one dictionary, reversing one-to-many dictionary
# Function to return a default 
# values for keys that is not 
# present 
def def_value(): 
    return "Not Present"
      
# Defining the default dict 
d = defaultdict(def_value)  #define here what should be the output when key not found as a higher level function name
d["a"] = 1
d["b"] = 2
  
print(d["a"]) 
print(d["b"]) 
print(d["c"])     #this key not present, so default dict will create this new key with the value defined by function specified during it's declaration time

#or
d = defaultdict(lambda:"Not Present")

#therefore now we can also use default dict to group things together
d = defaultdict(set)
d['starts_with_l']
d['starts_with_p'].add('parth')
d['starts_with_l'].add('lathiya')
d['starts_with_l'].add('lavjibhai')
d

# $Excersize ->sum list members
print("\nIterable sum example")
my_list = [1,2,3,4,5,6,7,8,9,10]
sum = 0
for item in my_list:
  sum+=item
print("Total sum of all items = ",str(sum))

#another way to solve(using range)
another_sum = 0
for index in range(len(my_list)):
      another_sum += my_list[index]
print(f'Another Sum : {another_sum}')


# $Enumerate
print("\nEnumerate example")
for item in enumerate("Hellooo"):
  print(item)                   #returns tuples of couples with (index,char)

print("Main purpose -> to get the index from 0")
for index, item in enumerate("Hellooo"):
  print(f'{index} -> {item}')            #hence we can retrive both seperately

print("Main purpose -> to get the index from custom index")
for index, item in enumerate("Hellooo", start=1):
  print(f'{index} -> {item}')            #we can enumerate by specifying the start position as well


# $While loops
print("\nChecking while loops")
i=0
while i<2:
  print("i : ", str(i))
  i+=1
else:
  print("done with all the work")  

i=0
while i<50:
  print("\ni : ", str(i))
  break     #breaks out in the first iteration itself without even running 'else' part
else:
  print("done with all the work")   #does not runs after break, 'else' is used only if the whole loop completes without any break successfully and we need to show some message

# $While example
while True:
  response = input("Chat 'bye' to exit :")
  if("bye" in response.split()):
    break

# $'continue' example
# $skip if you get '3'
print("\nSkipping no. 3")
for item in [1,2,3,4,5]:
  if(item == 3):
    continue
  else:
    print(item)

# $'pass' example
# $it is absolutely nothing, if you're using for loop and you don't know what to right, indentation error will arise. Thereyou can use pass as a placeholder
for x in [1,2,3]:
  pass

#iterator magic
#(partially consumed iterable)
it = iter('abcdefg')        #make anything iterable, now it follows iterable protocol with additional tools as 'next', etc.
next(it)
next(it)        #not only it iterates element one by one but it is halted at that place, see by making the list with the rest of the iterator object
list(it)        #surprise, this is helpful if you want to parse the incomming header with the id and iterate over the received data


# Chapter 5 :
# $Starting with tuple -> immutable
# $therefore it can be used as a key in the dictionary and not the list(which is mutable)

my_tuple = (1,2,3,4,5) #faster than list. use for unchangabe items and security

# $This won't work because list is mutable
# user = {
#   [1,2] : [1,2,3],
#   'greet' : 'hello',
#   'age' : 24
# }

user = {
  (1,2) : [1,2,3],
  'greet' : 'hello',
  'age' : 24
}

print("Calling value using tuple(as key)",user[(1,2)])


# $tuple stuff
new_tuple = my_tuple[:]
x,y,z, *other = new_tuple
print("\nSlicing tuple :", my_tuple[2:3])
print("Slicing tuple :", my_tuple[2:])
print("x : ",x)
print("y : ",y)
print("z : ",z)
print("other : ",other)
print("Count '5' occurances: ", new_tuple.count(5))
print("Index of '5' occurance: ", new_tuple.index(5))
print("Length of the tuple :", len(new_tuple))



# Chapter 6 : Sets
# $unordered collections of unique sets
#sets will always return themselves(after defining) as sorted, with unique items

my_set = {1,2,3,4,5}
print("my_set : ", my_set) #ascending

my_set = {1,5,3,4,5,5,2,5,5,5}
print("my_set : ", my_set) #ascending

# $convert a list into a set
my_list = [9,4,5,4,4,2,2,1]
my_list_set = set(my_list)
my_list_back = list(my_list_set)
print("\nList converted to set :", my_list_set)
# $useful in sending emails to a list containing duplicate emails

# $Exercise -> count each element's count in a list
exe_list = [1,5,3,1,6,9,6,4,6,2,5,8,4,2,4,7,8,9,4,2,1,6]
for item in exe_list:
      print(f'element: {item} : count: {exe_list.count(item)}')

# $Exercise -> count each element's count in a list more effectively(without implementing count function on the same element >twice)
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




# $Set's methods#
#################
#Remember the venn diagram
#################
# .difference()
# .discard()
# .difference_update()
# .isdisjoint()
# .issubset()
# .issuperset()
# .union()

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

print("\nSet operations/methods")
print("Difference :", my_set.difference(your_set)) #just tells us the differemnce, not update the set #remove common things from me
print("Difference :", my_set.difference_update(your_set)) #finds the differemce and updates the original set #inPlace=True
print("my_set : ",my_set)
print("Discard : ", my_set.discard(1)) #inplace=True
print("my_set after discarding '5' : ",my_set)

my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print("Intersection :", my_set.intersection(your_set)) 
print("Intersection(another method) : ", my_set&your_set)
#common things

print("\nDisjoint(is there anything common. are they not overlapped?) : ", my_set.isdisjoint(your_set))

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
print("Reversing again :", basket[::-1]) #inplace=False due to slicing
print("Original list   :", basket)

# $Creating list with range
print("\nRange")
print(range(1,100))
print("\n", list(range(100)))
print("\n", list(range(5,100)))


# $join
print("\nJoin operation")
sentence = '!'
print(sentence.join(['hi','my','name','is','Parth']))
print(' '.join(['hi','my','name','is','Parth']))


# $List unpacking
print("\nList unpacking")
a,b,c,d,*other,d = [1,2,3,4,5,6,7,8,9]
print(a)
print(b)
print(c)
print(d)
print(other)
print(d)


# Chapter 7 : working with lists 3
#  # More with lists
# using this list, 
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# 1. Remove the Banana from the list
print(basket.remove('Banana'))
print(basket)
# 2. Remove "Blueberries" from the list.
print(basket.pop())
print(basket)
# 3. Put "Kiwi" at the end of the list.
print(basket.append("Kiwi"))
print(basket)
# 4. Add "Apples" at the beginning of the list
print(basket.insert(0,"Apples"))
print(basket)
# 5. Count how many apples in the basket
print(basket.count("Apples"))
# 6. empty the basket
print(basket.clear())
print(basket)


# Chapter 8 :
# using this list: 
basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
# access "Oranges" and print it:
# You will find the answer if you scroll down to the bottom, but attempt it yourself first!

print(basket[1][1][0])


# Solution:
# basket[1][1][0]


# Chapter 9 : Operator Precedence
# Guess the output of each answer before you click RUN
# Try to write down your answer before and see how you do... keep it mind I made it a little tricky for you :)

print((5 + 4) * 10 / 2)
#450

print(((5 + 4) * 10) / 2)
#45
print((5 + 4) * (10 / 2))
#45
print(5 + (4 * 10) / 2)
#25
print(5 + 4 * 10 // 2)
#45


# Chapter 10 :String Formatting
# 1 What would be the output of the below 4 print statements? 
#Try to answer these before you click RUN!

print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

# 2 How would you write this using f-string? (Scroll down for answer)
name='cindy'
amount=50
print(f"hello {name}, your balance is {amount}")

name = 'Cindy'
amount = 50
print(f"Hello {name}, your balance is {amount}.")



# Chapter 11 : Miscelleaneous
# $Condtions
# $Truthy and Falsy

x,xx = "Hello",""
y,yy = 20,0

print(f"x:{bool(x)}, xx:{bool(xx)},\ny:{bool(y)}, yy:{bool(yy)}")

# $Check is username or password exists
username = "Parth"
password = '123'

if username and password:
  print("\nusername,password do exists")
else:
  print("\nusername,password don't exists")

username = "Parth"
password = ''
print("Current password :", bool(password))
if username and password:
  print("\nusername,password do exists")
else:
  print("\nusername,password don't exists")

# $Ternary operator
#Note: Ternary operator returns only expressions on both sides, statements are NOT allowed
is_friend = True
can_message = "message allowed" if is_friend else "message not allowed"
print("\ncan_message :", can_message)

#Failed eg.
# li = [(1,2), (2,2), (3,1)]
# res = [0, 0]
# for x,y in li:
#       res[0] += 1 if x > y else res[1] += 1  #cannot assign in ternary operators
# #Sol for Failed eg
# for x,y in li:
#       r = 0 if x > y else 1
#       li[r]+=1
      


# $Wizard if else
is_magician = False
is_expert = True
if is_magician and is_expert:
  print("\nYou are a master magician")
elif is_magician and not is_expert:
  print("\nAtleast you're getting somewhere")
elif not is_magician:
  print("You need magic powers")

# $is vs ==
print("\n'is'-> compares content at the passed value memory location")
print(True is True)
print('1' is '1')
print([] is []) #data structures are created at different locations
print(10 is 10)
print([1,2,3] is [1,2,3])

# $concept
a = [1,2]
b = [1,2]
memory = "Same memory" if a is b else "Different memory"
print("\nMemory location : ", memory)

print("\n'=='-> compares content")
print(True == True)
print('1' == '1')
print([] == []) #data structures are created at different locations, but currently content is same
print(10 == 10.0)
print([1,2,3] == [1,2,3])

# $Loops
# $Iterable ->list,dictionary,tuple,strings,set
print("\nFor loop")
for item in "Hi Duh!":    #'ji duh!'->is an iterable item
  print(item)

for item in reversed("Hi Duh!"):
      print(item)

for item in [1,2,3]:    
  print(item)

for item in {1,2,3}:    
  print(item)  

for item in (1,2,3):    
  print(item)



  #Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for row in picture: #name as readable/rememberable as possible
  for pixel in row:
    # if pixel == 0:  #you can clean it
    if not pixel: 
      print(" ",end='') #we need this to override the default end='\n' from the print
    else:
      print("*",end='')
  print("\n")    


# $Some excersize 
# $Create a new list indicating multiple entrie items
some_list = ['a','b','c','b','d','m','n','n']
duplicates = []

for item in some_list:
  if some_list.count(item) > 1:
    if item not in duplicates:
      duplicates.append(item)
  
print(duplicates)



# $Functions ->takes parameters
# $Methods ->are a part of objects
# $Generic
def call_me():
  print("You have called me!")

print(call_me)  #function name and memory location
call_me()


# $Positional arguments->position matters in argument
def call_me(name,age):  # <-this is parameter
  print(f"\nYou have called me {name}! of {age} age")

call_me("Parth",24) # <- this is argument 

# $Keyword arguments #('can be confused with default arguments)
call_me(age=25, name="Zeal")  # <-bad practice


# $Default parameters
def call_me(name="Default",age=25):  # <-this is parameter
  print(f"\nYou have called me {name}! of {age} age")

call_me()

# $calling function inside of a function
def outer_function():

  print("\nOuter function`")
  def inner_function():
    print("\nInner function")

  return inner_function()

outer_function()


# $'*args' and '**kwargs'
# $passing any number of arguments as 1 parameter

# def some_fn(args):
#   return sum(args)

# some_fn(1,2,3,4,5)  # <=this will give error as some_fn above only takes one argument

def some_fn(*args):   # -> args stored as tuple
  return sum(args)

print("\n'args' gets stored as a tuple, Sum :",some_fn(1,2,3,4,5))


# $using '**kwargs'
def some_fn(**kwargs):
  print(kwargs)
  print(kwargs['item1'])
  return sum(kwargs.values())

print("\n'kwargs' contains a dictionary, Sum :",some_fn(item1=5, item2=10))



# $Combination of all
# $Rule: params, *args, default_params, **kwargs
def some_fn(name,*args,age=24,**kwargs):
  return sum(kwargs.values()) + sum(args)

print("\nCombination :",some_fn('Parth',1,2,3,4,5,25,item1=5, item2=10))


# $partials (freeze the function and reduce the number of parameters by assigning some parameters by default)
from functools import partial

pow(2,5)  #this is an inbuilt function
two_pow = partial(pow,2)    #passed one argument and freezed it into a variable
two_pow(5)    #call the freezed partial function with the remaining arguments
