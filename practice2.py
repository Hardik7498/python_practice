#------------------ 1.2 Part 1 -----------------
#fstrings
#in digit
x=10
print(f'Convert \'x\' to 8 digits number: {x:08d}')

#in error
raise ValueError(f'Expected {x} to a float not a {type(x).__name__}')       #very useful

#use counter object #useful in data analysis
from collections import Counter         #sub class of dictionary, just as default dict is a type of dict, it is also a type of dict
d={}
d['dragons']       
d=Counter()
d['dragons']       

d['dragons'] += 1   
d['dragons'] += 1   
d
list(d.elements())

#Counter is a container that holds the count and element name, and unpacks all elements on elements() method call only, till then it stays in the dictionaty format
c = Counter('red green blue green blue blue'.split())   #default split is done by white spaces and counter automatically counts and forms a 'Counter' object, no need to run 'for' loop
c

c.most_common(1)        
c.most_common(2)        
list(c.elements())           

#descriptive statistice module (better results that self made calculations)
from statistics import mean,median,mode,stdev,pstdev

mean([50,52,53])
median([50,52,53])
mode([50,52,53, 53])
stdev([50,52,53,50,52,53])  
pstdev([50,52,53,50,52,53]) 

#list concatination
s = [10,20,30,40]          
t = [50,60,70,80]
u = s+t
u

u[:2]+u[-2:]              
dir(list)           

s = 'abrakadabra'
s.index('k')
s.count('b')        

s = [10,5,29,4]
s.sort()        
s

s = [10,5,29,4]
sorted(s)       
s

sorted('cat')  

#lambda -> people forget and use -> partial, itemgetter, attrgetter, ...
# raymen hettinger says forget all new stuff and just use lambda
# lambda makes a nameless one-time use and throw away function
lambda x:x**2

(lambda x:x**2)(5)

2+ (lambda x:x**2)(3) + 5

f = lambda x,y: x**2 + y       
f(2,3)

#defer a computation for future by making a function of no arguments(also called promises, freez and thaw, thunks), used when someone triggers an event in an async type i/o event or pressing button in GUI widget
x,y=2,3 
f = lambda : x**y       

#call in future
f()

# or to defer a computation for future by passing one argument, use partial
from functools import partial
def sum(x,y):
    print(x+y)
x=2
sum_partial = partial(sum,x)
sum_partial(y)

#chained expression
x=15
6<x<20                  







#------------------ 1.2 Part 2 -----------------
#random module
from random import *

#produce same results in random(reproduce results in stimulations, publish seed in testing results(reproduceable research))
seed(8473940)
random()
random()
random()

seed(8473940)
random()       
random()
random()

uniform(1000,1100)     
triangular(1000,1100)   
triangular(1000,1100)
triangular(1000,1100)

gauss(100,15)           #(number, random->standard_deviation) #returns number around 100 += random standard deviation

expovariate(1/5)       
#let's check statistics for above methods
from statistics import mean, stdev

data = [triangular(1000,1100) for x in range(1000)]
mean(data)         
stdev(data)        

data = [uniform(1000,1100) for x in range(1000)]
mean(data)         
stdev(data)        

data = [gauss(100,15) for x in range(1000)]
mean(data)          
stdev(data)         


from random import choice,choices, sample,shuffle
outcomes = ['win','lose','draw','play again','double win']
choice(outcomes)    
choice(outcomes)
choice(outcomes)
choice(outcomes)
choice(range(100))  

choices(outcomes,k=3)   
choices(outcomes, [5,4,3,2,1], k=10)   

sample(outcomes, k=4)       
sample(outcomes, k=6)       
sample(range(100), k=2)         

from collections import Counter

Counter(choices(outcomes, k=100))
Counter(choices(outcomes,[5,4,3,2,1], k=100))   

#shuffle
outcomes
shuffle(outcomes)
outcomes        

#exercise, lottery ticket draw, ticket number must not be repeated, show them in sorted order
your_ticket_no = 25
declared_list = sorted(sample(range(1,100), k=5))
print('won') if your_ticket_no in declared_list else print('better luck next time!')

#------------------ 2.1 Part 1 -----------------
# Statictics module
from random import *                    
from statistics import *               
from collections import *              

#----> Six roulette wheels --18 red 18 black 2 green
population = ['red']*18 + ['black']*18 + ['green']*2
Counter(population)

[choice(population) for x in range(6)]               
Counter([choice(population) for x in range(6)])     

#another way
choices(population, k=6)
Counter(choices(population, k=6))

#best way
choices(['red','black','green'], [18,18,2], k=6)
Counter(choices(['red','black','green'], [18,18,2], k=6))

deck = Counter(tens=16, low=36)         
deck
deck = list(deck.elements())            
deal = sample(deck,20)                 
deal
Counter(deal)                          

#summarise
deck = Counter(tens=16, low=36)    
deck = list(deck.elements())           
deal = sample(deck, k=52)               
remaining_cards = deal[20:]             
Counter(remaining_cards)               

#----> prob of 5 or more heads from 7 spins of a biased coin
trial = lambda: choices(['heads','tails'], cum_weights=[0.60,1.00], k=7).count('heads')>=5     
trial()
sum([True]*2)      
total_trials = 1000
sum(trial() for x in range(total_trials))/total_trials

#----> prob that the median of 5 samples falls in a middle quartile(b/w 1/4 and 3/4 of total)
total_numbers = 10000
total_numbers//4
total_numbers*3//4
sample(range(total_numbers), k=5)

median(sample(range(total_numbers), k=5))

#another method for median
sample(range(total_numbers), k=5)[2]   

#summary
total_numbers = 10000
trial = lambda: total_numbers//4 < median(sample(range(total_numbers), 5)) <= total_numbers*3//4
sum(trial() for x in range(total_numbers))/total_numbers


#------------------ 2.2 Part 2 -----------------
#----> Bootstrapping to estimate the confidence interval on a sample of data
#build a 90% confidence interval for means in a dataset
timings = [7.18, 8.59, 12.24, 7.39, 8.19, 8.69, 6.98, 8.31, 9.06, 7.06, 7.67, 10.02, 6.68, 9.07]

from statistics import mean, stdev
mean(timings)
stdev(timings)

def bootstrap(data):
    return choices(data, k=len(data))

from random import choices
bootstrap(timings)
mean(bootstrap(timings))
trial = lambda: mean(bootstrap(timings))
total_numbers = 10000
means = sorted(trial() for x in range(total_numbers))
len(means)
means[:20]
means[-20:]
#90% confidence range would be [5% to 95%] values, i.e., 1st 500 onwards till leving last 500 values
means[500]
means[-500]
print(f'The observed mean of total data: {mean(means)}')
print(f'Falls in a 90% confidence interval from mean value outcomes {means[500]:.1f} to {means[-500]:.1f}')

#summary
timings = [7.18, 8.59, 12.24, 7.39, 8.19, 8.69, 6.98, 8.31, 9.06, 7.06, 7.67, 10.02, 6.68, 9.07]
total_numbers = 10000
def bootstrap(data):
    return choices(data, k=len(data))
trial = lambda: mean(bootstrap(timings))
means = sorted(trial() for x in range(total_numbers))
print(f'Falls in a 90% confidence interval from mean value outcomes {means[500]:.1f} to {means[-500]:.1f}')

#----> birth study giving drug to females(drug result and placebo result)
# Statistical difference of the difference of two means
# if difference is almost same, drug did not have an effect, else it did have an effect
drug_results = [7.1, 8.5, 6.4, 7.7, 8.2, 7.6, 8.4, 5.1, 8.1, 7.4, 6.9, 8.4]
placebo_results = [8.2, 6.1, 7.1, 7.1, 4.9, 7.4, 8.1, 7.1, 6.2, 7.0, 6.6, 6.3]
len(drug_results)
len(placebo_results)

mean(drug_results)     
mean(placebo_results)  

obs_diff = mean(drug_results) - mean(placebo_results)
obs_diff                

combination = drug_results + placebo_results
nd = len(drug_results)
shuffle(combination)    #inplace=True, #now we'vs mixed and shuffled drug and placebo users
combination[:nd]
combination[nd:]        

#if we reshufftle (permutung,relabeling) the participant,
#is the new mean diff the same or more extreme than be observed
#summary
def trial():
    shuffle(combination)
    drug_results = combination[:nd]
    palcebo_results = combination[nd:]
    new_diff = mean(drug_results) - mean(placebo_results)
    return new_diff >= obs_diff                             #is the new result more extreme than before i.e, did it make change?
sum(trial() for x in range(total_numbers))/total_numbers    #precentage of change it made to total trials

#------------------ 3.1 Part 1 -----------------
#help us understand our code better and improve documentation and error checking
#topic: type hinting
#add little bit of code and understand your code better

#code in another file named: 'hints.py'


#------------------ 3.1 Part 2 -----------------
#grouping
from collections import defaultdict
names = ''' parth samjay zeal zeel bhoomit helly 
anjali uttam rahul singham brijesh shlok zelu rajeshvar raj mahesh'''.split()
#group all these names according to their first name letter
d = defaultdict(list)
for name in names:
    feature = name[0]
    d[feature].append(name)
pprint(d)

d = defaultdict(list)
for name in names:
    feature = len(name)        
    d[feature].append(name)
pprint(d)

#sort by custom key
pprint(sorted(names, key=len))

#zipping
list(zip('abcde','fghijk'))         

from itertools import zip_longest
list(zip_longest('abcde','fghijk')) 
list(zip_longest('abcde','fghijk', fillvalue='x')) 

m = [[10,20],
    [30,40],
    [50,60]
]
# 3 rows and 2 columns
pprint(list(zip([10,20],[30,40],[50,60])), width=20)    
#another way transposing matrix zip*
pprint(list(zip(*m)),width=20)


#convert any iterator into list
it = iter('abcde')
it
list(it)



#-------------------- 4.1 Part 1 -------------------
#Implementing k-means unsupervised machine learning
# Code implemented in kmeans.py with mypy structure

#-------------------- 4.1 Part 2 -------------------

#additional code to 'kmeans.py' with addition type hinting and more


#-------------------- 5.1 Part 1 -------------------
#Implementing k-means unsupervised machine learning
# Code implemented in session_congress1.py with mypy structure

#-------------------- 5.1 Part 2 -------------------
import glob         #global wild card expansion
glob.glob('*.txt')       

#open a file with encoding in it
with open('../Modernpython/congress_data/congress_votes_114-2016_s20.csv') as f:      
    print(f.read())

with open('../Modernpython/congress_data/congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    print(f.read())         

import csv
with open('../Modernpython/congress_data/congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    print(next(csv.reader(f)))     
    for row in csv.reader(f):       
        print(row)



#-------------------- 6 Part 1 -------------------
#load and transform data with ML
# code in 'congress.py'

#-------------------- 7 Part 1 -------------------
print("TheRaymondWay\N{trade mark sign}")

#encoding characters
s = 'L' + chr(246) + 'wis'
t = 'L' + chr(111) + chr(776) + 'wis'
s,t     
s==t

#decoding characters
[ord(s) for s in s]
[ord(t) for t in t]    

#Note: always normalize before any lookups are performed
import unicodedata
u = unicodedata.normalize('NFC',t)
[ord(u) for u in u]     




#MAke it simple, faster and easier to read

#-------> and comparision
a,b = 5,5

# bad
print('same') if a == 5 and b == 5 else print('different')

# best
print('same') if a==b==5 else print('different')   

#-------> looping number of times
#1 bad
for i in [0,1,2,3,4,5]:
    print (i)

#1 best
for i in range(6):                                 
    print (i)

#-------> looping each value
fruits = ['apples', 'bananas', 'grapes', 'tomatos']

#2 bad
for index in range(len(fruits)):
    print (fruits[index])                   

#2 best
for fruit in fruits:
    print(fruit)

#-------> looping each value backwords
fruits = ['apples', 'bananas', 'grapes', 'tomatos']

#2 bad
for index in range(len(fruits)-1,-1,-1):
    print (fruits[index])

#2 best
for fruit in reversed(fruits):
    print(fruit)

#-------> looping each value with indices
fruits = ['apples', 'bananas', 'grapes', 'tomatos']

#3 bad
for index in range(len(fruits)):
    print (f'{index} -> {fruits[index]}')

#3 best
for index,fruit in enumerate(fruits):
    print (f'{index} -> {fruit}')

#-------> looping multiple lists at once(note both list's lengths)
fruits = ['apples', 'bananas', 'grapes', 'tomatos']
vegetables = ['carrot', 'spinach', 'cucumber']

#4 bad
smaller_size = min(len(fruits), len(vegetables))
for index in range(smaller_size):
    print (f'{fruits[index]} -> {vegetables[index]}')       

#4 best
for fruit,vegetable in zip(fruits,vegetables):      
    print (f'{fruit} -> {vegetable}')

#with uneven list sizes
from itertools import zip_longest
for fruit,vegetable in zip_longest(fruits,vegetables, fillvalue='None'):
    print(f'{fruit} -> {vegetable}')

#-------> looping in sorted order
fruits = ['apples','ginger' ,'bananas', 'grapes', 'tomatos']

#5 bad
fruits.sort()                                       
for fruit in fruits:
    print (fruit)
print(fruits)                                      

_fruits = ['apples','ginger' ,'bananas', 'grapes', 'tomatos']
#5 best
for fruit in sorted(_fruits):
    print(fruit)
print(_fruits)                                      

#5 best reverse
for fruit in sorted(_fruits, reverse=True):
    print(fruit)

#5 best compare lengths
lengths = ['asd', 'dsgerg', 'rgsdgsdrwd', 'e', 'fw', 'reg', 'z']
print(sorted(lengths, key=len))

#-------> finding value in loops
#6 bad
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

#6 better
users = ['parth', 'helly', 'nidhi', 'bhoomit']
find_name = 'nidhi'
for user in users:
    if user == find_name:
        print("Found!")
        break
else:
    print("Not Found!")

#6 best
users = ['parth', 'helly', 'nidhi', 'bhoomit']
find_name = 'nidhi'
print(f'User Found! at index: {users.index(find_name)}') if find_name in users else print("Not Found!")

#-------> delete item from dictionary while iterating
#7 bad
my_dict = {'cat':'milk', 'bee':'honey', 'dog':'bone'}
for key in my_dict:                                  
    if key.startswith('b'):
        del my_dict[key]
print(my_dict)

#7 best
my_dict = {'cat':'milk', 'bee':'honey', 'dog':'bone'}
for key in list(my_dict):                             
    if key.startswith('b'):
        del my_dict[key]
print(my_dict)

#-------> looking over dictionary key and value
my_dict = {'cat':'milk', 'bee':'honey', 'dog':'bone'}

#8 bad
for key in my_dict: 
    print(f'{key} -> {my_dict[key]}')                      

#8 best   
my_dict = {'cat':'milk', 'bee':'honey', 'dog':'bone'}
for key, value in my_dict.items():                   
    print(f'{key} --> {value}')


#-------> creating dictionary from two lists
users = ['parth', 'helly', 'nidhi', 'bhoomit']
fruits = ['apples','ginger' ,'bananas']               

#9 best
my_dict = dict(zip(users,fruits))                      
print(my_dict)

#-------> Merging two dicts
x = {'a':1, 'b':2}
y = {'b':3, 'c':4}
z={**x, **y}
z                   
#-------> grouping items by length into a dictionary
users = ['parth', 'helly', 'nidhi', 'bhoomit']

#10 bad
d = {}
for user in users:
    key = len(user)
    if key not in d:
        d[key] = []
    d[key].append(user)
print(d)

#10 better
users = ['parth', 'helly', 'nidhi', 'bhoomit', 'zeal', 'zeel', 'uttam', 'vaikunth', 'shlok']
d = {}
for user in users:
    key = len(user)
    d.setdefault(key,[]).append(user)       
print(d)

#10 best
users = ['bhoomit', 'parth', 'helly', 'nidhi', 'zeal', 'uttam', 'vaikunth', 'shlok']

from collections import defaultdict
d = defaultdict(list)
for user in users:
    key = len(user)
    d[key].append(user)
print(d)

#-------> bonus: #reversing one-to-one dictionary
# bad
eng_to_span = dict(one='uno', two='dos', three='tres')
span_to_eng = dict()
for x,y in eng_to_span.items():
  span_to_eng[y] = x
span_to_eng

#best
eng_to_span = dict(one='uno', two='dos', three='tres')
span_to_eng = {v:k for k,v in eng_to_span.items()}
span_to_eng

#-------> bonus: #reversing one-to-many using default dictionary
e2s = {                         
    'one':['uno'],
    'free':['libre','gratis']
}

#best
from collections import defaultdict
from pprint import pprint
s2e = defaultdict(list)
for k,listt in e2s.items():
    for v in listt:
        s2e[v].append(k)
pprint(s2e, width=40)

#-------> clarify names in function calls
def fun(username, password, is_premium_user):
    pass

#11 bad
fun('Parth',"2sf6h", True)

#11 best
fun(username="Parth", password="2sf6h", is_premium_user=True)

#-------> clarify multiple return values with named tuples
#12 bad
class_result = (9,1)
print(class_result)             

#12 best
from collections import namedtuple
Class_Result = namedtuple('Result', ['passes','fails'])
#or
Class_Result = NamedTuple('Result', [('passes',int), ('fails',int)])
class_result = Class_Result(9,1)
print(class_result)                 
print(class_result[0])              
print(class_result.passes)          

#-------> unpacking sequences
my_tuple = 'hi','how','are','you'   
print(my_tuple)

#13 bad
p = my_tuple[0]
q = my_tuple[1]
r = my_tuple[2]
s = my_tuple[3]

#13 best
p,q,r,s = my_tuple

#-------> updating multiple state variables

#14 bad
def fibonacci(len_fib):
    x=0
    y=1
    for i in range(len_fib):
        print(x, end=', ')
        t = y
        y = x+y
        x = t
fibonacci(len_fib=10)

#14 best
def fibonacci(len_fib):
    x,y = 0,1
    for i in range(len_fib):
        print(x, end=", ")
        x,y = y, x+y                           
fibonacci(len_fib=10)

#-------> concatenating strings
my_list = ['hi','how','are','you']

#15 bad
s = my_list[0]
for item in my_list[1:]:
    s += ", " + item
print(s)

#15 best
s = ', '.join(my_list)
print(s)

#-------> updating sequences

#16 bad
my_list = ['hi','how','are','you']
del[my_list[0]]
my_list.pop()
my_list.insert(0,"yo!")
print(my_list)

#16 best
from collections import deque
my_new_list = deque(['hi','how','are','you'])      
del[my_new_list[0]]
my_new_list.pop()
my_new_list.insert(0,"yo!")
print(my_new_list)
my_new_list[0]
[*my_new_list]         

#-------> open and close files
#17 bad
f = open('Some_Code.txt')
try:
    data = f.read()
finally:
    f.close()

#17 best
with open ('Some_Code.txt') as f:                 
    data = f.read()

#-------> how to use locks
import threading
lock = threading.Lock()

#18 bad 
lock.acquire()
try:
    print('Critical Section 1')
    print('Critical Section 2')
finally:
    lock.release()

#18 best
with lock:                                         
    print('Critical Section 1')
    print('Critical Section 2')

#-------> exercise: sum of squares first 10 numbers
#19 bad (shows how you can do it)
squares = []
for number in range(10):
    squares.append(number**2)
print(f'sum :{sum(squares)}')

#19 better (shows single unit of thought)
print(f'sum :{sum([x**2 for x in range(10)])}')    

#19 best
print(f'sum :{sum(x**2 for x in range(10))}')       

#-------> form large list with same element multiple times
from collections import Counter     

#20 bad
my_list = ["list_item" for x in range(10)]
my_list
Counter(my_list)

#20 best
my_list = ["list_item"]*10
my_list
Counter(my_list)


#-------> Summing
#21 bad
sum([0.1]*10)
sum([0.1]*10) == 1        

#21 best
from math import fsum
fsum([0.1]*10)
fsum([0.1]*10) == 1         

#-------> Printing
from collections import defaultdict
d = defaultdict(list)
d['p'].append('parthiv')
d['z'].append('zeal')
d['p'].append('parth')

#22 normal
print(d)

#22 best
from pprint import pprint
pprint(d, width=40)

#-------> Deflating matrix
m=[
    [10,20],
    [30,40],
    [50,60]
]

#23 bad
for row in m:
    for column in row:
        print(f'{column}', end=", ")

#23 best
print([x for row in m for x in row])


# Sample Input: abcdefghi -> abc def ghi

# Make string iterable as object
s = 'abadffghi'
list(zip(s,s,s))

s = 'abadffghi'
it = iter(s)
list(zip(it,it,it))    

for part in zip([iter('abadffghi')]*3):
	print(part)

di = dict({'a':1,'b':2})
di.setdefault('c',3)   

list(zip(['abc','def','ghi']))
list(zip(*['abc','def','ghi']))

for part in zip(*[iter('abadffghi')]*3):
    di = dict()
    "".join([di.setdefault(char,char) for char in part if char not in di])