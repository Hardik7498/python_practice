#Accept numbers from a user
num1 = int(input("Enter first number "))
num2 = int(input("Enter second number "))

res = num1 * num2
print("Multiplication is", res)

#Display three string “Name”, “Is”, “James” as “Name**Is**James”
print('My', 'Name', 'Is', 'James', sep='**')

# Convert Decimal number to octal using print() output formatting
num = 8
print('%o' % num)

# Display float number with 2 decimal places using print()
num = 458.541315
print('%.2f' % num)

#Accept a list of 5 float numbers as an input from the user
numbers = []

# 5 is the list size
# run loop 5 times
for i in range(0, 5):
    print("Enter number at location", i, ":")
    # accept float number from user
    item = float(input())
    # add it to the list
    numbers.append(item)

print("User List:", numbers)

#Write all content of a given file into a new file by skipping line number 5
# read test.txt
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()

# open new file in write mode
with open("new_file.txt", "w") as fp:
    count = 0
    # iterate each lines from a test.txt
    for line in lines:
        # skip 5th lines
        if count == 4:
            count += 1
            continue
        else:
            # write current line
            fp.write(line)
        # in each iteration reduce the count
        count += 1

#Accept any three string from one input() call
str1, str2, str3 = input("Enter three string").split()
print('Name1:', str1)
print('Name2:', str2)
print('Name3:', str3)

# Format variables using a string.format() method.
quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))

#Check file is empty or not
import os

size = os.stat("test.txt").st_size
if size == 0:
    print('file is empty')

#Read line number 4 from the following file
# read file
with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 3
    print(lines[2])
