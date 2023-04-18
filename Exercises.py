



for num in range(10):
    for i in range(num):
        print ( end="* ")
    print("\n")

#




quantity = 3
totalMoney = 1000
price = 450
statement1 = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement1.format(quantity, totalMoney, price))

#

print("Number Pattern ")
row = 10
for i in range(1, row + 1, 1):

    for j in range(1, i + 1):
        print(j, end=' ')

    print("")
