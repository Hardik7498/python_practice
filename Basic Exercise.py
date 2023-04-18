#1)Calculate the multiplication and sum of two numbers
def multiplication_or_sum(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

result = multiplication_or_sum(20, 30)
print("The result is", result)

result = multiplication_or_sum(40, 30)
print("The result is", result)

#2)Print the sum of the current number and the previous number
print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)

    previous_num = i

#3)Print characters from a string that are present at an even index number
# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

size = len(word)

print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])

#4)Remove first n characters from a string
def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x

print("Removing characters from a string")
print(remove_chars("pynative", 4))
print(remove_chars("pynative", 2))

#5)Check if the first and last number of a list is the same
def first_last_same(numberList):
    print("Given list:", numberList)

    first_num = numberList[0]
    last_num = numberList[-1]

    if first_num == last_num:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
print("result is", first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("result is", first_last_same(numbers_y))

#6)Display numbers divisible by 5 from a list
num_list = [10, 20, 33, 46, 55]
print("Given list:", num_list)
print('Divisible by 5:')
for num in num_list:
    if num % 5 == 0:
        print(num)

#7) Return the count of a given substring from a string
def count_emma(statement):
    print("Given String: ", statement)
    count = 0
    for i in range(len(statement) - 1):
        count += statement[i: i + 4] == 'Emma'
    return count

count = count_emma("Emma is good developer. Emma is a writer")
print("Emma appeared ", count, "times")

#8)Print the following pattern
for num in range(10):
    for i in range(num):
        print (num, end=" ")
    print("\n")

#9)Check Palindrome Number
def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")


palindrome(121)
palindrome(125)

#10)Create a new list from a two list using the following condition
def merge_list(list1, list2):
    result_list = []

    for num in list1:

        if num % 2 != 0:

            result_list.append(num)


    for num in list2:
        if num % 2 == 0:

            result_list.append(num)
    return result_list


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))

#11) Write a Program to extract each digit from an integer in the reverse order.
number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")

 #12)Calculate income tax for the given income by adhering to the below rules
income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:

    x = income - 10000

    tax_payable = x * 10 / 100
else:

    tax_payable = 0


    tax_payable = 10000 * 10 / 100


    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)

#13) Print multiplication table form 1 to 10.
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")

#14)Print downward Half-Pyramid Pattern with Star.
for i in range(6, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

#15)Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
def exponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num - 1
    print(base, "raises to the power of", exp, "is: ", result)

exponent(5, 4)