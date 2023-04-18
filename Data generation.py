#Generate 3 random integers between 100 and 999 which is divisible by 5
import random

print("Generating 3 random integer number between 100 and 999 divisible by 5")
for num in range(3):
    print(random.randrange(100, 999, 5), end=', ')

# Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.
import random

lottery_tickets_list = []
print("creating 100 random lottery tickets")
# to get 100 ticket
for i in range(100):
    # ticket number must be 10 digit (1000000000, 9999999999)
    lottery_tickets_list.append(random.randrange(1000000000, 9999999999))
# pick 2 luck tickets
winners = random.sample(lottery_tickets_list, 2)
print("Lucky 2 lottery tickets are", winners)

# Generate 6 digit random secure OTP
import secrets

#Getting systemRandom class instance out of secrets module
secretsGenerator = secrets.SystemRandom()

print("Generating 6 digit random OTP")
otp = secretsGenerator.randrange(100000, 999999)

print("Secure random OTP is ", otp)

#Pick a random character from a given String
import random

name = 'pynative'
char = random.choice(name)
print("random char is ", char)

#Generate random String of length 5
import random
import string

def randomString(stringLength):
    """Generate a random string of 5 charcters"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

print ("Random String is ", randomString(5) )

# Generate a random Password which meets the following conditions
import random
import string

def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(randomSource, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

print ("Password is ", randomPassword())

#Calculate multiplication of two random float numbers
import random

num1  = random.random()
print("First Random float is ", num1)
num2 = random.uniform(9.5, 99.5)
print("Second Random float is ", num1)

num3 = num1 * num2
print("Multiplication is ", num3)

# Generate random secure token of 64 bytes and random URL
import secrets

print("Random secure Hexadecimal token is ", secrets.token_hex(64))
print("Random secure URL is ", secrets.token_urlsafe(64))

#Roll dice in such a way that every time you get the same number
import random

dice = [1, 2, 3, 4, 5, 6]
print("Randomly selecting same number of a dice")
for i in range(5):
    random.seed(25)
    print(random.choice(dice))

#Generate a random date between given start and end dates
import random
import time

def getRandomDate(startDate, endDate ):
    print("Printing random date between", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print ("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))
